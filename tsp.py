from sys import maxsize
from itertools import permutations
def travellingSalesmanProblem(graph, s):
    V=len(graph)
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    min_path = maxsize
    next_permutation = permutations(vertex)
    tour_path = None
    for i in next_permutation:
        current_pathweight = 0
        k = s
        path = [s]  # Store the current tour path
        for j in i:
            current_pathweight += graph[k][j]
            path.append(j)  # Append the vertex to the path
            k = j
        current_pathweight += graph[k][s]

        if current_pathweight < min_path:
            min_path = current_pathweight
            tour_path = path  # Update tour path

    # Print tour path
    print("Tour path:", end=" ")
    for vertex in tour_path:
        print(f"v{vertex + 1}", end=" ")  # Adjust index to start from 1 instead of 0
    print(f"v{s + 1}")  # Add the starting vertex to close the tour

    return min_path

graph = [
        [0, 2, 9, float('inf')],
        [1, 0, 6, 4],
        [float('inf'), 7, 0, 8],
        [6, 3, float('inf'), 0]
    ]
s = 0
print(travellingSalesmanProblem(graph, s))
