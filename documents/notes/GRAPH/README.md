## Contenent
 - [Graph Model](GRAPH/graph_model.md)
 - [Graph Embedding](GRAPH/graph_embd.md)
    - [subGNN](GRAPH/subGNN.md)
 - [GDS (Graph Data Sceinece Library- NEO4J)](GRAPH/gds.md)
    - [GDS Algorithems](GRAPH/gds_alg_lib.md)
 - [DGL (Deep Graph Library)](GRAPH/dgl_lib.md)
-------------------------------------------------------------------
### Energy Graph Method

A simple undirected weighted network to connect simillar sim-sim


#### Graph Embedding
- Graph embedding, fail, compares two seprate graph and in energy graph, graph interconnection matter
- SubGNN, sounds a good idea with local and global feature, but code is not stable, hard to use torch-lightning to debug


**New Perspective**: 2 layer neural Network interpretation
#### Hasso-Plattner-Institut
##### course
- [electures](https://hpi.de/studium/im-studium/lehrveranstaltungen/e-lectures-tele-task.html)
- [Knowledge Graph](https://open.hpi.de/courses/knowledgegraphs2020), Knowledge Graph Applications
- [Semantic Web Technologies](https://open.hpi.de/courses/semanticweb)
- [Graph Exploration (ST 2017)](https://www.tele-task.de/series/1162/)
##### Graph Mining
- [HPI](https://hpi.de/mueller/lehre/aktuelle-vorlesung/ws-1617/graph-mining.html)
- [EECS](http://web.eecs.umich.edu/~dkoutra/tut/icdm14.html)
  - [SimRank for Bipartite Graphs](url)


###### [Introduction](https://hpi.de/fileadmin/user_upload/fachgebiete/mueller/courses/graphmining/GraphMining-01-Introduction.pdf)
 
It should be a dynamic graph, but for now cosider it static
- if all parts are the same, the graph is isomorphism

###### [Link Prediction](https://hpi.de/fileadmin/user_upload/fachgebiete/mueller/courses/graphmining/2017/05-LinkPrediction.pdf)
supervised Method 
-  Neighborhood-based, The	larger	the	overlap	of	the	neighbors	of	two	nodes,	the	more	likely	the	nodes	to	
be	linked	in	the	future. 

ideas:
- Influence propagation
- Link Prediction
  - unsupervised, Neighborhood based, link prediction on specific nodes
- Graph evolution
- Detecting frauds


#### To Do 
- [ ] Go through HPI material
- [ ] Imolement simple matrix
- [ ] look in the big Knowledge graph book
- [ ] [Networkx new algorithems](https://networkx.org/documentation/latest/auto_examples/index.html)

-------------------------------------------------------------------
### Shramana Inputs 
[link1]( https://arxiv.org/pdf/1709.05584.pdf),[link2](http://snap.stanford.edu/proj/embeddings-www/), These two are very informative links on node embeddings that I got from Dr.Fröhlich

[This](http://ceur-ws.org/Vol-2100/paper26.pdf) Property graph models

- Python package to use
    - [pypi-graphembedding](https://pypi.org/project/graphembedding/)
    - [karateclub](https://github.com/benedekrozemberczki/karateclub), Shramana

Start with karateclub and [nxneo4j](https://github.com/ybaktir/networkx-neo4j/blob/master/examples/nxneo4j_tutorial_latest.ipynb)
- update package `pip install karateclub --upgrade`
    - Neighbourhood-Based Node Level Embedding/DeepWalk
    - change edges to be indirected

    - https://stackoverflow.com/questions/59289134/constructing-networkx-graph-from-neo4j-query-result

- How to read fully connected graph
  - Use GDS to make the graph, not returning nodes, relationships in result
  - Use apoc.path.subgraph to get based on connectivity, didn't work
  - try to check connectivity with networkx
    - [Algorithms](https://networkx.org/documentation/stable/reference/algorithms/approximation.html#module-networkx.algorithms.approximation.connectivity)
  - try to develop the cypher query

- visualize graph based on lable color
- graph embedding
- [ ] sort graph - layer graph

depend completely on whether the subgraph is heterogeneous or homogeneous (only one type of nodes and connections), Dr.Frohlich:  look into Graph Neural Networks specifically from the DGL Python Package. 
There are two major packages in python for Graph Neural Nets - pytorch geometric and DGL (https://docs.dgl.ai/en/0.4.x/index.html)


shramana.thakur: needed algorithms for heterogeneous graph embeddings... so, graph neural nets

- [RGCN](https://paperswithcode.com/method/rgcn)


-------------------------------------

- [ ] add simulation connection
- [ ] embed fp3 based on status_parameter value
- [ ] look into dt instead of tn
- [ ] save intersting finding on neodash - find better viewing for graph
- [ ] consider termination time to exclude half run ex, fp3 57,95

<img src="./img/graph.svg" height="200px"/>[link](./img/graph.svg)


