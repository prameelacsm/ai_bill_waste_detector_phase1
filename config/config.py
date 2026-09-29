"""
config/config.py
-----------------
Central configuration for the AI Bill & Subscription Waste Detector.

Every other module should import settings FROM HERE instead of calling
os.getenv() directly. This keeps configuration in one place and makes
it easy to see every setting the app depends on.

Usage:
    from config.config import settings
    print(settings.DATABASE_URL)
"""

import os
from dataclasses import dataclass, field
from pathlib import Path

from dotenv import load_dotenv

# ----------------------------------------------------------------------
# Load the .env file (if present) into environment variables.
# This must happen BEFORE we read any os.getenv() calls below.
# ----------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)


def _get_bool(env_var: str, default: bool = False) -> bool:
    """Read an environment variable as a boolean ('true'/'1'/'yes')."""
    value = os.getenv(env_var)
    if value is None:
        return default
    return value.strip().lower() in {"true", "1", "yes"}


def _get_int(env_var: str, default: int) -> int:
    """Read an environment variable as an int, falling back safely."""
    value = os.getenv(env_var)
    if value is None or value.strip() == "":
        return default
    try:
        return int(value)
    except ValueError:
        return default


@dataclass(frozen=True)
class Settings:
    """
    Immutable settings object built once at import time.

    Using a dataclass (instead of scattering os.getenv calls everywhere)
    means:
      - Autocomplete works in your editor.
      - There's exactly one place to look when something is misconfigured.
      - Tests can construct a Settings object with custom values easily.
    """

    # ---- Paths ----
    BASE_DIR: Path = BASE_DIR
    DATA_DIR: Path = BASE_DIR / "data"
    RAW_DATA_DIR: Path = BASE_DIR / "data" / "raw"
    PROCESSED_DATA_DIR: Path = BASE_DIR / "data" / "processed"
    SAMPLE_TRANSACTIONS_PATH: Path = BASE_DIR / "data" / "sample_transactions.csv"
    MODEL_DIR: Path = BASE_DIR / "ml" / "models"
    DATABASE_DIR: Path = BASE_DIR / "database"

    # ---- Database ----
    DATABASE_URL: str = field(
        default_factory=lambda: os.getenv(
            "DATABASE_URL", "sqlite:///database/app.db"
        )
    )

    # ---- Generative AI ----
    GEMINI_API_KEY: str = field(default_factory=lambda: os.getenv("GEMINI_API_KEY", ""))
    LLM_PROVIDER: str = field(default_factory=lambda: os.getenv("LLM_PROVIDER", "gemini"))
    LLM_MODEL_NAME: str = field(
        default_factory=lambda: os.getenv("LLM_MODEL_NAME", "gemini-1.5-flash")
    )
    LLM_TIMEOUT_SECONDS: int = field(
        default_factory=lambda: _get_int("LLM_TIMEOUT_SECONDS", 20)
    )

    # ---- File Upload ----
    MAX_UPLOAD_SIZE_MB: int = field(
        default_factory=lambda: _get_int("MAX_UPLOAD_SIZE_MB", 15)
    )
    ALLOWED_EXTENSIONS: tuple = (".csv", ".xlsx", ".xls", ".pdf", ".png", ".jpg", ".jpeg")

    # ---- OCR ----
    TESSERACT_CMD_PATH: str = field(
        default_factory=lambda: os.getenv("TESSERACT_CMD_PATH", "")
    )

    # ---- App behavior ----
    CURRENCY_SYMBOL: str = field(default_factory=lambda: os.getenv("CURRENCY_SYMBOL", "₹"))
    LOG_LEVEL: str = field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))

    @property
    def ai_enabled(self) -> bool:
        """True only when an API key has actually been provided."""
        return bool(self.GEMINI_API_KEY.strip())


# A single shared instance every module imports.
settings = Settings()


def ensure_directories() -> None:
    """
    Create any data/model/database directories that don't exist yet.
    Safe to call multiple times (idempotent). Called once on app startup.
    """
    for directory in (
        settings.DATA_DIR,
        settings.RAW_DATA_DIR,
        settings.PROCESSED_DATA_DIR,
        settings.MODEL_DIR,
        settings.DATABASE_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    # Quick manual check: run `python config/config.py` to print current settings.
    ensure_directories()
    print("Loaded settings:")
    for key, value in settings.__dict__.items():
        # Never print the raw API key to the console.
        if key == "GEMINI_API_KEY":
            value = "SET" if value else "NOT SET"
        print(f"  {key}: {value}")
