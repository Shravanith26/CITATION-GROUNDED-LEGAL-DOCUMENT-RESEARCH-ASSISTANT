import os
from typing import Tuple

ALLOWED_EXTENSIONS = {".txt", ".pdf", ".md", ".json"}
MAX_FILE_SIZE_BYTES = 50 * 1024 * 1024  # 50 MB

def validate_uploaded_file(filename: str, file_size: int) -> Tuple[bool, str]:
    """
    Validates uploaded document filename and file size.
    Returns (is_valid, error_message).
    """
    if not filename:
        return False, "Filename cannot be empty."

    ext = os.path.splitext(filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return False, f"Unsupported file type '{ext}'. Allowed types: {', '.join(sorted(ALLOWED_EXTENSIONS))}"

    if file_size <= 0:
        return False, "File is empty."

    if file_size > MAX_FILE_SIZE_BYTES:
        return False, f"File size exceeds limit of {MAX_FILE_SIZE_BYTES // (1024*1024)} MB."

    return True, ""
