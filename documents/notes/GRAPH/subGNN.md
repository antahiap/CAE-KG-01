```
cd /home/apakiman/Projects/SubGNN/prepare_dataset
conda activate subGemb_update

```

for pytorch geometry installation, use setup from [link](https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html) with:
```
pip install torch-scatter==latest+cu101 -f https://pytorch-geometric.com/whl/torch-1.4.0.html
```

additional installation:

```
python -m pip install snap-stanford
pip install pytorch-lightning
pip install optuna
pip install fastdtw
pip install commentjson
```

[pytorch-lightning](https://pytorch-lightning.readthedocs.io/_/downloads/en/stable/pdf/)
changes to the code:
- in SubGNN.py __init, comment self.device, it fails when it is figured
- in train.config. build_trainer > ModelCheckpoint, filepath --> dirpath, no arguement as filepath


### Leo1
```	
module load Anaconda3 CUDA
conda create --clone /opt/software/easybuild/software/Anaconda3/2020.02/envs/pytorch-02-2021/ --prefix=./envs
source activate ./envs

pip install pytorch_lightning
pip install optuna
pip install fastdtw

sbatch run.sh 


cd /home/apakiman/Projects/SubGNN
```


- gcc issue `distutils.errors.CompileError: command 'gcc' failed with exit status 1` 

```
conda install -c conda-forge fbprophet

```
