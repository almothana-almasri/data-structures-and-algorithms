import pytest
from code_challange_class37.business_trip.graphs import *
from code_challange_class37.business_trip.business_trip import *

@pytest.fixture
def sample_graph():
    graph = Graph()
    metroville = graph.add_vertex("Metroville")
    pandora = graph.add_vertex("Pandora")
    arendelle = graph.add_vertex("Arendelle")
    new_monstropolis = graph.add_vertex("New Monstropolis")
    naboo = graph.add_vertex("Naboo")
    narnia = graph.add_vertex("Narnia")

    graph.add_edge(metroville, pandora, 82)
    graph.add_edge(arendelle, new_monstropolis, 42)
    graph.add_edge(arendelle, naboo, 150)
    graph.add_edge(naboo, pandora, 82)
    graph.add_edge(narnia, metroville, 125)

    return graph

def test_add_vertex(sample_graph):
    assert len(sample_graph.get_vertices()) == 6
    new_vertex = sample_graph.add_vertex("Atlantis")
    assert len(sample_graph.get_vertices()) == 7
    assert new_vertex in sample_graph.get_vertices()

def test_add_edge(sample_graph):
    start_vertex = sample_graph.add_vertex("Atlantis")
    end_vertex = sample_graph.add_vertex("Naboo")
    sample_graph.add_edge(start_vertex, end_vertex, 200)
    
    neighbors = sample_graph.get_neighbors(start_vertex)
    assert len(neighbors) == 1
    assert neighbors[0].vertex == end_vertex
    assert neighbors[0].weight == 200

def test_business_trip_not_possible(sample_graph):
    itinerary = ["Naboo", "Pandora", "Narnia"]
    cost = business_trip(sample_graph, itinerary)
    assert cost is None