from collections import deque

def shortest_path(graph, start, end):

    queue = deque([[start]])
    visited = set()

    while queue:

        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:

            visited.add(node)

            for neighbor in graph[node]:

                new_path = list(path)
                new_path.append(neighbor)

                queue.append(new_path)

    return None