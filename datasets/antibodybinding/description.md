# "Antibody Binding Energy" dataset


## Dataset Description
Antibody protein binding energy dataset.

### Dataset Summary

Antibody protein binding energy dataset. 40k antibody protein sequences. Embeddings available calculated with ProtBert

Features:
 - sequence
 - cdr1
 - cdr2
 - cdr3


Embeddings:
 - CDR1 embeddings - 1024-dim
 - CDR2 embeddings - 1024-dim
 - CDR3 embeddings - 1024-dim

Label:
 - binding energy

### Usage
```python
from biodatasets import load_dataset

pathogen_dataset = load_dataset("binding")

X, y = pathogen_dataset.to_npy_array(input_names=["sequence","cdr1","cdr2","cdr3"], target_names=["binding"])
cdr1_embeddings = pathogen_dataset.get_embeddings("sequence", "protbert", "cdr1")
```

### Supported Tasks
 - regression
 - binding energy prediction

### Model used to calculate Embeddings
 - ProtBert

### Libraries used to calculate embeddings
 - PyTorch


### Source Data

<!-- [Uniprot](https://www.uniprot.org/) -->
[DeepChain team](https://deepchain.bio)

### Dataset Curators

[DeepChain team](https://deepchain.bio)

### Licensing Information
<!-- [Creative Commons Attribution (CC BY 4.0)](https://www.uniprot.org/help/license)  -->
