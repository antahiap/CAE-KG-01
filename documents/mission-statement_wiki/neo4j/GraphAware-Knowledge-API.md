 It integrates NLP processing capabilities available in several software packages like Stanford NLP and OpenNLP, existing data sources, such as [ConceptNet](http://conceptnet.io/) 5 and [WordNet](WordNet), and GraphAware knowledge about search, graphs, and recommendation engines.
    
The available interesting features are:
* Information Extraction (IE) - processing textual information for extracting main components and relationships
* Extracting sentiment
* Enriching basic data with ontologies and concepts (ConceptNet 5)
* Computing similarities between text elements in a corpus using base data and ontology information
* Enriching knowledge using external sources (Alchemy)
* Providing basic search capabilities
* Providing complex search capabilities leveraging enriched knowledge such as ontology, sentiment, and similarity
* Providing recommendations based on a combination of content/ontology-based recommendations, social tags, and collaborative filtering
* Unsupervised corpus clustering using LDA
* Semi-supervised corpus clustering using Label Propagation
* Word2Vec computation and importing

----------------------------------------------------------------------------------------
### NLP- Neo4j
 - [Accelerating Towards Natural Language Search with Graphs](https://neo4j.com/blog/accelerating-towards-natural-language-search-graphs/)
 - [Python NLTK/Neo4j: Analysing the Transcripts of How I Met Your Mothe](https://dzone.com/articles/python-nltkneo4j-analysing)
 - [NLP with With Neo4j - Mining Paradigmatic Word Associations](https://www.lyonwj.com/2015/06/16/nlp-with-neo4j/)

### Keywording
 - [ Unsupervised Keyword Extraction](https://graphaware.com/neo4j/2017/10/03/efficient-unsupervised-topic-extraction-nlp-neo4j.html)

### GraphAware
 - [more](https://graphaware.com/blog/nlp/)
----------------------------------------------------------------------------------------
```
- CALL ga.nlp.createSchema()
- CALL ga.nlp.config.setDefaultLanguage('de')
- CALL ga.nlp.processor.addPipeline({
name:"pipeline_name",
textProcessor: 'com.graphaware.nlp.processor.stanford.StanfordTextProcessor',
processingSteps: {tokenize:true, ner:true, dependencies:true, relations:true, open:true, sentiment:true}
})
 - CALL ga.nlp.processor.pipeline.default('annotateText')
 - CALL ga.nlp.processor.getPipeline()
 - CALL apoc.periodic.iterate(
'MATCH (n:Article) RETURN n',
'CALL ga.nlp.annotate({
        	text: n.Text,
        	id: id(n),
        	pipeline: "pipeline_name",
        	checkLanguage:false
})
YIELD result MERGE (n)-[:HAS_ANNOTATED_TEXT]->(result)',
{batchSize:1, iterateList:false})
```
-------------------------------------------------------------------------
```
CALL apoc.periodic.iterate(
  "MATCH (a:AnnotatedText) RETURN a",
  "CALL ga.nlp.ml.textRank({annotatedText: a}) YIELD result
   RETURN distinct 'done' ",
{batchSize:1,iterateList:true})
```
-------------------------------------------------------------------------
```
CALL dbms.procedures() YIELD name, signature, description
WHERE name =~ 'ga.nlp.*'
RETURN name, signature, description ORDER BY name asc;
```

