# "Toxicity Prediction" dataset


## Dataset Description
Toxic vs non-Toxic Protein/Peptide classification dataset

### Dataset Summary

 Toxic vs non-Toxic Protein classification dataset. 7996 protein sequences extracted from [UniProt](https://www.uniprot.org/) based on sequence length (range [10, 1000]). Embeddings available calculated with ProtBert (_cls_ pooling type).

Features:
 - sequence


Embeddings:
 - CLS embeddings - 1024-dim

Label:
  class
  - 0: non-Toxic Protein
  - 1: Toxic Protein

### Usage
```python
from biodatasets import load_dataset
dataset = load_dataset("toxicity")
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
