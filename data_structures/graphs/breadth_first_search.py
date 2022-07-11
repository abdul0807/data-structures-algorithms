# ********************************************
# Created by Mohammed Abdul Qavi on 11/07/22
# ********************************************

from collections import deque


class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges
        self.node_names = []
        self._node_map = {}

    def set_node_names(self, names):
        """The Nth name in names should correspond to node number N.
        Node numbers are 0 based (starting at 0).
        """
        self.node_names = list(names)

    def insert_node(self, new_node_val):
        "Insert a new node with value new_node_val"
        new_node = Node(new_node_val)
        self.nodes.append(new_node)
        self._node_map[new_node_val] = new_node
        return new_node

    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        "Insert a new edge, creating new nodes if necessary"
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
            from_node = self.insert_node(node_from_val)

        if to_node is None:
            to_node = self.insert_node(node_to_val)

        new_edge = Edge(new_edge_val, from_node, to_node)
        from_node.edges.append(new_edge)
        to_node.edges.append(new_edge)
        self.edges.append(new_edge)

    def find_max_index(self):
        """Return the highest found node number
        Or the length of the node names if set with set_node_names()."""
        if len(self.node_names) > 0:
            return len(self.node_names)

        max_index = -1
        for node in self.nodes:
            max_index = max(max_index, node.value)

        return max_index

    def find_node(self, node_number):
        "Return the node with value node_number or None"
        return self._node_map.get(node_number)

    def _clear_visited(self):
        for node in self.nodes:
            node.visited = False

    def bfs(self, start_node_num):
        """An iterative implementation of Breadth First Search
        iterating through a node's edges. The output is a list of
        numbers corresponding to the traversed nodes.
        RETURN: a list of the node values (integers)."""
        node = self.find_node(start_node_num)
        self._clear_visited()
        ret_list = [node.value]

        q = deque()
        q.append(node)
        node.visited = True

        while len(q):
            node = q.pop()
            for edge in node.edges:
                if edge.node_from == node and not edge.node_to.visited:
                    ret_list.append(edge.node_to.value)
                    q.append(edge.node_to)
                    edge.node_to.visited = True

        return ret_list

    def bfs_names(self, start_node_num):
        """Return the results of bfs with numbers converted to names."""
        return [self.node_names[num] for num in self.bfs(start_node_num)]


if __name__ == "__main__":
    graph = Graph()
    graph.set_node_names(
        (
            'Mountain View',  # 0
            'San Francisco',  # 1
            'London',  # 2
            'Shanghai',  # 3
            'Berlin',  # 4
            'Sao Paolo',  # 5
            'Bangalore',  # 6
        )
    )

    graph.insert_edge(51, 0, 1)  # MV <-> SF
    graph.insert_edge(51, 1, 0)  # SF <-> MV
    graph.insert_edge(9950, 0, 3)  # MV <-> Shanghai
    graph.insert_edge(9950, 3, 0)  # Shanghai <-> MV
    graph.insert_edge(10375, 0, 5)  # MV <-> Sao Paolo
    graph.insert_edge(10375, 5, 0)  # Sao Paolo <-> MV
    graph.insert_edge(9900, 1, 3)  # SF <-> Shanghai
    graph.insert_edge(9900, 3, 1)  # Shanghai <-> SF
    graph.insert_edge(9130, 1, 4)  # SF <-> Berlin
    graph.insert_edge(9130, 4, 1)  # Berlin <-> SF
    graph.insert_edge(9217, 2, 3)  # London <-> Shanghai
    graph.insert_edge(9217, 3, 2)  # Shanghai <-> London
    graph.insert_edge(932, 2, 4)  # London <-> Berlin
    graph.insert_edge(932, 4, 2)  # Berlin <-> London
    graph.insert_edge(9471, 2, 5)  # London <-> Sao Paolo
    graph.insert_edge(9471, 5, 2)  # Sao Paolo <-> London
    # (6) 'Bangalore' is intentionally disconnected (no edges)
    # for this problem and should produce None in the
    # Adjacency List, etc.

    print("\nBreadth First Search")
    print(graph.bfs_names(2))


"""
Output

Breadth First Search
['London', 'Shanghai', 'Berlin', 'Sao Paolo', 'Mountain View', 'San Francisco']

"""