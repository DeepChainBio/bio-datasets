# "RNA Binding Protein Prediction" dataset


## Dataset Description
RNA Binding Protein vs non-RNA Binding Protein classification dataset

### Dataset Summary

 RNA Binding Protein vs non-RNA Binding Protein classification dataset. 14725 protein sequences (3713 RNA Binding Protein, 11012 non-RNA Binding Protein). Respectively extracted from [UniProt](https://www.uniprot.org/) and [PISCES](http://dunbrack.fccc.edu/pisces/) based on sequence length (range [40, 1000]). Embeddings available calculated with ProtBert (_cls_ pooling type).

Features:
 - sequence
 - sequence_ID

Embeddings:
 - CLS embeddings - 1024-dim

Label:
  class
  - 0: non-RNA Binding Protein
  - 1: RNA Binding Protein

### Usage
```python
from biodatasets import load_dataset
dataset = load_dataset("RNABindingProtein")
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
 - [PISCES](http://dunbrack.fccc.edu/pisces/)


### Dataset Curators

[DeepChain team](https://deepchain.bio/)

### Licensing Information
[Creative Commons Attribution (CC BY 4.0)]((https://www.uniprot.org/help/license))
