# "Human vs pathogen" dataset


## Dataset Description
Human vs pathogen classification dataset.

### Dataset Summary

Human vs pathogen classification dataset. 96k protein sequences (50% human, 50% pathogens). Extracted from Uniprot. Embeddings available calculated with ProtBert (_CLS_ pooling type).

Features:
 - sequence
 - sequence_id

Embeddings:
 - CLS embeddings - 1024-dim

Label:
 - class
  - 0: human
  - 1: pathogen

### Usage
```python
from biodatasets import load_dataset

pathogen_dataset = load_dataset("pathogen")

X, y = pathogen_dataset.to_npy_arrays(input_names=["sequence"], target_names=["class"])
cls_embeddings = pathogen_dataset.get_embeddings("sequence", "protbert", "cls")
```

### Supported Tasks
 - classification
 - immunogenicity

### Model used to calculate Embeddings
 - [prot-bert]()

### Libraries used to calculate embeddings
 - Pytorch


### Source Data

[Uniprot]()


### Dataset Curators

[DeepChain team]()

### Licensing Information
[Creative Commons Attribution (CC BY 4.0)]()
