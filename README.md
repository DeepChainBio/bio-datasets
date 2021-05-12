<p align="center">
  <img width="50%" src="https://raw.githubusercontent.com/DeepChainBio/bio-datasets/main/.source/_static/deepchain.png">
</p>


![PyPI](https://img.shields.io/pypi/v/bio-datasets)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)

# Bio-datasets
Open-source collection of biology datasets and pre-trained embeddings. :dna: :closed_book:

## Description
bio-datasets is a collaborative framework that allows the user to fetch publicly available sequence-based protein datasets.
For these datasets, pre-trained contextual embeddings are also available.


## Installation
Install the required dependencies with `pip install bio-datasets`.

# How it works

```python
from biodatasets import list_datasets, load_dataset

print(list_datasets())

# Load your dataset
pathogen = load_dataset("pathogen")

# Display the available columns and embeddings
print(pathogen)

# Get data from your dataset
X, y = pathogen.to_npy_arrays(input_names=["sequence"], target_names=["class"])
embeddings = pathogen.get_embeddings("sequence", "protbert", "cls")

# Get a full description of your dataset
pathogen.display_description()
```

# How to contribute
Check out how to setup the project or **add a public dataset** in [CONTRIBUTING.md](CONTRIBUTING.md).
