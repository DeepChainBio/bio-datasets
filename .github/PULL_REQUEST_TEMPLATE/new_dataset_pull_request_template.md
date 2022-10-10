## Contribute a new bio-dataset
- Dataset name: `your_dataset_name`.
:warning: It must be the same name as the dataset folder in the bucket.

### Checklist :white_check_mark:

#### Misc
- [ ] I have read and followed the instructions in **[CONTRIBUTING.md](../../CONTRIBUTING.md)**.
- [ ] I have described my dataset in `description.md` and `info.json` files.
- [ ] My dataset is gathered into `dataset.csv`. This `.csv` file must contain a **header** and be `,`-separated.
- [ ] _Optional:_ I have computed embeddings for feature sequences of my dataset. One embedding file is **per [sequence, model, pooling_type]**.

#### Google bucket
- [ ] I have created a folder with the name of my dataset in the :file_cabinet: [_buffer_ google bucket](https://console.cloud.google.com/storage/browser/deepchain-datasets-buffer). :warning: You must be authenticated with a gmail account.
- [ ] I have uploaded `description.md`, `info.json` and `dataset.csv`, as well as all the _embeddings_ files.

#### Github
- [ ] I have added a folder with the name of my dataset in [`datasets/`](../../datasets).
- [ ] I have added the `description.md` file in my dataset folder.
- [ ] I have added a reviewer to this pull request. Reviewers: @delfosseaurelien or @theomeb.

:tada: Congrats, your dataset is going to be reviewed and will soon be pushed to this [bucket](https://console.cloud.google.com/storage/browser/deepchain-datasets-public) and available with the API. :rocket:
