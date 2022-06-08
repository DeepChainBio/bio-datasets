# "Quaternary Structure" dataset


## Dataset Description
Quaternary structure prediction dataset

### Dataset Summary

Quaternary structure  dataset with 10237 protein sequences retrieved from [UniProt](https://www.uniprot.org/). Embeddings available calculated with ProtBert (_cls_ pooling type).

Features:
 - sequence


Embeddings:
 - CLS embeddings - 1024-dim

Label:
  class
  - hetero-decamer:0
  - hetero-dimer:1
  - hetero-dodecamer:2
  - hetero-hexamer:3
  - hetero-octamer:4
  - hetero-pentamer:5
  - hetero-tetramer:6
  - hetero-trimer:7
  - homo-decamer:8
  - homo-dimer:9
  - homo-dodecamer:10
  - homo-hexamer:11
  - homo-octamer:12
  - homo-pentamer:13
  - homo-tetramer:14
  - homo-trimer:15
  - monomer:16

### Usage
```python
from biodatasets import load_dataset
dataset = load_dataset("quaternary-structure")
X, y = dataset.to_npy_arrays(input_names=["sequence"], target_names=["label"])
cls_embeddings = dataset.get_embeddings("sequence", "protbert", "cls")
```

### Supported Tasks
 - classification


### Model used to calculate Embeddings
 - [protbert](https://pypi.org/project/bio-transformers/)

### Libraries used to calculate embeddings
 - Pytorch


### Source Data

 - [UniProt](https://www.uniprot.org/)



### Dataset Curators

[DeepChain team](https://deepchain.bio/)

### Licensing Information
[Creative Commons Attribution (CC BY 4.0)]((https://www.uniprot.org/help/license))
