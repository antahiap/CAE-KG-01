
import os
import networkx as nx
import numpy as np
from neo4j import GraphDatabase
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def neo4jReturn(cypherTxt):

    results = driver.session().run(cypherTxt)
    nodes = list(results.graph()._nodes.values())
    rels = list(results.graph()._relationships.values())

    return (nodes, rels)


def get_digraph(txt, nameKey='model_name'):
    nodes, rels = neo4jReturn(txt)
    G = nx.DiGraph()

    for node in nodes:
        propN = node._properties
        label, = node._labels
        name = propN[nameKey].split('_')[-1]

        G.add_node(node.id, properties=propN, label=label, name=name)

    for rel in rels:
        G.add_edge(
            rel.start_node.id,
            rel.end_node.id,
            color='k',
            key=rel.id, type=rel.type, properties=rel._properties)

    start_index = 0
    G = nx.convert_node_labels_to_integers(G, first_label=start_index)

    return(G)


if __name__ == '__main__':
    driver = GraphDatabase.driver(
        uri="bolt://localhost:7687", auth=("neo4j", "ivory123"))
    # uri="bolt://berkeley:7687", auth=("neo4j", "NEO4J"))

    cypherTxt = """
        //html page 
        match (m:Model)-[r:MODEL_REF]-(n:Model)
        where m.model_name=~'.*pp46.*' 
        return m,n, r
        """
# ------------------------------------------------
    # G = get_digraph(cypherTxt)

    dPath = '/home/apakiman/leo1/Projects/carGraph/runs/YARIS/full_front/TL2PID_12/'
    simsTree = os.path.join(dPath,  "sims.txt")
    G = nx.read_gpickle(simsTree)
    pr = nx.pagerank(G, alpha=0.8)
    pr_size = [v * 90e3 for v in pr.values()]
    print(G.nodes.data())
    names = dict(G.nodes.data('name'))

    print(pr_size)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, node_size=pr_size, with_labels=True)
    # nx.draw(G, pos, node_size=pr_size, with_labels=True, labels=names)
    plt.show()
