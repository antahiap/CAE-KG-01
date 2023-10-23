# [Nodes 2020](https://neo4j.com/video/nodes-2020/?mkt_tok=eyJpIjoiTVRRNU9HVXpNamxqTm1SbSIsInQiOiJTbzZ0XC9YT2QzYlVTSTRnY3U1OTgzeG5QZzQ2UmJsdWxZTW0yREJUaFdGdlY2S0RiNVVBZlg4RUozSTNDb3VqREFGXC9kUEN4ZGttbU1id2ZiR2o4RWxjOGlna3JEeEF1bFlKMGRRSXJIVTlIZlBkekpxbGhQRmhSYTZsZ1wvSktvKyJ9)

- NEO4j aura
- GDSL
- Neo4j bloom is free
- GQL, make graph industry normal
- Hume, Graph-Powered Insights Engine
- APOC procedures

---
### Knowledge Graph
#### KG powered by NLP, [link](https://www.slideshare.net/secret/r9Y4Mv2tZ3P6eU)
-  stanford coreNLP > pageRank, keyword extraction (textRank)
- named entity recognition(NER), classification of the words to known classes
- entity relations extraction > build entity relation modesl (LSTMs, CNNs, **GCNs**, Language Models) > integrate it KG
- GCNs, [article](https://arxiv.org/abs/1906.07510) > unsupervised ML > use NER to extract relations
- topic modeling (LSA/LDA,  SVM, CNNs/RNNs), sth faster: graphed-based topic modeling > combine keyword and community detection > extract keyword > create weighted co-occurrence graph > leverage a community detection alg to identify clusters (Louvain algorithm)
- **book**, Graph Powered Machine Learning Alessandro Negro

#### KG powered by NLP, [link](https://www.slideshare.net/secret/1rQX23DZKWPrGF)
- tbgraph.wordpress.com
- [Network of Thrones](https://networkofthrones.wordpress.com/) > creat interact if 15 words between entities > count interaction between pair of character and store the normalized value as a relationship weight
- Graph enrichment, co-occurrence graph, wikidata, conceptNet, commercial APIs
- practical applications, recommendations, curated news feed, [link prediction](https://www.researchgate.net/publication/265095736_Link_Prediction_in_a_MeSH_Co-occurrence_Network_Preliminary_Results), hypothesis generation. feature generation(node embedding), 

#### Qknows knowledge graph, (**BASF. Janez Ales**)
- 5 bi nodes, 50 bio rel > add pairwise relation > memory challenge in the past
- enterprise version 
- using apoc.periodic.iteraite (1 Tb neostore)
- **meta/fuzzy node**, **meta/fuzzy relation**, **ontology concept** (for simillarity evaluatio), **rooted sub-graph** (for simillarity),

#### Representing & Managing consent for Data Sharing with KG (Innsburk Anelia Kurteva, sensor data, GPDR)
- platform, CampaNeo
- KG benefits, can reuse ontologies for events, time, timestamp data

#### A Survey as a Graph, (Klaus Blass)
- survey solutions, free
- considering time
- java loader
- ** never through away survey data**
- save multi-option questions as a sting and query it with search string 
- ordered multiple-answers, three properties, toilet1, toilet2, toilet3
- longitudinal data, ex pregnancy, use multiple labels (MATCH (m:member)--(p:pregnancy), MATCH (m:member)--(p:pregnancy:round1))
- Migration time, node or relationship > relationship with property

#### Using Software Agents for Querying KG, (Siraj Munir, Ph.D. Pakistan )
- **semantic web tower**
- ** target queries **, list of questions to answer
- SNA (social network analysis), NLP, semantic web 

#### build a KG using NLP and Ontologies (Mark Needham- Borrasa, neo4j) **Good DEMO for EuNCAP**
- explicit knowledge (ontology) + facts (structure data, xml)
- football knowledge graph: football taxonomies Wikidata SPARQL API, n10s> sport articles > entity extraction, GCP NLP APIs > OWL, enrich entity
- KG for: semantic search, item similarity, inference, detect inconsistencies
- tools: Wikidata SPARQL API, neosemantics(n10s), APOC (NLP GCP)
- :play nlp_knowledge_graphs_nodes2020
- apoc.load.xml
- remove redundant structure, remove multi-connection
- add custom ontology

#### Dev KG for your knowledge, abilities, tasks, training(LSATT), (David Meza, NASA **domain-specific search engine**)
- understand domain > ask question > define model > do the analysis
- tools uses: neo4j(Jaccard similarity, GNN) python(doc2vec, entity extraction, BERT, RNN, Spacy)
- available data: ONET-SOC, OPM(handbook of occupancy), ESCO(European skills, competencies, qualification and occupations) 
- neo4j, gds.nodesimilarity.stream
- **DASH**, plotly

#### Mastering Enterprise Metadata with Neo4j (Vladimir Bacvanski, Deepak Chandramouli PayPal)[video](https://youtu.be/8flUr0J9rkU), [](https://www.slideshare.net/secret/mLLjOy8zoIYuoT)
- unified data control
<img src="uploads/4073018548383f6f31b3523dcab9f9c6/image.png" width="50%">

- demo sandbox on [github](https://github.com/Dee-Pac/GEM), [gitter](https://gitter.im/graph_of_enterprise_metadata/GEM-Ask-Us-Anything)
- **graphQL**
- different sys of data challenge

<img src="uploads/1e5b59c3188b8d2a3199d6a153b714b3/image.png" width="30%">
<img src="uploads/3bc81a351122050fa0cc3a2786fcb771/image.png" width="30%">
<img src="uploads/1480827602e005016d43527f1d0e3770/image.png" width="30%">

#### Project Domino: COVID19  with sitizen size data, Graphs4good (Sean Griffin - Disaster Tech, Leo Meyerovich - **Graphistry**, **RAPIDS.ai**)
- **NLP**
- infodemic, encourage good decrease bad
- 10TB server w index neo4j, Twitter API scraper, run parallel **PREFECT**
- jupyter -> graphistry

#### 33. Extending a Knowledge Graph from Wikidata

----
### GDS Lib
#### 50. From Local Strategies to Global Patterns, Nathan Smith
- reading Graph theory > Drawing > coding
- power laws: graph theory preferential attachment
books
- [Networks, Crowds, and Markets](https://www.cs.cornell.edu/home/kleinber/networks-book/)
- [Hands-On Graph Analytics with Neo4j](https://www.packtpub.com/product/hands-on-graph-analytics-with-neo4j/9781839212611)
- [codes](https://github.com/smithna/NODES2020)
- [source list](https://neo4j.com/blog/top-13-resources-graph-theory-algorithms/)

#### Leveraging Dimensionality for Graph-Based Recommendations with Sparse Data, Will Evans- Graphable
- spars: P > N (number of parameters vs number of samples)
- Schema Design, the product is in the center (beer)> ask questions to add other entities
- avoid complexity if it is not needed
- consider the business aspect, how it has affected the customer
- pattern of scoring vs average of scoring for similarity
-  use expert knowledge to leverage the recommendation, then using just the most reviewed product, not relying on crowd
- used home for visualization

#### Graph Native learning, Introducing GraphSAGE & ML Model Catalog in Neo4j
- why you use graph, relationships are predictive, make prediction you can't without relationship
- Graph embedding, convert each node to some digits to maintain its key features,
how far away is this node in the graph, how similar are the nodes how important is this node, in lower dimension (path embedding, edge embedding, graph embedding, but in neo4j just node embedding)

**graph embedding in neo4j**
- FastRP. similarity matrix to lower dimensionality math, fast
- Node2Vec, random walk-sampling, easy to understand
both output same length vector, need to rerun if you add new data
- GraphSAGE.

**GraphSAGE**, SAmpling and AggreGate
- assume: nodes in the neighborhood should have a similar representation
- use node property beside relationships, if not much property is on the node,
output will be as two other method
- random walk to Sample > AggreGate (mean, pool)> Predict, learn a function to predict (instead of learn the parameters), predict the node around it
- if you add new data, you don't need to re-train the model
- complex algorithm, slow but no need to retrain it
- used for: prediction, classification, visualization

#### 49. Doom, Kafka and Neo4j- Building a (Near) Real-Time Telemetry Graph, Dave Voutila, [slides](https://www.slideshare.net/secret/BeI0z2YkkTmB52), [videos](https://youtu.be/nBbXPakhg-I)
- cause and effect relations
- time matters in the data
- Event, PREV_EVENT give the history 
- windowing vs filtering
- NEO4j driver 4.1, Reactor-Netty, SDL_Net
* continue ... 


#### 53. From RDBMS to Neo4j: Tips and tricks, Mike Blum-Logic gate
- Python: Sqlalchemy, PyYAML
- [more info](https://neo4j.com/developer/guide-importing-data-and-etl/)
----
### Use cases
#### Automotive use case
- Uve Klosa (RLE), Elena Kohwey
- better to use a combination of process development of the company and knowledge graph

---
### Seminars
- KGC
- Data Science Salon
- nyhackr.org
- Neo4j ninja
- R-Ladies Miami
- Data for science
- NumFOCUS