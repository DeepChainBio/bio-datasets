# Contributing

### Add a dataset :closed_book:

1. First, fork the repository by clicking on the 'Fork' button in the [repository](https://github.com/DeepChainBio/bio-datasets). Then, clone your fork locally with:
```bash
git clone git@github.com:<your Github username>/bio-datasets.git
cd bio-datasets
git remote add upstream https://github.com/DeepChainBio/bio-datasets.git
```

2. Set your environment and install _pre-commit hooks_ by following the [project setup section](./CONTRIBUTING.md#project-setup-nerd_face).

3. Create a new branch: `git checkout -b contribute/name-of-your-dataset`.

4. Prepare your dataset. The latter must contains the 3 following files:
    - `dataset.csv` - which is your dataset (all your features + targets) without any embeddings.
    - `info.json` - an information file for the hub frontend - you can find a template [here](./templates/description.md).
    - `description.md` - a description file for your dataset - you can find a template [here](./templates/description.md).

5. Complete your dataset with embeddings for some of its feature sequences:
    - You can add an _embeddings file_ **per [sequence, model, pooling_type]**, e.g. `sequence1_protbert_cls_embeddings.npy`.
    - The given model should be the one used to compute these embeddings (e.g. `protbert`).
    - The pooling type refers to the way the embeddings are extracted from the last layer of the pre-trained Transformer , i.e. `cls` or `mean`.
    - One _embeddings file_ should be written as the following: `<column_name_in_dataset.csv>_<model_name_to_compute_embeddings>_<pooling_type>_embeddings.npy`.
    - For now, only this format (`.csv` for the dataset + `.npy` files for embeddings) is supported. The plan is to integrate different formats in the next weeks!

6. Create a folder for your dataset in [`datasets/`](./datasets) and add the `description.md` file in it.
    - The remaining files will need to be added to a google bucket. This is explained in the [template](./.github/PULL_REQUEST_TEMPLATE/new_dataset_pull_request_template.md) with which you will open your pull request.

7. Commit your changes:
```bash
git add datasets/<your_dataset_name>
git commit
```

8. Rebase on the upstream `main` branch and push your changes:
```bash
git fetch upstream
git rebase upstream/main
git push -u origin contribute/name-of-your-dataset
```

9. Go to the webpage of your fork on GitHub. Click on "Pull request" and choose the PR template _new_dataset_pull_request_template.md_.

10. Complete the check-list and wait for your PR to be reviewed, and your dataset to be added.

All good, you've officially contributed a publicly available _protein dataset_. :rocket:


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
