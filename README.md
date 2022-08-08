# Directed Weighted graph-OOP

## This is an object oriented programmin project which his main idea is based on functions.

## This Project Made by Yosef Desse and Daniel Nevo Students in Ariel University.

## at this project we implement the data structure of directional weighted graph with vertexs and edges.

## we implement a 4 main classes: Node, edge_data , WGraph_DS , WGraph_Algo and These classes contains serval methods.


## Class Node:

### This Class represents the set of operations applicable on a single node(vertex) in a directional weighted graph. Every node gets it key, tag, pos and info.
### this class contains several functions:

def get_key(self):
Returns the node key.

def get_pos(self):
return the node pos

def set_pos(self, x: float, y: float, z: float):
set a new pos by given p.
.
def get_info(self):
return the  node info.

def set_info(self, info):
set a new info for node by given String info.

def get_tag(self):
return the node Tag.

def set_tag(self, tag):
set a new Tag for the node by given int tag.

def get_distance(self)
return the dis of the node.

def set_distance(self, distance):
set a new distance for the node.



## Class edge_data :

### This Class represents the set of operations applicable on a  edge(src,dest) in a directional weighted graph.
### this class contains several functions:

def get_src(self):
return the surce of the edge.

def get_dest(self):
return the destination of the edge.

def get_weight(self):
return the weight of the edge.

def setWeight(double w) :
set a new weight on the edge by given new double w.

def get_tag(self,tag) :
return the tag of the edge.

def set_tag(self,tag):
set a new tag on the edge by given new int tag.




##  Class DiGraph(GraphInterface):

### This class represents the set of opretions applicable on graph in a directional weighted graph. 
### we implement this Graph with a two data structure one called dictionary vertices and the second called list edges one contains the Nodes and the other one contains the nodes and all the  edges of the same node.
### this class contains several functions:

def get_node(self, node_id: int):
return node by given key.

def get_edge(self, id1: int, id2: int):
check if there is an edge between src and dest and if there such edge, return the edge between src and dest ,else return -1.

def add_node(self, node_id: int, pos: tuple = None):
add a new node to the graph.

def add_edge(self, id1: int, id2: int, weight: float):
add an edge between id1 and id2 If and there is already edge exists between src and dest just update the Weight

def get_all_v(self) ):
return dictionary of  all the vertice of the graph

def all_in_edges_of_node(self, id1: int):
return  dictionary of all the node  that node id1 neighbor

def all_out_edges_of_node(self, id1: int):
return  dictionary of all the node neighbors

def remove_node(self, node_id: int)  :
delete the node by given key from the graph and delete him from all his neighbors (edges).

def remove_edge(self, node_id1: int, node_id2: int) ):
remove the edge between node_id1 and node_id2 .

def v_size(self):
return the number of the nodes in the graph.

def e_size(self)
return the number of the edges in the graph.

def get_mc(self) :
 returns the number of changes we made to the graph

## Class GraphAlgo(GraphAlgoInterface):

### This Class represents the "regular" Graph Theory algorithms.
### in this class we used  several functions like : 
### 1.bfs(self, start: int, v: []) - Go through all the neighbors of the vertex and create a list of all the neighbors that come out of the vertex
### 2. transpose(self, id1, visited) - Go through all the neighbors of the vertex and create a list of all the neighbors that come In  the vertex


### this class contains several functions:

def __init__(self, graph: DiGraph = None):
init the graph .

def get_graph(self) :
return the the graph.

def shortest_path(self, id1: int, id2: int):
return the shortest path between id1to id2 as an list of nodes and the length of the shortest path.

def connected_component(self, id1: int) :
returns the Strongly Connected Component in the graph that node id1 is  one of part of the component.

def connected_components(self):
returns all the Strongly Connected Component in the graph.

def save_to_json(self, file_name: str):
saves the graph to the given file name.

def load_from_json(self, file_name: str):
load a graph from the file to this graph algorithm.
