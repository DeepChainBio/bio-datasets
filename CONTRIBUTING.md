# Contributing

### Add a dataset :closed_book:

In order to make a dataset available with the `bio-datasets` API, you need to:
1. Create a folder in this [google storage bucket](https://console.cloud.google.com/storage/browser/deepchain-datasets-public).
   The folder name should be your dataset name, e.g. `pathogen`.


2. Then you need to add in this folder the 3 following files:
    - `dataset.csv` - which is your dataset (all your features + targets) without any embeddings.
    - `info.json` - an information file for the hub frontend, you can download an example from others datasets in the bucket and then edit it.
    - `description.md` - a description file for your dataset, you can get the template from other datasets as well.


3. You're good, you've officially added a publicly available _protein dataset_. :rocket:


4. A complete dataset should have embeddings for some of its feature sequences. You can add an embeddings file **per [sequence, model, pooling_type]** used to compute these embeddings (e.g. `protbert`):
    - `sequence_protbert_cls_embeddings.npy` - a file for all the embeddings for 1 feature of your dataset.
      The _embeddings file_ should be written as the following:
      ```
      <column_name_in_dataset.csv>_<model_name_to_compute_embeddings>_<pooling_type>_embeddings.npy.
      ```
For now, only this format (`.csv` + `.npy` files for embeddings) is supported. The plan is to integrate different formats in the next weeks!

### Project setup :nerd_face:

- create the conda environment
```bash
conda env create -f environment.yaml
```
- install the pre-commit
```bash
conda activate biodatasets
(biodatasets) pre-commit install
```
