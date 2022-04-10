# %%
import subprocess

# %%
files = [
    's3://drivendata-competition-airathon-public-us/pm25/train/maiac/2018/20180604T054500_maiac_dl_0.hdf',
    's3://drivendata-competition-airathon-public-us/pm25/train/maiac/2019/20190604T065000_maiac_dl_0.hdf',
    's3://drivendata-competition-airathon-public-us/pm25/train/maiac/2020/20200604T070000_maiac_dl_0.hdf',
    's3://drivendata-competition-airathon-public-us/pm25/train/maiac/2018/20180216T065500_maiac_dl_0.hdf'
]

# %%
for file in files:
    subprocess.run(["aws", "s3", "cp", file, "./dataset", "--no-sign-request"])

# %%
