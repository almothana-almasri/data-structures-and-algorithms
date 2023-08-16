import pytest
from code_challange_class38.depth_first.depth_first import Graph, Vertex

@pytest.fixture
def graph():
    return Graph()

def test_depth_first_empty(graph):
    vertex_a = graph.add_vertex('A')
    result = graph.depth_first(vertex_a)
    assert result == ['A']

def test_depth_first_single_path(graph):
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')
    vertex_d = graph.add_vertex('D')
    
    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_b, vertex_c)
    graph.add_edge(vertex_c, vertex_d)
    
    result = graph.depth_first(vertex_a)
    assert result == ['A', 'B', 'C', 'D']

def test_depth_first_branching(graph):
    vertex_a = graph.add_vertex('A')
    vertex_b = graph.add_vertex('B')
    vertex_c = graph.add_vertex('C')
    vertex_d = graph.add_vertex('D')
    
    graph.add_edge(vertex_a, vertex_b)
    graph.add_edge(vertex_a, vertex_c)
    graph.add_edge(vertex_b, vertex_d)
    
    result = graph.depth_first(vertex_a)
    assert result == ['A', 'B', 'D', 'C']
