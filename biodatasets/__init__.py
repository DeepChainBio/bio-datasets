"""Define all the useful directories for the project.

- ROOT_DIRECTORY: main directory

- CURRENT_DIRECTORY: directory with all the code

- HOME_DIRECTORY: home directory

- CACHE_DIRECTORY: directory used to store the cache datasets
"""
from pathlib import Path

CURRENT_DIRECTORY = Path(__file__).resolve().parent
ROOT_DIRECTORY = CURRENT_DIRECTORY.parent

HOME_DIRECTORY = Path.home()
CACHE_DIRECTORY = HOME_DIRECTORY / ".cache" / "bio-datasets"

from .dataset import list_datasets  # noqa: E402
from .dataset import load_dataset  # noqa: E402
