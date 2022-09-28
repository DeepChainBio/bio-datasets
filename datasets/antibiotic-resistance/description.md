# "Antibiotic Resistance" dataset


## Dataset Description
Antibiotic resistance prediction  dataset

### Dataset Summary

  Antibiotic resistance prediction dataset encompasses 17k protein sequences extracted from [HMD-ARG-DB](http://www.cbrc.kaust.edu.sa/HMDARG/dataset). Embeddings available calculated with esm1_t34_670M_UR100 (_cls_ pooling type).

Features:
 - sequence
 - description


Embeddings:
 - CLS embeddings - 1280-dim

Label:

  - 0: non-Antibiotic resistance Protein
  - 1: Antibiotic resistance Protein

### Usage
```python
from biodatasets import load_dataset
dataset = load_dataset("antibiotic-resistance")
X, y = dataset.to_npy_arrays(input_names=["sequence"], target_names=["label"])
cls_embeddings = dataset.get_embeddings("sequence", "esm1-t34-670M-UR100", "cls")
mean_embeddings = dataset.get_embeddings("sequence", "esm1-t34-670M-UR100", "mean")
```

### Supported Tasks
 - classification
 - multi-task learning


### Model used to calculate Embeddings
 - [esm1_t34_670M_UR100](https://pypi.org/project/bio-transformers/)

### Libraries used to calculate embeddings
 - Pytorch


### Source Data

 - [HMD-ARG-DB](http://www.cbrc.kaust.edu.sa/HMDARG/dataset.html)



### Dataset Curators

[DeepChain team](https://deepchain.bio/)

### Licensing Information
[Creative Commons Attribution (CC BY 4.0)]((https://www.uniprot.org/help/license))
