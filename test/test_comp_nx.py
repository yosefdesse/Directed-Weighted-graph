import networkx as nx
import time

from src.GraphAlgo import GraphAlgo





def check1():
    ga = GraphAlgo()
    file = '../data/G_10_80_1.json'
    ga.load_from_json(file)
    ga_nx = nx.Graph()
    for i in ga.get_graph().get_all_v().keys():
        ga_nx.add_node(i)
    for k, v in ga.get_graph().get_all_v().items():
        for node_id, w in ga.get_graph().all_out_edges_of_node(k).items():
            ga_nx.add_edge(k, node_id, weight=w)
    start1 = time.time()
    nx.shortest_path(ga_nx, 0, 5)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    nx.node_connected_component(ga_nx, 9)
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    nx.connected_components(ga_nx)
    end3 = time.time()
    print(end3 - start3)


def check2():
    ga = GraphAlgo()
    file = '../data/G_100_800_1.json'
    ga.load_from_json(file)
    ga_nx = nx.Graph()
    for i in ga.get_graph().get_all_v().keys():
        ga_nx.add_node(i)
    for k, v in ga.get_graph().get_all_v().items():
        for node_id, w in ga.get_graph().all_out_edges_of_node(k).items():
            ga_nx.add_edge(k, node_id, weight=w)
    start1 = time.time()
    nx.shortest_path(ga_nx, 0, 45)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    nx.node_connected_component(ga_nx, 34)
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    nx.connected_components(ga_nx)
    end3 = time.time()
    print(end3 - start3)


def check3():
    ga = GraphAlgo()
    file = '../data/G_1000_8000_1.json'
    ga.load_from_json(file)
    ga_nx = nx.Graph()
    for i in ga.get_graph().get_all_v().keys():
        ga_nx.add_node(i)
    for k, v in ga.get_graph().get_all_v().items():
        for node_id, w in ga.get_graph().all_out_edges_of_node(k).items():
            ga_nx.add_edge(k, node_id, weight=w)
    start1 = time.time()
    nx.shortest_path(ga_nx, 3, 450)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    nx.node_connected_component(ga_nx, 900)
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    nx.connected_components(ga_nx)
    end3 = time.time()
    print(end3 - start3)


def check4():
    ga = GraphAlgo()
    file = '../data/G_10000_80000_1.json'
    ga.load_from_json(file)
    ga_nx = nx.Graph()
    for i in ga.get_graph().get_all_v().keys():
        ga_nx.add_node(i)
    for k, v in ga.get_graph().get_all_v().items():
        for node_id, w in ga.get_graph().all_out_edges_of_node(k).items():
            ga_nx.add_edge(k, node_id, weight=w)
    start1 = time.time()
    nx.shortest_path(ga_nx, 3324, 3333)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    nx.node_connected_component(ga_nx, 5000)
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    nx.connected_components(ga_nx)
    end3 = time.time()
    print(end3 - start3)


def check5():
    ga = GraphAlgo()
    file = '../data/G_20000_160000_1.json'
    ga.load_from_json(file)
    ga_nx = nx.Graph()
    for i in ga.get_graph().get_all_v().keys():
        ga_nx.add_node(i)
    for k, v in ga.get_graph().get_all_v().items():
        for node_id, w in ga.get_graph().all_out_edges_of_node(k).items():
            ga_nx.add_edge(k, node_id, weight=w)
    start1 = time.time()
    path = nx.shortest_path(ga_nx, 25, 300)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    nx.node_connected_component(ga_nx, 900)
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    nx.connected_components(ga_nx)
    end3 = time.time()
    print(end3 - start3)


def check6():
    ga = GraphAlgo()
    file = '../data/G_30000_240000_1.json'
    ga.load_from_json(file)
    ga_nx = nx.Graph()
    for i in ga.get_graph().get_all_v().keys():
        ga_nx.add_node(i)
    for k, v in ga.get_graph().get_all_v().items():
        for node_id, w in ga.get_graph().all_out_edges_of_node(k).items():
            ga_nx.add_edge(k, node_id, weight=w)
    start1 = time.time()
    path = nx.shortest_path(ga_nx, 9, 25000)
    end1 = time.time()
    print(end1 - start1)
    start2 = time.time()
    nx.node_connected_component(ga_nx, 20000)
    end2 = time.time()
    print(end2 - start2)
    start3 = time.time()
    nx.connected_components(ga_nx)
    end3 = time.time()
    print(end3 - start3)


if __name__ == '__main__':
    check1()
    check2()
    check3()
    check4()
    check5()
    check6()