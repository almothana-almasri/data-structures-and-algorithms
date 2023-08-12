[&leftarrow; Back to Home](../README.md)

Author: **Almothana Almasri**

## Code Challenge: Class 33: Implement a simplified LEFT JOIN for 2 Hashmaps.

Implement your own Graph. The graph should be represented as an adjacency list.

## [Code is here](graphs/graphs.py)

## Approach

- The graph is implemented using an adjacency list, where each vertex is associated with a list of edges that represent its neighbors.
- The `add_vertex` method adds a new vertex to the graph by creating an instance of the `Vertex` class and associating an empty list of edges with it in the adjacency list.
- The `add_edge` method adds an edge between two vertices by creating instances of the `Edge` class and adding them to the respective vertex's list of edges.
- The breadth-first traversal is implemented using a queue. Starting from the specified vertex, the traversal explores neighbors level by level while keeping track of visited vertices to avoid revisiting.

## Efficiency

- **Adding Vertices and Edges:**
  - Adding a vertex or an edge has a constant time complexity of O(1).

- **Getting Neighbors:**
  - The time complexity of getting neighbors of a vertex is O(V), where V is the number of vertices.

- **Breadth-First Traversal:**
  - The time complexity of the breadth-first traversal is O(V + E), where V is the number of vertices and E is the number of edges.

- **Space Complexity:**
  - The space complexity is O(V + E) due to the adjacency list, where each vertex and its associated edges contribute to the space used.
  - The additional space used during breadth-first traversal is proportional to the number of vertices.

## Tests

[They are linked here](tests/test_graphs.py)

```bash
pytest -v code_challange_class35/tests/test_graphs.py
```