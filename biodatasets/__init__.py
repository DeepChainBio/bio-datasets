"""Define all the useful directories for the project.

- ROOT_DIRECTORY: main directory

- CURRENT_DIRECTORY: directory with all the code

- CACHE_DIRECTORY: directory used to store the cache datasets
"""
from pathlib import Path

CURRENT_DIRECTORY = Path(__file__).resolve().parent
ROOT_DIRECTORY = CURRENT_DIRECTORY.parent

CACHE_DIRECTORY = ROOT_DIRECTORY / ".cache"

from .dataset import list_datasets  # noqa: E402
from .dataset import load_dataset  # noqa: E402
