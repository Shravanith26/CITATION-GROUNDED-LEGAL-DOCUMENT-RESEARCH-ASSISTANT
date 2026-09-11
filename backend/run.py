import os
import sys
import uvicorn

# Ensure the backend directory is in the Python path
backend_dir = os.path.dirname(os.path.abspath(__file__))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from app.config.config import settings

if __name__ == "__main__":
    print(f"============================================================")
    print(f" Starting {settings.APP_NAME}")
    print(f" Host: {settings.API_HOST}:{settings.API_PORT}")
    print(f" Environment: {settings.APP_ENV}")
    print(f" Docs available at: http://{settings.API_HOST}:{settings.API_PORT}/docs")
    print(f"============================================================")
    uvicorn.run(
        "app.main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=settings.DEBUG,
        log_level="info"
    )
