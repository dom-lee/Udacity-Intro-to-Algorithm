def find_eulerian_tour(graph):
    unexplored = graph
    node = graph[0][0]
    path = [node]
    open_set = [[path, node, unexplored]]

    while open_set:
        path, node, unexplored = open_set.pop()
        if not unexplored:
            return path

        for unexplored_edge in unexplored:
            if node in unexplored_edge:
                node1 = unexplored_edge[1] if node == unexplored_edge[0] else unexplored_edge[0]
                path1 = path + [node1]
                unexplored1 = [edge for edge in unexplored if edge != unexplored_edge]
                open_set.append([path1, node1, unexplored1])

    return path


if __name__ == "__main__":
    graph = [(0, 1), (1, 5), (1, 7), (4, 5), (4, 8),
             (1, 6), (3, 7), (5, 9), (2, 4), (0, 4),
             (2, 5), (3, 6), (8, 9)]
    print(find_eulerian_tour(graph))
