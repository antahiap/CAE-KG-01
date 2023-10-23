I have added a text file with some info (/export/codes/cargraphs/running-cargraphs.txt). You may first run the neo4j for the present data that is already in the /export (we used for testing). Then clear the database. Then may be you can use the needed simulations. (The simulations are needed to be in a4db file format, only geometry is needed)

### First test


**Start neo4j server**
/export/tools/neo4j/neo4j-community-3.5.8/bin/neo4j console


**Open browser**
firefox http://localhost:7474/

**Login**
 - username - neo4j
 - pass - Neo4j


This file has the needed info (about where are the a4db files, where are the modelcompare results, modelcompare exe path etc ...)
 - /export/codes/cargraphs/thakur-master-2019-11-15/build2/config.txt

**Run cargraphs**

cd /export/codes/cargraphs/thakur-master-2019-11-15/build2
./cargraphs



The modelcompare results will be loaded into the neo4j. (will take some minutes)

Checkout the file "running-cargraphs.txt" for info about the storage structure needed by cargraphs.