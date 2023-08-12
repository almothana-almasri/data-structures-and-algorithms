from code_challange_class35.graphs.graphs import Graph

def test_add_vertex():
    g = Graph()
    vertex = g.add_vertex('A')
    assert vertex in g.get_vertices()

def test_add_edge():
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    g.add_edge(a, b)
    neighbors = g.get_neighbors(a)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == b

def test_get_vertices():
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    vertices = g.get_vertices()
    assert a in vertices
    assert b in vertices

def test_get_neighbors_with_weight():
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    g.add_edge(a, b, weight=5)
    neighbors = g.get_neighbors(a)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == b
    assert neighbors[0].weight == 5

def test_size():
    g = Graph()
    a = g.add_vertex('A')
    b = g.add_vertex('B')
    assert g.size() == 2

def test_single_vertex_edge():
    g = Graph()
    a = g.add_vertex('A')
    assert g.size() == 1
    neighbors = g.get_neighbors(a)
    assert len(neighbors) == 0

if __name__ == '__main__':
    pass