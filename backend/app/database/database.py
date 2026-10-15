import os
import shutil
import logging
from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base, sessionmaker
from app.config.config import settings

logger = logging.getLogger(__name__)

def resolve_safe_database_url() -> str:
    """
    Resolves a reliable, read-write database URL.
    On Streamlit Cloud or containerized deployments where /mount/src may be
    read-only or permission-restricted for SQLite journal/WAL creation,
    automatically copies the seeded corpus DB to a writable location (/tmp).
    """
    orig_url = settings.DATABASE_URL
    if not orig_url.startswith("sqlite:///"):
        return orig_url

    raw_path = orig_url.replace("sqlite:///", "")
    parent_dir = os.path.dirname(raw_path)

    # Check write capability
    is_writable = False
    try:
        os.makedirs(parent_dir, exist_ok=True)
        test_file = os.path.join(parent_dir, ".db_write_probe")
        with open(test_file, "w") as f:
            f.write("probe")
        if os.path.exists(test_file):
            os.remove(test_file)
        if os.path.exists(raw_path):
            is_writable = os.access(raw_path, os.W_OK)
        else:
            is_writable = True
    except Exception:
        is_writable = False

    # Force /tmp on Streamlit Cloud mount or non-writable paths
    if not is_writable or "/mount/src" in raw_path:
        tmp_db_path = "/tmp/legal_documents.db"
        if os.path.exists(raw_path):
            try:
                # Copy existing seeded database to /tmp if not present or smaller
                if not os.path.exists(tmp_db_path) or os.path.getsize(tmp_db_path) < os.path.getsize(raw_path):
                    shutil.copy2(raw_path, tmp_db_path)
            except Exception as e:
                logger.warning(f"Could not seed /tmp DB from {raw_path}: {e}")
        return f"sqlite:///{tmp_db_path}"

    return orig_url

ACTUAL_DATABASE_URL = resolve_safe_database_url()

# Create engine for SQLite
# check_same_thread=False allows multi-threaded access to SQLite
# timeout=30.0 avoids immediate OperationalError on concurrent queries
connect_args = {}
if "sqlite" in ACTUAL_DATABASE_URL:
    connect_args = {
        "check_same_thread": False,
        "timeout": 30.0
    }

engine = create_engine(
    ACTUAL_DATABASE_URL,
    connect_args=connect_args
)

if "sqlite" in ACTUAL_DATABASE_URL:
    @event.listens_for(engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        try:
            cursor = dbapi_connection.cursor()
            cursor.execute("PRAGMA busy_timeout=30000;")
            cursor.execute("PRAGMA synchronous=NORMAL;")
            cursor.close()
        except Exception:
            pass

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """Dependency for obtaining database session in FastAPI endpoints."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    """Initializes all database tables."""
    import app.database.models  # Ensure models are imported
    if "sqlite" in ACTUAL_DATABASE_URL:
        db_path = ACTUAL_DATABASE_URL.replace("sqlite:///", "")
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        logger.warning(f"init_db create_all notice: {e}")


