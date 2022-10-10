# "AlphaFold" dataset


## Dataset Description
AlphaFold dataset.

### Dataset Summary

AlphaFold dataset. 456.007 protein sequences extracted from AlphaFold Protein Structure Database. Embeddings available calculated with ProtBert (_mean_ pooling type).

Features:
 - sequence
 - sequence_ID

Embeddings:
 - MEAN embeddings - 1024-dim


Label:
 - Predicted local distance difference test (__pLDDT__) values

### Usage
```python 
from biodatasets import load_dataset

alphafold_dataset = load_dataset("alphafold")

X, y = alphafold_dataset.to_npy_arrays(["sequence"], target_names=["label"])
mean_embeddings = alphafold_dataset.get_embeddings("sequence", "protbert", "mean")
```

### Supported Tasks
 - pLDDT prediction


### Model used to calculate Embeddings
 - ProtBert

### Libraries used to calculate embeddings
 - Pytorch


### Source Data

[AlphaFold](https://alphafold.ebi.ac.uk/download)


### Dataset Curators

[DeepChain team](https://deepchain.bio)

### Licensing Information
[Creative Commons Attribution (CC BY 4.0)](https://alphafold.ebi.ac.uk/download)
