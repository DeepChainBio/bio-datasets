from pathlib import Path
from typing import List
from typing import Optional
from typing import Union

from google.cloud import storage
from google.cloud.storage import Blob

from biodatasets import CACHE_DIRECTORY
from biodatasets import ROOT_DIRECTORY
from biodatasets.utils import logger

log = logger.get(__name__)

DATASET_BUCKET_NAME = "deepchain-datasets-public"


def list_blobs() -> List[Blob]:
    """Lists all the blobs for a bucket."""

    storage_client = storage.Client.create_anonymous_client()
    datasets_bucket = storage_client.get_bucket(DATASET_BUCKET_NAME)
    blobs = datasets_bucket.list_blobs()

    return blobs


def get_dataset_path(name: str) -> Path:
    """Get dataset path.

    Args:
        name: name of the dataset

    Returns: Path to cache directory of the dataset
    """
    return CACHE_DIRECTORY / name


def pull_dataset(name: str, force: bool = False) -> None:
    """Pull data from the Google Bucket.

    Args:
        name: name of the dataset
        force: force the download of the dataset
    """

    cache_dataset_directory = get_dataset_path(name)

    storage_client = storage.Client.create_anonymous_client()
    datasets_bucket = storage_client.get_bucket(DATASET_BUCKET_NAME)

    log.info(
        f"Start downloading {name} dataset in {cache_dataset_directory.relative_to(ROOT_DIRECTORY)} ..."
    )
    file_paths = [blob.name for blob in datasets_bucket.list_blobs(prefix=f"{name}/")]

    for file_path in file_paths:
        # filter on empty dataset folder path, in case the folder has been manually created
        if file_path[-1] != "/":
            download_from_bucket(datasets_bucket, file_path, force=force)


def download_from_bucket(
    bucket: storage.Bucket,
    bucket_file_path: str,
    local_file_path: Optional[Union[Path, str]] = None,
    force: bool = False,
) -> None:
    """
    Download the file from the bucket to the local machine.

    If the local_directory is specified the files are downloaded to this directory,
    otherwise the structure of the file path is preserved.

    Raises:
        FileNotFoundError: if the file does not exist.
    """
    gs_blob = bucket.blob(bucket_file_path)

    if not gs_blob.exists():
        raise FileNotFoundError(
            f"The file {bucket_file_path} does not exist in Google Bucket '{bucket.name}'"
        )

    if local_file_path is None:
        local_file_path = CACHE_DIRECTORY / bucket_file_path
    else:
        local_file_path = _convert_file_path(local_file_path).resolve()

    should_download = force or not local_file_path.exists()

    if should_download:
        local_file_path.parent.mkdir(exist_ok=True, parents=True)
        gs_blob.download_to_filename(local_file_path)
        log.info(
            f"File {bucket_file_path} downloaded from Google Bucket "
            f"'{bucket.name}' at {local_file_path.relative_to(ROOT_DIRECTORY)}"
        )


def _convert_file_path(file_path: Union[str, Path]) -> Path:
    if isinstance(file_path, str):
        file_path = Path(file_path)

    return file_path
