#### Shortcuts
>  `CALL db.schema.visualization()`
------------------------------------------------------------------------
##### Visualizatin:
>  `MATCH (c:Person)-[:INTERACTS]->()`

##### Summary statistics:
> `MATCH (c:Person)-[r:INTERACTS]->()
WITH r.book as book, c, count(*) AS num
RETURN book, min(num) AS min, max(num) AS max, avg(num) AS avg_interactions, stdev(num) AS stdev
ORDER BY book`

##### Memory estimation:
>  `CALL gds.graph.create.estimate('Person', 'INTERACTS') YIELD nodeCount, relationshipCount, requiredMemory`

>  `CALL gds.graph.create('got-interactions', 'Person', 'INTERACTS')`

>  `CALL gds.pageRank.stream.estimate('got-interactions') YIELD requiredMemory`

>  `CALL gds.pageRank.stream.estimate({nodeProjection: 'Person', relationshipProjection: 'INTERACTS'})`

>  `  nodeProjection: 'Person',
  relationshipProjection: 'INTERACTS'
}) YIELD mapView
UNWIND [ x IN mapView.components | [x.name, x.memoryUsage] ] AS component
RETURN component[0] AS name, component[1] AS size`

>  `CALL gds.graph.drop('got-interactions')`

>  more specific call `CALL gds.graph.create.cypher(
  'got-interactions-cypher',
  'MATCH (n:Person) RETURN id(n) AS id',
  'MATCH (s:Person)-[i:INTERACTS]->(t:Person) RETURN id(s) AS source, id(t) AS target, i.weight AS weight',
  {
    relationshipProperties: {
      weight: {
        property: 'weight',
        aggregation: 'SINGLE'
    }
  }
})`
------------------------------------------------------------------------
##### Graph creation:
>  `CALL gds.graph.create('got-interactions', 'Person', {
  INTERACTS: {
    orientation: 'UNDIRECTED'
  }
})`
 - standard creation (`gds.graph.create()`) , order of magnitude faster
 - Cypher projection (`gds.graph.create.cypher()`), load specific nodes to the graph
>  `CALL gds.graph.create.cypher(
  'got-interactions-cypher',
  'MATCH (n:Person) RETURN id(n) AS id',
  'MATCH (s:Person)-[i:INTERACTS]->(t:Person) RETURN id(s) AS source, id(t) AS target, i.weight AS weight',
  {
    relationshipProperties: {
      weight: {
        property: 'weight',
        aggregation: 'SINGLE'
    }
  }
})`
>  `CALL gds.graph.list()`, `CALL gds.graph.list('got-interactions-cypher')`, `CALL gds.graph.exists('got-interactions')`
-------------------------------------------------------------------------------------
##### Algorithm syntax: explicit graphs:
>  `CALL gds.<algo-name>.<mode>(
  graphName: String,
  configuration: Map
)`

    <algo-name> is the algorithm name.
    <mode> is the algorithm execution mode. The supported modes are:
        write: writes results to the Neo4j database and returns a summary of the results.
        stats: same as write but does not write to the Neo4j database.
        stream: streams results back to the user.
    The graphName parameter value is the name of the graph from the graph catalog.
    The configuration parameter value is the algorithm-specific configuration.

##### Algorithm syntax: implicit graphs
>  `CALL gds.<algo-name>.<mode>(
  configuration: Map
)`
-------------------------------------------------------------------------------------
##### Page Rank:
>  `CALL gds.pageRank.stream('got-interactions') YIELD nodeId, score
RETURN gds.util.asNode(nodeId).name AS name, score
ORDER BY score DESC LIMIT 10`
>  write property: `CALL gds.pageRank.write('got-interactions', {writeProperty: 'pageRank'})`
-------------------------------------------------------------------------------------
##### Label Propagation (LPA):
>  `CALL gds.labelPropagation.stream(
  'got-interactions-weighted',
  {
    relationshipWeightProperty: 'weight',
    maxIterations: 1
  }
) YIELD nodeId, communityId
RETURN communityId, count(nodeId) AS size
ORDER BY size DESC
LIMIT 5`
>  `CALL gds.labelPropagation.write(
  'got-interactions-weighted',
  {
    relationshipWeightProperty: 'weight',
    maxIterations: 1,
    writeProperty: 'community'
  }
)`
>  `CALL gds.graph.create(
  'got-interactions-seeded',
  {
    Person: {
      properties: 'community'
    }
  },
  {
    INTERACTS: {
      orientation: 'UNDIRECTED',
      properties: 'weight'
    }
  }
)`
> `CALL gds.labelPropagation.stream(
  'got-interactions-seeded',
  {
    relationshipWeightProperty: 'weight',
    maxIterations: 1,
    seedProperty: 'community'
  }
) YIELD nodeId, communityId
RETURN communityId, count(nodeId) AS size
ORDER BY size DESC
LIMIT 5`
-------------------------------------------------------------------------------------
##### Weakly Connected Components
> `CALL gds.wcc.stream('got-interactions')
YIELD nodeId, componentId
RETURN componentId as component, count(nodeId) AS size
ORDER BY size DESC`