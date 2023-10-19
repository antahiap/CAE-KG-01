## Ontology

- neosemantic

  - config the neosemantic before loading the data
  - be carefule with toturial old command, [link](https://jbarrasa.com/2018/10/18/quickgraph7-creating-a-schema-org-linked-data-endpoint-on-neo4j-in/), find new version

  - latest command,

```
/home/apakiman/Projects/neo4j/ns10_GAE_neo4j-community-4.4.12/bin neo4j start
```

```
CALL n10s.graphconfig.init();
CREATE CONSTRAINT n10s_unique_uri ON (r:Resource)
ASSERT r.uri IS UNIQUE;

CALL n10s.onto.import.fetch("file:///home/apakiman/Projects/protege/GAE-vehicle-safety.rdf","RDF/XML");
CALL n10s.onto.import.fetch("file:///Y:\\Projects\\kg01\\publish_data\\GAE-vehicle-safety.rdf","RDF/XML");


```

```
CALL n10s.nsprefixes.add("sch","http://schema.org/");
CALL n10s.nsprefixes.add("dbo","https://dbpedia.org/ontology/");

CALL n10s.mapping.add("http://schema.org/Vehicle", "Veh");
CALL n10s.mapping.add("https://dbpedia.org/ontology/productionStartYear", "PUBL_IN")
```

- make ontology for classes missing

  - [x] publish current ontology to reach it via neo4j
    - https://stackoverflow.com/questions/46705136/how-to-make-an-ontology-public-accessible/47008727#47008727
    - https://jena.apache.org/documentation/fuseki2/fuseki-quick-start.html

- improve the ontology
  - [x] disconnected node
  - [x] relationships name
  - [x] benefits of ontology
  - [x] define entitites, mapping

### Linked Data

set the name spaces

```
CALL n10s.nsprefixes.add("akt","http://www.aktors.org/ontology/support#");
CALL n10s.nsprefixes.add("gae","http://www.semanticweb.org/GAE/#");
```

for get command need to set in config file

```
dbms.unmanaged_extension_classes=n10s.endpoint=/rdf
```

should see the `2023-04-12 16:28:58.414+0000 INFO  Mounted unmanaged extension [n10s.endpoint] at [/rdf]` when starting the server.

and then run

```
:GET /rdf/neo4j/onto?format=N-Triples

```

```
//:param uri: "http://www.semanticweb.org/GAE/#"
CALL n10s.mapping.add($uri + "AdultOccupantProtection","Aop");
CALL n10s.mapping.add($uri + "Attribute","Atr");
CALL n10s.mapping.add($uri + "Change","Chnage");
CALL n10s.mapping.add($uri + "Class","Class");
CALL n10s.mapping.add($uri + "CommonNodes","Common_Nodes");
CALL n10s.mapping.add($uri + "Connection","Connection");
CALL n10s.mapping.add($uri + "ChildOccupantProtection","Cop");
CALL n10s.mapping.add($uri + "Design","Des");
CALL n10s.mapping.add($uri + "Impactor","Imp");
CALL n10s.mapping.add($uri + "Model","Model");
CALL n10s.mapping.add($uri + "Platform","Pltf");
CALL n10s.mapping.add($uri + "Protocol","Prtcl");
CALL n10s.mapping.add($uri + "RigidBodyElement","RBE");
CALL n10s.mapping.add($uri + "ResultPage","Resultpage");
CALL n10s.mapping.add($uri + "SafetyAssist","Sas");
CALL n10s.mapping.add($uri + "Semantic","Semantic_Type");
CALL n10s.mapping.add($uri + "Simulation","Sim");
CALL n10s.mapping.add( "http://schema.org/Vehicle","Veh");
CALL n10s.mapping.add($uri + "VulnerableRoadUser","Vru");
CALL n10s.mapping.add("http://www.aktors.org/ontology/support#Year","Year");
```

- [ ] does it make sense to have relationship mapping

### Ontology Documentation

The output should be in xml/RDf.

cd /home/apakiman/Projects/pyLODE

moved to:
/var/www/caewebvis/cae_web_fe/build/GAE

182 git clone https://github.com/RDFLib/pyLODE.git
183 ll
184 cd pyLODE/
185 ll
186 python setup.py
187 cd pylode/
188 ll
189 python cli.py ~/Projects/GAE-vehicle-safety/ontology/GAE-vehicle-safety-v1.0.owl
190 pip install dominate
191 cd ..
192 python setup.py
193 ll
194 pip install -r requirements.txt
195 pip install pytest-cov=2.0
196 pip install pytest-cov
197 pip install pytest-filter-subpackage
198 python setup.py
199 pip install -r requirements.txt
200 python setup.py
201 ll
202 cd pylode/
203 ll
204 history
205 python cli.py ~/Projects/GAE-vehicle-safety/ontology/GAE-vehicle-safety-v1.0.owl

## Doocker container for django

- intro , [link](https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application)

### Build
-use [buildah]( https://github.com/containers/buildah/blob/main/docs/tutorials/01-intro.md#using-containerfilesdockerfiles-with-buildah)

```
buildah build -f Dockerfile -t gae:v0-django
```


### requirement

maintain requirements, [link](https://learnpython.com/blog/python-requirements-file/)

```
pip freeze > requirements.txt
pip list --outdated
pip install -U -r requirements.txt
```

check for dependencies

```
python -m pip check
```

### Podman

- it is with docker but runing it with podman. some cmmands:

```
podman images
podman run --rm localhost/antahia/gae
podman build -t latest .
podman rmi imageID
```

## SPHINX

## Django + Dash + Bootstrap
