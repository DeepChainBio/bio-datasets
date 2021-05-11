"""
This module aims to define the Dataset class and the load_dataset api function.
"""
from pathlib import Path
from typing import List
from typing import Optional
from typing import Set
from typing import Tuple

import numpy as np
import pandas as pd

from biodatasets.utils import logger
from biodatasets.utils.google_bucket import get_dataset_path
from biodatasets.utils.google_bucket import list_blobs
from biodatasets.utils.google_bucket import pull_dataset

log = logger.get(__name__)


class Dataset:
    """Dataset class."""

    def __init__(self, name: str, force: bool = False):
        """Init the Dataset instance by fetching the dataset files.

        Args:
            name: name of the dataset
            force: force fetching the dataset
        """
        self.name = name
        self.path = get_dataset_path(name)
        if force or not self.path.exists():
            pull_dataset(name, force=force)

    def __repr__(self) -> str:
        """String representation of the dataset."""
        return f"Dataset(name={self.name}, available_columns={self.available_columns}, available_embeddings={self.available_embeddings})"

    @property
    def csv_path(self) -> Path:
        """Path to the CSV file."""
        return self.path / "dataset.csv"

    @property
    def description_path(self) -> Path:
        """Path to the description.md file."""
        return self.path / "description.md"

    @property
    def available_embeddings(self) -> Set[Tuple[str, str, str]]:
        """Return the available embeddings (column_name, model_name, type) for the dataset."""
        stems = [fp.stem.replace("_embeddings", "") for fp in self.path.glob("*_embeddings.npy")]
        return {tuple(stem.split("_")) for stem in stems}  # type: ignore

    @property
    def available_columns(self) -> List[str]:
        """Return the available columns in the dataset."""
        available_columns = pd.read_csv(self.csv_path, nrows=0).columns.tolist()

        # filter in case the column names include the index
        available_columns = list(filter(lambda x: x != "Unnamed: 0", available_columns))

        return available_columns

    def to_npy_arrays(
        self, input_names: List[str], target_names: Optional[List[str]] = None
    ) -> Tuple[List[np.ndarray], Optional[List[np.ndarray]]]:
        """Load dataset inputs and targets into numpy arrays.

        Args:
            input_names: list of input column names
            target_names: list of target column names

        Return:
            list of inputs arrays and targets arrays

        Raises:
            ValueError: one or several columns are not available
        """
        columns_to_load = input_names + target_names if target_names is not None else input_names

        available_columns = set(pd.read_csv(self.csv_path, nrows=1).columns)
        not_available_columns = set(columns_to_load) - available_columns

        if not_available_columns:
            raise ValueError(f"The following columns are not available: {not_available_columns}")

        df = pd.read_csv(self.csv_path, usecols=columns_to_load)

        inputs = [df[input_name].values for input_name in input_names]

        targets = None
        if target_names is not None:
            targets = [df[target_name].values for target_name in target_names]

        return inputs, targets

    def get_embeddings(
        self,
        variable_name: str,
        model_name: str = "esm-1b",
        embeddings_type: str = "cls",
    ) -> np.ndarray:
        """Return a 2D numpy array with the pretrained embeddings for each sequence.

        Args:
            variable_name: name of the sequence variable
            model_name: name of the model from which come the embeddings
            embeddings_type: type of the embeddings

        Return:
            list of inputs arrays and targets arrays

        Raises:
            ValueError: the embeddings are not available
        """
        if (
            variable_name,
            model_name,
            embeddings_type,
        ) not in self.available_embeddings:
            msg = f"""The embeddings for the sequence {variable_name} with model {model_name} and type {embeddings_type}
            are not available.
            Embeddings available: {self.available_embeddings}
            """
            raise ValueError(msg)

        embeddings = np.load(
            self.path / f"{variable_name}_{model_name}_{embeddings_type}_embeddings.npy"
        )

        return embeddings

    def display_description(self) -> None:
        """Display the description of the dataset."""
        with open(self.description_path, "r") as description_file:
            print(description_file.read())


def list_datasets(include_tests: bool = False) -> List[str]:
    """List all the datasets in the bucket.

    Args:
        include_tests: include test datasets in the list

    Return:
        list of the datasets
    """
    blobs = list_blobs()
    dataset_names = list(set(map(lambda x: x.name.split("/")[0], blobs)))
    if not include_tests:
        dataset_names = list(filter(lambda x: not x.startswith("test"), dataset_names))

    return dataset_names


def load_dataset(name: str, force: bool = False) -> Optional[Dataset]:
    """Load a bio-dataset.

    Args:
        name: name of the dataset
        force: force fetching the dataset

    Return:
        a Dataset instance
    """
    available_datasets = list_datasets(include_tests="test" in name)

    if name not in available_datasets:
        log.error(f"Dataset {name} does not exist.")
        return None

    return Dataset(name, force=force)
