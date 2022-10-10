# "Pfam-32.0" dataset


## Dataset Description
Pfam - protein family classification dataset - version 32.0.

### Dataset Summary

Pfam-32.0 dataset. 1 339 083 protein sequences, associated to a family_id. Embeddings (mean) calculated with ProtBert, available for all the sequences. In order to compute these embeddings, the sequences have been trimmed to a max length of 120. The original train/dev/test is given in the "split" column.

Features:
 - sequence
 - sequence_name
 - family_accession
 - split

Embeddings:
 - MEAN embeddings - 1024-dim

Label:
 - family_id - 17929 unique classes - 13071 present in all splits.

### Usage
```python
from biodatasets import load_dataset

dataset = load_dataset("pfam-32.0")

X, y = dataset.to_npy_arrays(input_names=["sequence", "sequence_name", "split"], target_names=["family_id"])
cls_embeddings = dataset.get_embeddings("sequence", "protbert", "mean")
```

### Supported Tasks
 - classification

### Model used to calculate Embeddings
 - ProtBert

### Libraries used to calculate embeddings
 - bio-transformers (torch)


### Source Data

[Pfam32.0](ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam32.0/Pfam-A.seed.gz)

The split is taken from the one given on [Kaggle](https://www.kaggle.com/googleai/pfam-seed-random-split).



### Dataset Curators

[DeepChain team](https://deepchain.bio)

### Licensing Information
[Creative Commons Legal Code (CCO 1.0 Universal)](https://www.kaggle.com/googleai/pfam-seed-random-split)
