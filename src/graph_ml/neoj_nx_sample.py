import networkx as nx
from neo4j import GraphDatabase


def neo4jReturn(cypherTxt):

    results = driver.session().run(cypherTxt)
    nodes = list(results.graph()._nodes.values())
    rels = list(results.graph()._relationships.values())

    return (nodes, rels)


if __name__ == '__main__':
    driver = GraphDatabase.driver(
        uri="bolt://localhost:7687", auth=("neo4j", "ivory123"))

    txt = """
        //html page 
        match (p:Page)-[r]-()
        return p, r
        """

    nodes, rels = neo4jReturn(txt)
    G = nx.Graph()

    for node in nodes:
        propN = node._properties
        label, = node._labels
        
        G.add_node(node.id, properties=propN, label=label)
    for rel in rels:
        G.add_edge(
            rel.start_node.id,
            rel.end_node.id,
            color='k',
            key=rel.id, type=rel.type, properties=rel._properties)
            
    start_index = 0
    G = nx.convert_node_labels_to_integers(G, first_label=start_index)
