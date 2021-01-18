from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        """
        constructor
        """
        self.edges = []
        self.vertices = {}
        self.mc = 0
        self.edge_size = 0
        self.vertices_size = 0

    def e_size(self) -> int:
        """
        return the number of edges in graph
        """
        return self.edge_size

    def get_mc(self) -> int:
        """
        returns the number of changes we made to the graph
        """
        return self.mc

    def get_all_v(self) -> dict:
        """
        return dictionary of all node in the graph
        represented {node_key,node_data}
        """
        return self.vertices

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        return dictionary of nodes connected to the node
        represented {node,weight}
        """
        edge_dict = {}
        if self.edge_size < 1 or self.vertices_size == 0:
            return edge_dict
        for curr in self.edges:
            if curr[1] == id1:
                edge_dict[curr[0]] = curr[2]
                return edge_dict
        return edge_dict

    def all_out_edges_of_node(self, id1: int) -> dict:
        """"
        return dictionary of nodes connected from
        represented {node,weight}
        """
        edge_dict = {}
        if self.edge_size < 1 or self.vertices_size == 0:
            return edge_dict

        for curr in self.edges:
            if curr[0] == id1:
                edge_dict[curr[1]] = curr[2]
        self.mc += 1
        return edge_dict

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        add age to the graph
        if the edge is exist we do nothing and return false or weight<0
        if the nodes id1 or id2 not in the graph return false
        we retrun true if the graph is added

        :param self:
        :param id1:
        :param id2:
        :param weight:
        :return:
        """
        edge_id = [id1, id2, weight]
        if weight < 0:
            return False
        if self.vertices.__contains__(id1) is None or self.vertices.__contains__(id2) is None:
            return False
        else:
            flag = False
            i = 0
            while i < len(self.edges) and flag == False:
                edge = self.edges[i]
                if edge[0] == id1 and edge[1] == id2:
                    edge[2] = weight
                    flag = True
                    self.mc += 1
                    self.edge_size += 1
                    return True
                i += 1
        if flag == False:
            self.edges.append(edge_id)
            self.mc += 1
            self.edge_size += 1
            return True
        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        if we dont have the node in graph
        we create new node and put him on the graph
        :param self:
        :param node_id:
        :param pos:
        :return:
        """
        if self.vertices.get(node_id) is None:
            self.vertices[node_id] = Node(node_id, pos)
            self.mc += 1
            self.vertices_size += 1
            return True
        return False

    def remove_node(self, node_id: int) -> bool:
        """
        remove node from the graph
        if the size <1 we dont do nothing or if the node is not on the graph we return false
        we return true and remove him from dictionary of edges and remove edge
        then we remove from the graph

        :param self:
        :param node_id:
        :return:
        """
        if self.vertices_size < 1:
            return False
        elif self.vertices.get(node_id) is None:
            return False
        else:
            edge = self.edges
            for curr in edge:
                if curr[0] == node_id or curr[1] == node_id:
                    self.edges.remove(curr)
                    self.edge_size -= 1
            self.vertices.__delitem__(node_id)
            self.mc += 1
            self.vertices_size -= 1
            return True

        return False

    def get_edge(self, id1: int, id2: int) -> float:
        """
        return the edge
        if some of the nodes not in the graph we return -1
         we return the edge between the src id->dest id
        :param self:
        :param id1:
        :param id2:
        :return:
        """
        if self.vertices.__contains__(id1) is None or self.vertices.__contains__(id2) is None:
            return -1
        else:
            flag = False
            i = 0
            while i < len(self.edges) and flag == False:
                edge = self.edges[i]
                if edge[0] == id1 and edge[1] == id2:
                    return edge[2]
                i += 1
        return -1

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        remove edge from graph
        if we dont have edges and if we dont have the nodes in the graph we return false
        we return true if the edge exist and is remove from the dic
        :param self:
        :param node_id1:
        :param node_id2:
        :return:
        """
        if self.edge_size < 1:
            return False
        elif self.vertices.__contains__(node_id1) is None or self.vertices.__contains__(node_id2) is None:
            return False
        else:
            edge = self.edges
            for curr in edge:
                if curr[0] == node_id1 and curr[1] == node_id2:
                    self.edges.remove(curr)
                    self.edge_size -= 1
                    self.mc += 1
                    return True
        return False

    def v_size(self) -> int:
        """
         return size of node on the graph
        :param self:
        :return:
        """
        return self.vertices_size

    def get_node(self, node_id: int) -> Node:
        """
        return the node in the graph the key
        :param self:
        :param node_id:
        :return:
        """
        return self.vertices.get(node_id)

    # def _repr_(self) -> str:
    #
    #     graph_info = f"Graph: |V|={self.v_size()} , |E|={self.e_size()}\n"
    #     graph_info += "{"
    #     i = 0
    #     for j in self.vertices.keys():
    #         i += 1
    #         graph_info += f"{j}: {j}: |edges out| "
    #         graph_info += f"{len(self.all_out_edges_of_node(j).keys())} "
    #         graph_info += "|edges in| "
    #         graph_info += f"{len(self.all_in_edges_of_node(j).keys())}"
    #
    #         if len(self.vertices.keys()) == i:
    #             graph_info += "}"
    #         else:
    #             graph_info += ", "
    #     return graph_info

    def _repr_(self) -> str:

        graph_info = f"Graph: |V|={self.vertices_size} , |E|={self.edge_size}\n"
        graph_info += "{"
        i = 0
        for j in self.vertices.keys():
            i += 1
            graph_info += f"{j}: {j}: |edges out| "
            graph_info += f"{len(self.all_out_edges_of_node(j).keys())} "
            graph_info += "|edges in| "
            graph_info += f"{len(self.all_in_edges_of_node(j).keys())}"

            if len(self.vertices.keys()) == i:
                graph_info += "}"
            else:
                graph_info += ", "
        return graph_info


if __name__ == '__main__':
    graph = DiGraph()
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    graph.add_node(a.key)
    graph.add_node(b.key)
    graph.add_node(c.key)
    graph.add_node(d.key)
    graph.add_edge(a.key, d.key, 2.2)
    graph.add_edge(a.key, b.key, 2.3)
    graph.add_edge(a.key, c.key, 5.2)
    print("edgegraph", graph.edges)
    graph.add_edge(a.key, d.key, 3.2)
    graph.add_edge(b.key, c.key, 8.2)
    print("graph is :", graph)

