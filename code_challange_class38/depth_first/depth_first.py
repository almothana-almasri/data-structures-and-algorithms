from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)

class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Edge:
    def __init__(self, vertex, weight=0):
        self.weight = weight
        self.vertex = vertex

class Graph:
    def __init__(self):
        self.__adj_list = {}

    def add_vertex(self, value):
        """
        Arguments: value
        Returns: The added vertex
        Add a vertex to the graph
        """
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Arguments: 2 vertices to be connected by the edge, weight (optional)
        Returns: nothing
        Adds a new edge between two vertices in the graph
        If specified, assign a weight to the edge
        Both vertices should already be in the Graph
        """
        if start_vertex not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertex not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertex, weight)
        edge2 = Edge(start_vertex)
        self.__adj_list[start_vertex].append(edge1)
        self.__adj_list[end_vertex].append(edge2)

    def get_vertices(self):
        """
        Arguments: none
        Returns all of the vertices in the graph as a collection (set, list, or similar)
        Empty collection returned if there are no vertices
        """
        return self.__adj_list.keys()

    def size(self):
        return len(self.__adj_list)

    def get_neighbors(self, vertex):
        """
        Arguments: vertex
        Returns a collection of edges connected to the given vertex
        Include the weight of the connection in the returned collection
        Empty collection returned if there are no vertices
        """
        return self.__adj_list.get(vertex, [])

    def breadth_first(self, start_vertex):
        result = []
        visited = set()
        q = Queue()

        q.enqueue(start_vertex)
        visited.add(start_vertex)

        while len(q):
            current_vertex = q.dequeue()

            result.append(current_vertex.value)

            neighbors = self.get_neighbors(current_vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited.add(neighbor)

        return result
    
    def depth_first(self, start_vertex):
        """
        Perform a depth-first traversal of the graph starting from the given vertex.

        Args:
            start_vertex (Vertex): The vertex to start the traversal from.

        Returns:
            list: A list of vertex values in the order they were visited during the traversal.
        """
        result = []
        visited = set()

        def dfs(vertex):
            """
            Recursively perform depth-first traversal starting from a given vertex.

            Args:
                vertex (Vertex): The vertex to start the traversal from.
            """
            visited.add(vertex)
            result.append(vertex.value)

            neighbors = self.get_neighbors(vertex)

            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_vertex)
        return result

if __name__ == "__main__":
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    e = g.add_vertex('E')
    c = g.add_vertex('C')
    d = g.add_vertex('D')
    f = g.add_vertex('F')
    h = g.add_vertex('H')
    x = g.add_vertex('X')

    g.add_edge(a, b)
    g.add_edge(a, d)
    g.add_edge(b, c)
    g.add_edge(b, d)
    g.add_edge(d, e)
    g.add_edge(f, h)
    g.add_edge(d, h)
    g.add_edge(d, f)
    g.add_edge(c, x)

    print("\nDepth First Traversal:")
    print(g.depth_first(a))