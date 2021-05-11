from pathlib import Path
from unittest.mock import MagicMock
from unittest.mock import patch
from unittest.mock import PropertyMock

import pytest
from google.cloud.storage import Blob

from biodatasets import list_datasets
from biodatasets.dataset import Dataset
from biodatasets.utils.google_bucket import DATASET_BUCKET_NAME


@pytest.fixture()
def dataset_description_path(tmp_path_factory) -> Path:
    """Fixture to define the dataset description_path."""
    dataset_path = tmp_path_factory.mktemp("test_dataset") / "description.md"
    description = "This is a fake description of the dataset.\nAnother line."
    with open(dataset_path, "w") as file:
        file.write(description)

    return dataset_path


@patch("biodatasets.dataset.pull_dataset")
@patch("biodatasets.dataset.Dataset.description_path", new_callable=PropertyMock)
def test_display_description_describe(
    desc_path_mock: MagicMock, pull_dataset_mock: MagicMock, dataset_description_path, capfd
):
    # mock pull_dataset to avoid loading a dataset
    pull_dataset_mock.return_value = None

    desc_path_mock.return_value = dataset_description_path
    dataset = Dataset("test")
    dataset.display_description()

    out, _ = capfd.readouterr()
    assert out == "This is a fake description of the dataset.\nAnother line.\n"


@patch("biodatasets.dataset.list_blobs")
@pytest.mark.parametrize("include_tests", [False, True])
def test_list_datasets(list_blobs_mock: MagicMock, include_tests: bool):
    list_blobs_mock.return_value = [
        Blob(name=x, bucket=DATASET_BUCKET_NAME)
        for x in [
            "test_1/dataset.csv",
            "pathogen",
            "pathogen/description.md",
            "protein-binding/info.json",
            "test2",
        ]
    ]

    datasets = list_datasets(include_tests)

    list_blobs_mock.assert_called_once()
    if include_tests:
        assert set(datasets) == {"test_1", "pathogen", "protein-binding", "test2"}
    else:
        assert set(datasets) == {"pathogen", "protein-binding"}
