# ********************************************
# Created by Mohammed Abdul Qavi on 11/07/22
# ********************************************


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        new_node = Node(new_node_val)
        self.nodes.append(new_node)

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_node = None
        to_node = None

        for node in self.nodes:
            if node.value == node_from_val:
                from_node = node

            if node.value == node_to_val:
                to_node = node

            if from_node and to_node:
                break

        if from_node is None:
            from_node = Node(node_from_val)
            self.nodes.append(from_node)

        if to_node is None:
            to_node = Node(node_to_val)
            self.nodes.append(to_node)

        new_edge = Edge(new_edge_val, from_node, to_node)
        from_node.edges.append(new_edge)
        to_node.edges.append(new_edge)
        self.edges.append(new_edge)

    def get_edge_list(self):
        """
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        return [
            (edge.value, edge.node_from.value, edge.node_to.value)
            for edge in self.edges
        ]

    def get_adjacency_list(self):
        """
        Return a list of lists.
        The indices of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        max_index = self.find_max_index()
        adjacent_list = [[] for _ in range(max_index)]

        for edge in self.edges:
            adjacent_list[edge.node_from.value].append((edge.node_to.value, edge.value))

        return [a if len(a) > 0 else None for a in adjacent_list]

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        max_index = self.find_max_index()
        adjacent_matrix = [[0] * max_index for _ in range(max_index)]
        for edge in self.edges:
            adjacent_matrix[edge.node_from.value][edge.node_to.value] = edge.value
        return adjacent_matrix

    def find_max_index(self):
        max_node_index = -1
        for node in self.nodes:
            max_node_index = max(max_node_index, node.value)

        return max_node_index + 1


if __name__ == "__main__":
    graph = Graph()
    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 7)
    graph.insert_edge(103, 7, 4)
    print(graph.get_edge_list())
    print(graph.get_adjacency_list())
    print(graph.get_adjacency_matrix())

"""
Output

[(100, 1, 2), (101, 1, 3), (102, 1, 7), (103, 7, 4)]
[None, [(2, 100), (3, 101), (7, 102)], None, None, None, None, None, [(4, 103)]]
[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 100, 101, 0, 0, 0, 102], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 103, 0, 0, 0]]

"""