import json
import queue
from random import random
from typing import List
import matplotlib.pyplot as plt

from src import GraphInterface
from src.DiGraph import DiGraph
import math
import heapq

from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = None):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        load_graph = DiGraph()
        try:
            with open(file_name, "r") as file:
                my_dict = json.load(file)
                nodes = my_dict["Nodes"]
                edges = my_dict["Edges"]
                for n in nodes:
                    node_key = n.get("id")
                    pos = n.get("pos")
                    if pos is None:
                        load_graph.add_node(node_key, None)
                        continue
                    if isinstance(pos, str):
                        x, y, z = pos.split(",")
                    else:
                        x, y, z = pos[0], pos[1], pos[2]
                    pos = (float(x), float(y), float(z))
                    load_graph.add_node(node_key, pos)
                for e in edges:
                    load_graph.add_edge(e.get("src"), e.get("dest"), e.get("w"))

        except IOError as e:
            print(e)
            return False

        self.graph = load_graph
        return True

    def save_to_json(self, file_name: str) -> bool:
        edges = []
        nodes = []
        try:
            with open(file_name, "w") as file:
                for n in self.graph.get_all_v().keys():
                    for d, w in self.graph.all_out_edges_of_node(n).items():
                        edge = {"src": n, "Weight": w, "dest": d}
                        edges.append(edge)
                for i in self.graph.get_all_v().values():
                    curr = {"pos": i.get_pos(), "id": i.get_key()}
                    nodes.append(curr)
                json.dump({"Edges": edges, "Nodes": nodes}, fp=file)
        except IOError as e:
            print(e)
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        return the short path and the shortest way
        if we dont have graph we return none
        we do for to set distance to max inf then we pick the node we start
        then we do minheap and we doing a list unvisit
        then we going to the neightbour and if the distance of start and the distance of neighbour is more then the distance more then the distance
        we change and give the prev for neighbour to be start the then doing hepify
        after we finish we going from id2 to the strat and put them in the path then we doing reverse to the path
        :param id1:
        :param id2:
        :return:
        """
        unvisited = []
        path = []
        if self.graph is None:
            return None
        for key, value in self.graph.vertices.items():
            if id1 != key:
                value.set_distance(math.inf)

                unvisited.append(key)
            else:
                value.set_distance(0)
                unvisited.append(key)

        heapq.heapify(unvisited)

        while len(unvisited) > 0:
            curr = heapq.heappop(unvisited)

            dict = self.graph.all_out_edges_of_node(curr)
            for neightbour in dict:
                neightbour_vertex = neightbour
                neightbour_distance = self.graph.get_edge(curr, neightbour)

                distance = self.graph.get_node(curr).distance + neightbour_distance

                if distance < self.graph.get_node(neightbour).distance:
                    self.graph.get_node(neightbour_vertex).set_distance(distance)
                    self.graph.get_node(neightbour_vertex).set_prev(curr)
                    heapq.heapify(unvisited)

        node = self.graph.get_node(id2)
        while node != None:
            p = self.graph.get_node(node.key).previous
            prev = self.graph.get_node(p)
            path.append(node.key)
            node = prev
        distance = self.graph.get_node(id2).distance
        path.reverse()
        return distance, path

    def connected_component(self, id1: int) -> list:
        """
        we doing list len vertiecs
        then we doing bfs and return list
        then we doing transpose and return list
        if we have same number in the bfs list and in the transpose we put the in the dest list
        if bfs [1,2,3,4,5]
        if transpose [2,4,7,9,1]
        the dest[1,2,4]
        :param id1:
        :return:
        """
        temp = []
        dest = []
        visited = [False] * len(self.graph.vertices)
        list_bfs = self.bfs(id1, visited)
        list_transpose = self.transpose(id1, temp)
        for i in self.graph.vertices:
            if list_transpose.__contains__(i) and list_bfs.__contains__(i):
                dest.append(i)
        return dest

    def connected_components(self) -> List[list]:
        """
         we the graph is none we doing for and step over all the vertices then we take the connected component of each vertex
         and then if is not contains in the path we put in the path
        :return:
        """
        path = []

        if self.graph is not None:
            for i in range(self.graph.vertices_size):
                temp = self.connected_component(i)
                if not path.__contains__(temp):
                    path.append(temp)

        return path

    def transpose(self, id1, visited) -> list:
        """
        the transpose like the bfs we doing path[]
        then we doing list visited and queue
        then we put the id1 in the start and using funcion all_in_edges_of_node
        then we you change to true if we visited
        :param id1:
        :param visited:
        :return:
        """
        path = []
        visited = [False] * len(self.graph.vertices)
        visited[id1] = True
        q = queue.Queue()
        q.put(id1)
        while not q.empty():
            temp_vertex = q.get()
            path.append(temp_vertex)
            dict = self.graph.all_in_edges_of_node(temp_vertex)
            for neighbour in dict:
                if not visited[neighbour]:
                    q.put(neighbour)
                    path.append(neighbour)
                    visited[neighbour] = True

        return path

    def bfs(self, start: int, v: []) -> list:
        """
        we doing list if is empty we return []
        if is not empty we doing queue and path
        then we put in the queue the start and we going over all of neighbour of starts and then we change to visited
        :param start:
        :param v:
        :return:
        """
        visited = v
        q = queue.Queue()
        path = []
        q.put(start)
        visited[start] = True

        while not q.empty():
            temp_vertex = q.get()
            path.append(temp_vertex)
            dict = self.graph.all_out_edges_of_node(temp_vertex)
            for neighbour in dict:
                if not visited[neighbour]:
                    q.put(neighbour)
                    visited[neighbour] = True
        return path

    def plot_graph(self) -> None:
        """
         Plots the graph.
         If the nodes have a position, the nodes will be placed there.
         Otherwise, they will be placed in a random but elegant manner.
         @return: None
         """
        x = []
        y = []
        key = []
        if self.graph.get_all_v() is None:
            return None

        for i in self.graph.get_all_v().keys():
            node_temp = self.graph.get_node(i)
            if node_temp.get_pos() is None:
                node_temp.set_pos((random() * 434), (random() * 35), 0)
            x.append(node_temp.get_pos()[0])
            y.append(node_temp.get_pos()[1])
            key.append(i)

        fig, ax = plt.subplots()
        ax.scatter(x, y)
        for i, txt in enumerate(key):
            ax.annotate(key[i], (x[i], y[i]))
        for n in self.graph.get_all_v().keys():
            for j in self.graph.all_out_edges_of_node(n):
                x1 = self.graph.get_all_v().get(n).get_pos()[0]
                y1 = self.graph.get_all_v().get(n).get_pos()[1]
                x2 = self.graph.get_all_v().get(j).get_pos()[0]
                y2 = self.graph.get_all_v().get(j).get_pos()[1]
                plt.arrow(x1, y1, (x2 - x1), (y2 - y1), length_includes_head=True, width=0.000007, head_width=0.0003,
                          ec='green')
        plt.title("Ex3-OOP")
        plt.plot(x, y, "ro")
        plt.ylabel("y")
        plt.xlabel("x")

        plt.show()
