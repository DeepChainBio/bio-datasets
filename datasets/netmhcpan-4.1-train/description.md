# "NetMHCpan-4.1" training dataset


## Dataset Description
- This dataset is the training set used in [NetMHCpan-4.1](https://academic.oup.com/nar/article/48/W1/W449/5837056) for which an [inference web server](http://www.cbs.dtu.dk/services/NetMHCpan/) is available.
- It contains 12868293 combinations of a peptide and a MHC allele (or multiple MHC alleles - the dataset contains multi-allelic data), associated with the binding target.
- 663767 of these samples are hits (positive binding).
- The data comes from mass-spectrometry (multi-allelic data) and binding affinity experiments (mono-allelic data).

- "Multi-allelic" means that one peptide is associated to a set of MHC alleles (up to 6). If it is a hit, we do not know to which MHC the peptide has been bound. Multi-allelic data cannot be used for training per se and requires a "deconvolution" method when evaluating a model on it. You can find a way to filter the data on mono-allelic data in the usage section.

- For the sake of completeness, please find below the detailed information from the [NetMHCpan-4.1 and NetMHCIIpan-4.0 paper](https://academic.oup.com/nar/article/48/W1/W449/5837056):

"EL MA training data for this method were extracted from Alvarez et al ​(2)​, Bulik-Sullivan et al. ​(4) and one in-house dataset. EL SA data were collected from Alvarez et al. ​(2)​, the IEDB ​(5) and DeVette et al. ​(6)​; BA data was gathered from Alvarez. et al ​(2) and the IEDB ​(5)​. An overview of the full training set is presented in Supplementary Table 1. All peptides employed in the training were filtered to only include 8 to 14 amino acid long peptides. All MHCs present in the BA subset were enriched with 100 random negative sequences (target value of 0.01). On the other hand, positive peptides for each MHC present in the EL subset were enriched, length-wise, with 5 times the amount of peptides of the most abundant peptide length, as described earlier ​(2)​. Random peptides were extracted from the UniProt database."


### Dataset Curation
This dataset has been concatenating raw EL (eluted ligands) data from NetMHCpan-4.1 training data and the corresponding allele(s) for each sample has been fetched.

### Dataset Summary

NetMHCpan-4.1 EL training dataset. Roughly 13M peptide/MHC-allele pairs. Embeddings available calculated with ProtBert.

Features:
 - peptide
 - MHC_allele

Embeddings:
 - CLS embeddings - 1024-dim

Label:
 - target
  - 0: non-binding (decoy)
  - 1: binding (hit)

### Usage
```python
from biodatasets import load_dataset
import pandas as pd

pathogen_dataset = load_dataset("netmhcpan-4.1-train")

X, y = pathogen_dataset.to_npy_arrays(input_names=["peptide", "MHC_allele"], target_names=["target"])
cls_embeddings = pathogen_dataset.get_embeddings("peptide", "protbert", "cls")

# Compute a mono-allelic data
data = pd.DataFrame(data=X, columns=["peptide", "MHC_allele"])
mono_allelic_data = data[~data["MHC_allele"].str.contains(";")] # Contains 4 113 332 samples (223 852 hits for 3 889 480 decoys - unbalanced!)

```

### Supported Tasks
 - binding prediction
 - antigen presentation prediction

### Model used to calculate Embeddings
 - ProtBert

### Libraries used to calculate embeddings
 - Pytorch


### Source Data

[NetMHC(I/II)pan-4.x data](http://www.cbs.dtu.dk/suppl/immunology/NAR_NetMHCpan_NetMHCIIpan/)


### Dataset Curators

[DeepChain team](https://deepchain.bio)

### Licensing Information
NetMHCpan-4.1 and NetMHCIIpan-4.0: Improved predictions of MHC antigen presentation by concurrent motif deconvolution and integration of MS MHC eluted ligand data
Birkir Reynisson, Bruno Alvarez, Sinu Paul, Bjoern Peters and Morten Nielsen
Nucleic Acids Research, May 2020, https://doi.org/10.1093/nar/gkaa379
