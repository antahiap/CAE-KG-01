### Select Database for Knowledge graph
| Neo4j| OrientDB|
| ------ | ------ |
| some experience| bio support|
| Graphware applications | multi databases|
| bigg community | |


# Neo4j databse
## neo4j 3.5.13
- local server on ivory: /export/work/neo4j/NEO4j_kg
- run server: /export/work/neo4j/NEO4J_KG/bin/neo4j console

## neo4j 4.1.3
- local server on ivory: /export/work/neo4j/neo4j-community-4.1.3
- run server: /export/work/neo4j/neo4j-community-4.1.3/bin/neo4j console

### Java specification for 4.0
- check java comiler `javac -version`
- [requirements](https://neo4j.com/docs/operations-manual/current/installation/requirements/?_gl=1*1a2albm*_ga*MTc4MTE2MDMwOS4xNjIxOTI5NDAy*_ga_DL38Q8KGQC*MTYyMzI1MDAyNS42LjEuMTYyMzI1MDExNS4w&_ga=2.148265143.1456111907.1623250025-1781160309.1621929402)

------

Neomodel works for neo4j 3.0, current workflow:
 - neomodel load data on neoj 3.5.13
 - transfer the databse to neo4j 4.1.3
 - activate `dbms.allow_upgrade=true`
 - start the server

**Update**, with update of neoj driver (pip install neo4j), neomodel also works for neo4j 4.1

----
## Workflow neo3.0 and 4.1
- with virtual env
- django framework
- neomodel 
- neo4j python driver

- check available javas, `update-alternatives --config java`
- change local PATH, `export PATH=/usr/lib/jvm/java-11-openjdk-11.0.11.0.9-1.el7_9.x86_64/bin:$PATH`
- for CEVT, `export JAVA_HOME=/usr/lib64/jvm/jre-11-openjdk`

----
## Load and dump databases
neo4j.3 doesn't need use of dump, can simply transfer `graph.db` from `$NEO4j_home/data/database`
- Dump:
`/export/work/neo4j/neo4j-community-4.1.3/bin/neo4j-admin dump --database=graph.db --to=/home/apakiman/neo4j/test.dump`

- Loop `for i in $PWD/*neo4j-community-4.2.4*; do j=$(basename "$i"); echo $i; echo $j; $i/bin/neo4j-admin dump --database=neo4j --to=neo4j-community-4.2.4/$j.dump; done`

- Load
`bin/neo4j-admin load --from=../data/dumps/test.dump --database=neo4j --force`
 - activate `dbms.allow_upgrade=true`

- on Neo4j desktop, manage database>open terminal>`cd bin`>...

- [more info](https://neo4j.com/docs/operations-manual/current/tools/dump-load/?_gl=1*gioyb7*_ga*MTQwNTA3NDUwMS4xNjAzMTkwMzQy*_ga_DL38Q8KGQC*MTYwNTg4NDQ0Ny4xOS4xLjE2MDU4ODQ2NTUuMA..&_ga=2.21966395.1248871291.1605875788-1405074501.1603190342&_gac=1.195627486.1604062303.CjwKCAjw8-78BRA0EiwAFUw8LPwaXfCGpnzlAzU4hsaI9W_HeSNbJk57ybPZMdxt_N_PUqUKxUZAdhoCIEgQAvD_BwE)

## Linux installation
- run with `sudo neo4j start`
- installation under `/usr/bin/neo4j` I manged to 
- add the plugins (apoc and gds) by just adding the jar file to `/var/lib/neo4j/plugins`, the only trick is using sudo, apoc vailable on lib, gds [download](https://neo4j.com/download-center/#community)

- moving the APOC jar file from the $NEO4J_HOME/labs directory to the $NEO4J_HOME/plugins directory and restarting Neo4j.

after that restart your server, and check the installation with `return apoc.version()`, `return gds.version()`

## Issues
- not killed server on linux local installation `systemctl {start|stop|restart} neo4j` should be on root `sudo -i`
- get runing servers `sudo lsof -i -P -n | grep LISTEN1`
- neo4j 4+, cant start local installation, `WARNING: sun.reflect.Reflection.getCallerClass is not supported. This will impact performance.`
posted issue on neo4j,[link](https://community.neo4j.com/t/the-port-is-free-but-server-doesnt-start/30311),

On Ivory machine Andre addresses, `Caused by: java.io.IOException: User limit of inotify watches reached`, For that, we need to raise the inotify limit. I've increased it to 524288 now, it was 8192 before.

check the inotify limit: `cat /proc/sys/fs/inotify/max_user_watches`, [more info](https://unix.stackexchange.com/questions/13751/kernel-inotify-watch-limit-reached)

## [NeoDash](https://github.com/nielsdejong/neodash)
available on `/export/work/neo4j/neodash`, start command
```
cd neodash
npm start
```



