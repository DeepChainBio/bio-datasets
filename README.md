# bio-datasets
Open-source collection of biology datasets and pre-trained embeddings.

## Description
bio-datasets is a collaborative framework that allows the user to fetch publicly available sequence-based protein datasets.
For these datasets, pre-trained contextual embeddings are also available.


## Installation
Install the required dependencies with `pip install -r requirements.txt`.

# How it works

```python
from biodatasets import list_datasets, load_dataset

print(list_datasets())

my_dataset = load_dataset('test')
X, y = my_dataset.to_npy_arrays(input_names=['peptide'], target_names=['target'])

embeddings = my_dataset.get_embeddings(variable_name="peptide", model_name="protbert", embeddings_type="cls")
```
