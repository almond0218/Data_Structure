from heapq import heapify
from heapq import heappop


class Node:
    def __init__(self, key):
        self.key = key
        self.edges = {}

    def __lt__(self, other):
        return self.key < other.key

    def add_edge(self, target, cost):
        self.edges[target] = cost


class Dijkstra:
    def __init__(self, nodes, source=0):
        self.source = source
        self.distances = [0 if i == source else float("inf") for i in range(len(nodes))]
        self.parents = [None for _ in range(len(nodes))]
        self.queue = [(self.distances[node.key], node) for node in nodes]
        heapify(self.queue)

    def process(self):
        while self.queue:
            _, current_node = heappop(self.queue)
            for target_node_key, edge_cost in current_node.edges.items():
                current_node_distance = self._get_distance_from_key(current_node.key)
                self._relax(
                    current_node.key, current_node_distance, target_node_key, edge_cost
                )
        return self.distances, self.parents

    def _relax(
        self, current_node_key, current_node_distance, target_node_key, edge_cost
    ):
        target_node_distance = self._get_distance_from_key(target_node_key)
        cost = current_node_distance + edge_cost
        if target_node_distance > cost:
            self._set_distance(target_node_key, cost)
            self._set_parent(target_node_key, current_node_key)
            self._reset_queue()

    def _get_distance_from_key(self, key):
        return self.distances[key]

    def _set_distance(self, key, distance):
        self.distances[key] = distance

    def _set_parent(self, key, parent_key):
        self.parents[key] = parent_key

    def _reset_queue(self):
        self.queue = [(self.distances[node.key], node) for _, node in self.queue]
        heapify(self.queue)


class App:
    def __init__(self):
        num_nodes = int(input())
        nodes = [Node(i) for i in range(num_nodes)]

        num_edges = int(input())
        for _ in range(num_edges):
            key, target, cost = map(int, input().split())
            nodes[key].add_edge(target, cost)

        d = Dijkstra(nodes)
        distances, parents = d.process()
        print("distances: {}".format(distances))
        print("parents: {}".format(parents))


App()
