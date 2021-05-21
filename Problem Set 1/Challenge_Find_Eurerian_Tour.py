def make_unexplored_graph(graph, current_edge):
    unexlpored = [edge for edge in graph if edge != current_edge]
    return unexlpored


def find_eulerian_tour(graph):
    unexplored = graph
    node = graph[0][0]
    path = [node]
    open_set = [[path, node, unexplored]]

    while open_set:
        path, node, unexplored = open_set.pop()
        if not unexplored:
            return path

        for edge in unexplored:
            if node in edge:
                node1 = edge[1] if node == edge[0] else edge[0]
                path1 = path + [node1]
                unexplored1 = make_unexplored_graph(unexplored, edge)
                open_set.append([path1, node1, unexplored1])

    return path


if __name__ == "__main__":
    graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8),
             (1, 6), (3, 7), (5, 9), (2, 4), (0, 4),
             (2, 5), (3, 6), (8, 9)]
    print(find_eulerian_tour(graph))
