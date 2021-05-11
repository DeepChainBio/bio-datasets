# "SwissProt" dataset


## Dataset Description
SwissProt dataset.

### Dataset Summary

SwissProt dataset. 456 669 protein sequences with description. Extracted from UniProtKB/Swiss-Prot. Embeddings (<MEAN> and <CLS>) available calculated with ESM-1b

Features:
 - sequence
 - description

Embeddings:
 - MEAN embeddings - 1280-dim
 - CLS embeddings - 1280-dim

Label:


### Usage
```python
from biodatasets import load_dataset

swissprot_dataset = load_dataset("swissProt")

X, y = swissprot_dataset.to_npy_array(["sequence"])
mean_embeddings = swissprot_dataset.get_embeddings("sequence", "esm1b", "mean")

```

### Supported Tasks

### Model used to calculate Embeddings
 - ESM-1b

### Libraries used to calculate embeddings
 - Pytorch


### Source Data

[Uniprot](https://www.uniprot.org/)


### Dataset Curators

[DeepChain team](https://deepchain.bio)

### Licensing Information
[Creative Commons Attribution (CC BY 4.0)](https://www.uniprot.org/help/license)
