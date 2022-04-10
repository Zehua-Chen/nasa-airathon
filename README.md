# COMS 4995 Competition



## Content

- [`dataset`](dataset/): where training and testing data are stored
- [`docs`](docs/): example code on topics of Tensorflow and feature exploration
- [`airathon`](airathon/): utility packages and CLI tools
  - `airathon.model.tfrecord`: tf record creation
  - `airathon.metrics`: R2 implementation
  - `airathon.model`: synced with [`model.ipynb`](model.ipynb) and 
    [`model.modis.ipynb`](model.modis.ipynb)
  - `airathon.paths`: helper function for finding files in repo
- [`saves`](saves/): model training checkpoint
- [`Leaderboard`](Leaderboard.png): proof of getting on leaderboard on Feb 17
- [`test`](tests/): unit testing

### Notebook

- [`model.ipynb`](model.ipynb): where the model is developed
- [`model.modis.ipynb`](model.modis.ipynb): modis loading code
- [`tfrecord.ipynb`](tfrecord.ipynb): TFRecord creationg

## Get Started

### Setting Up Virtual Machine

1. Create a [deep learning VM](https://cloud.google.com/deep-learning-vm)
3. If GPU cannot be detected, run NVIDIA driver install script provided by
   Google
   ```
   $ sudo /opt/deeplearning/install-driver.sh
   ```

### Download Prebuilt TF Records

```
$ gsutil cp gs://zc2616_coms4995_22_competition/train-maiac-2000.tfrecord dataset/train/maiac/maiac-2000.tfrecord
$ gsutil cp gs://zc2616_coms4995_22_competition/test-maiac.tfrecord dataset/test/maiac/maiac.tfrecord
```

### Installing Python and Dependencies

1. Create a conda environment from [`requirements.txt`](requirements.txt)
2. Run `pip install -e .` at repo root to install the repo as an editable python
   package

### Jupyter Notebook

Open [model.ipynb](model.ipynb) to train the model

## Development

#### Creating TF Records

First download raw data from Amazon S3

```
$ aws s3 cp s3://drivendata-competition-airathon-public-us/pm25/test/maiac dataset/test/maiac/ --no-sign-request --recursive
$ aws s3 cp s3://drivendata-competition-airathon-public-us/pm25/train/maiac dataset/train/maiac/ --no-sign-request --recursive
```

Then create tf records using 

```
$ airathon tfrecord dataset/metadata/train_labels.csv train
$ airathon tfrecord dataset/metadata/submission_format.csv test
```

Created TF records will be placed at

1. `dataset/train/maiac/maiac.tfrecord`
2. `dataset/test/maiac/maiac.tfrecord`

### Developing Model

Model and preprocessing should be developed in [model.ipynb](model.ipynb)

### Syncing With `airathon` package

- `nbdev_build_lib`

### Source Control

Before pushing notebook, make sure to run `nbdev_clean_nbs` to clean notebooks
