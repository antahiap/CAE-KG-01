## Model Info

- https://www.ccsa.gmu.edu/models/2020-nissan-rogue/

### Unit System

| MASS | LENGTH | TIME | FORCE | STRESS | ENERGY | DENSITY  | YOUNG's  | 35MPH / 56.33KMPH | GRAVITY   |
| ---- | ------ | ---- | ----- | ------ | ------ | -------- | -------- | ----------------- | --------- |
| ton  | mm     | s    | N     | MPa    | N-mm   | 7.83e-09 | 2.07e+05 | 1.56e+04          | 9.806e+03 |

## Daniela SETUP

you can find the nissan rogue model https://www.ccsa.gmu.edu/models/2020-nissan-rogue/

I have downloaded the model and documentation is here: `/home/ndv/data/Nissan_Rogue_2020_CCSA_public`

inputdeck:
`/home/ndv/data/Nissan_Rogue_2020_CCSA_public/2020-nissan-rogue-v2`

I run the initial setup and one variation with thickness variation of a single

part (for simcompare test), simulation results are available here

```
/home/ndv/data/Nissan_Rogue_2020_CCSA_public/Output/Initial
/home/ndv/data/Nissan_Rogue_2020_CCSA_public/Output/p2000646-m5
```

I used on leo cluster.

```
mpirun ls-dyna_mpp_s_R12_0_0_x64_centos65_ifort160_avx2_intelmpi-2018_sharelib I=/home/femminer/NISSAN_ROGUE_INPUT/combine.key NCPU=1 MEMORY=2G MEMORY2=2G
```

The runscript is copied here

```
/home/ndv/data/Nissan_Rogue_2020_CCSA_public/runscript
```

---

# Dev tree setup

- directory
  `/home/ndv/stud/data/NISSAN/full_front`

- leo1 dir, perrsonal path for computing. allresults are transfered to former path
  `/home/Projects/carGraph/runs/NISSAN/full_front`

- post sessions
  `kg01/ses/front_status_values.ses`

---

### Todo

- [ ] load curves to the CAEWebVis

---

### Detail Setups

The initial simulations. Since this is the open model I thought it will be better to have the data also accessible to students. so you can find them here,

```
/home/ndv/stud/data/NISSAN/full_front
```

there is also a ppt that visualizes the changes, [link](model_changes.pptx). the run script changes a bit to extend the run time and match the change of input key file, [link](dynarun.sh). run the simulation on 10 nods, running time of less than 1 hr.

Each NISSAN_ff_00\*.key file has an XML header that also describes the change as a comment and parent of the simulations. I tried to follow the workflow we have for CAEWebVis so Raj can also read these to the database later on.

In each directory, I have only the NISSAN_ff_00*.key file, NISSAN_ff_00*.key and the rest are in a top dir, `../model`. So if you want to re-run the simulations, please also include this dir in the file structure.

I also set the session script to output the sensor's values. To run the script you can use the python script that is in the root `oems.py`

```
source /home/compeng/config/env_beta_cae19.1.sh
vglrun -d /dev/dri/card1 meta_post64.sh -b -s oems.py
```

`oems.py` include all the oems pre-post setups, but you just need some part of it for this. meta doesn't work with importing a python package and then using meta-command. that is why you should uncomment the following,

```
oem = oems('NISSAN')
oem.set_data_path()
oem.metapost()
```


- part list in ansa, 2000097-2000100,2000621,2000656-2000657,2000667,2000669-2000670,2000730,2000808-2000810,2000822,2000824,2000838-2000839,2000841,2000845-2000849,2000869-2000874,2000877-2000878,2000897,2000915,2000923,2000929,2000932,2000934-2000935,2000937-2000938,2000941-2000942,2000951-2000954,2000961 

