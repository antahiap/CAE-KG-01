Neo4j GDS
----------------------------------------------------------------------------
### Setup the Server
1. Download Neo4j Community Edition (Server Version) for Linux :[link](
https://go.neo4j.com/download-thanks.html?edition=community&release=3.5.13&flavour=unix&_ga=2.237343104.1052135394.1574938173-111304196.1557840539)

(Anahita could use the Desktop version as well, but I used only the Neo4j browser version till now).

2. Unzip the downloaded .tar file into a folder called neo4j-community-3.5.13

3. Start the Neo4j server on localhost:7474 (default) using the following command on the Terminal (replace <some path> with wherever the .tar has been unzipped):
<some path>/neo4j-community-3.5.13/bin/neo4j console

4. Open http://localhost:7474/browser/

5. When prompted, enter the default Neo4j username and password:
Username: neo4j
Password: neo4j

7. This will further prompt you to choose a new username and password. You can choose any of your choice. This should open the Neo4j UI on your browser.

----------------------------------------------------------------------------------------------
### Kill the Port
- netstat -tulpn | grep LISTEN
- lsof -i:7687

![kill_pid](uploads/e3ea524239542299cc053b6a553db19c/kill_pid.png)

- kill -9 26716
