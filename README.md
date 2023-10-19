### Inductive Knowledge Graph

Data samples:

- PAG Data
- YARIS model
- VW Data
- VENZA model

### Depndencies
Code is developed for `pytho=3.6.8`.

```
python3 -m venv envs
source envs/bin/activate
pip install -r requirements.txt
cat requirements.txt | xargs -n 1 pip install

pip freeze > requirements.txt
pipreqs --encoding=iso-8859-5 ./

```

#### Django Server

```
python manage.py runserver
python manage.py shell_plus --notebook
```

#### Jupyter for Atom

```
pip3 install jupyter jupyter_kernel_gateway
apm install jupyter-notebook
python manage.py shell_plus --notebook
```

#### Set Database

- download neo4j and load .dmp file form `./NEO4J_KG`, [more info](./documents/database.md)
- configuration, `NEO4J_KG/conf/neo4j.conf-neo4j-community-4.2.1 ../neo4j-community-4.2.1/conf/neo4j.conf`
- plugins

#### LASSO

- Issue in 1.5.1 release, working version `lasso-python==1.5.0.post3`

#### oems

To set different OEM data setup import `oems.py `class and call the panda data frame based on required data sampling, (the database should be runing, can edit the access in `oems.py`)

```
import sys
import os
import plotly.express as px

sys.path.append(os.path.abspath('..'))
import oems

if __name__ == '__main__':

    global OEM
# YARIS
    OEM = 'YARIS'

    oem = oems.oems(OEM)
    c_grp = 'c_grPID'
    ords = 10
    ns = 100
    nPid = 10
    sims = '.*'
    pids = ''

    df = oem.cypher().out_dataframe(
        ns=int(ns), nPID=int(nPid), nOrd=ords, regs=sims, regp=pids)

    print(df)

    df = oem.cypher().cnv_usys(df)
    df = df.sort_values(by=[c_grp])
    fig1 = px.scatter_3d(
        df, x="ti", y="tn", z="IE", color=c_grp, custom_data=["pic"],
        hover_name="PID")  # , template="plotly_white")
    fig1.show()


```
