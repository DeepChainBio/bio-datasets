# "Solubility Prediction" dataset


## Dataset Description
 Prediction of soluble protein expression in _Esherichia coli_

### Dataset Summary

 Soluble vs non-Soluble Protein classification dataset. 14536 protein sequences downloaded from [SoluProt](https://loschmidt.chemi.muni.cz/soluprot/) web application. Embeddings available calculated with ProtBert (_cls_ pooling type).

Features:
 - sequence


Embeddings:
 - CLS embeddings - 1024-dim

Label:
  class
  - 0: non-Soluble Protein
  - 1: Soluble Protein

### Usage
```python
from biodatasets import load_dataset
dataset = load_dataset("solubility")
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

 - [SoluProt](https://loschmidt.chemi.muni.cz/soluprot/?page=download)



### Dataset Curators

[DeepChain team](https://deepchain.bio/)

### Licensing Information
[Acedemic licence agreement]((https://loschmidt.chemi.muni.cz/soluprot/?page=terms-of-use))
