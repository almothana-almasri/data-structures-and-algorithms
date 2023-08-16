from code_challange_class37.business_trip.graphs import *

def business_trip(graph, itinerary):
    total_cost = 0
    
    for i in range(len(itinerary) - 1):
        current_city = Vertex(itinerary[i])
        next_city = Vertex(itinerary[i + 1])
        
        neighbors = graph.get_neighbors(current_city)
        found = False
        
        for edge in neighbors:
            if edge.vertex == next_city:
                total_cost += edge.weight
                found = True
                break
        
        if not found:
            return None
    
    return total_cost