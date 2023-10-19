unit system: ist noch im "alten" Einheitensystem
kg , mm , ms

### Setup
- look in mma platform
- one load case, 

| Loadcase | run number | max time|
| ------ | ------ |------|
| fmb | 4  | |
| **fo5** | 22 | 139,9|
| fo8 | 7 -| |
| **fod** | 15 - | 79,9|
| **fp3** | 36 | 79,9|
| fp5 | 1  | |
| fpp | 20 | |
| fpq | 12 | |
| fodo | 4 | |
| for | 1| |
- there are parts with negative energy, changed `energy_feature()` to consider abs of binout curve to evaluate tn (Max, Pct)
- consider abs in calculating max of energy
- add range for excluding the barrier
- read all fp3 (41 simulation), with 20 parts
- dump the database to be transfered
- [ ] read heade files

### vcc Setup
- path: `/cevt/cae/backup/safety/users/anahita.pakiman1`
- Java for neo4j , `export JAVA_HOME=/usr/lib64/jvm/jre-11-openjdk`

#### Installation
- couldn't install v4
- [ ] wait for reply
- [ ] editor - vscode, atom, tried under `/cevt/homes/anahita.pakiman1/Downloads/usr/share/applications`
- [ ] rerun all mma stages to the database




### How to
- connect to [cevt portal](portal.cevt.se)
- map drives `S:\`, `U:\`, use the *.bat in `C:\Users\anahita.pakiman1`
- on win use neo4j-3.5.26, in `U:\`
- kg01 in `U:\`
- activate virtual environment on win, `envs\Scripts\activate`
```
cd /share/nobackup/safety/projects/mma/3_stv0/front/runs
cp -r * ~/kg01/src/CEVT

find . -name 'binout*' -exec cp --parents \{\} /home/anahitapakiman/kg01/src/CEVT01/  \;

cd  ~/kg01/src/CEVT



for i in *; do cd $i; ~/clean.sh; cd .. ; done
for i in *; do cd $i; ll; cd .. ; done
find . -type f ! -name 'binout*' -delete

cd ..
tar -czvf cevt.tar.gz CEVT_out/
```

#### Transfer database
- move `/data/database/graph.db` to owncloud, (no permition to dump database to *.dmp)
- load database to a dumpy neo4j-3.5.26 on SCAI machine
- dump the database 
- activate `dbms.allow_upgrade=true` on neo4j 4.2
- load the database 
```
./neo4j-admin load --from /home/apakiman/kg01/NEO4J_KG/cevt_fp3_41_p_20_neo4_3.5.26.dump --database=neo4j --force
./neo4j-admin dump --database=neo4j --to=/home/apakiman/kg01/NEO4J_KG/cevt_fp3_41_p_20_neo4_4..2.3.dump
./neo4j-admin dump --database=graph.db --to=/home/apakiman/kg01/NEO4J_KG/cevt_fp3_53_p_20_neo4_3.5.26.dump

```

- run `connect_part_pid.py` to add extra connection based on extracted data
- add extra lables for nrg_evts


[more info](./database.md) for load/dump 

### Data Explore on fp3
- no simillar tn_max between parts
- for shared t0,tn get range of max_nrg
- [ ] use jupiter to plot over data, https://medium.com/@technologydata25/connect-neo4j-to-jupyter-notebook-c178f716d6d5
- [ ] add check for normal termination
- [ ] compare old data degree sort to the new one
- [ ] write test for database


### Fill Part information

### Visualize Analysis
- get part list from neo4j
- define the session to save picture
- write code in python to loop the session for fp3
- define visualizatin link 
    - python overlay two images

- on gridcore
```
module load metapost
cd ~/kg01/src/cevt_vis/script/fp3
meta_post64.sh -b -s frontPost_lin.py
cd picDir
~/kg01/src/cevt_vis/post/aviMp4
```
on windows
```
cd U:\kg01\src\cevt_vis\post
python html_gr.py
```

### cx11 data summary
- cx11/ cx11_eu with binout:
total = 106

11_pp1:16
7_v21:90

fmb:92
fo9:2
fp5:3
fo5:3
fpq:1
fps:5

- cx11/ cx11_eu with  key:
total = 2381

11_pp1:401
9_vp2:1378
7_v21:602

fac:4
fmb:411
fo8r:2
fo8:418
fo9:77
fod:11
forr:14
for:477
fp3:100
fp5:132
fpq:209
fps:180
mpdb:13
fab:27
fo5:271
fo5r:4
fo7:1
fo85:3
fodo:9
fpi:2
fpq16:15
fpq25:1

### [Energy Embedding ](./CEVT/energy_embd.md)

### [Graph Algorithems](./CEVT/graph_alg.md)

### Read Parts Geometric Features

