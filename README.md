# bio-datasets
Open-source collection of biology datasets and pre-trained embeddings.

## Description
bio-datasets is a collaborative framework that allows the user to fetch publicly available sequence-based protein datasets.
For these datasets, pre-trained contextual embeddings are also available.


## Installation
Install the required dependencies with `pip install biodatasets`.

# How it works

```python
from biodatasets import list_datasets, load_dataset

print(list_datasets())

pathogen = load_dataset("pathogen")
X, y = pathogen.to_npy_arrays(input_names=["sequence"], target_names=["class"])
embeddings = pathogen.get_embeddings("sequence", "protbert", "cls")
```
