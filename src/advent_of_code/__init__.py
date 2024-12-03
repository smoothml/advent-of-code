from pathlib import Path

from dotenv import find_dotenv

ROOT_DIR = Path(find_dotenv("pyproject.toml")).parent
DATA_DIR = ROOT_DIR / "data"
