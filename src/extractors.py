def extract_city(city_connections):
    return city_connections.split(' ')[0]

def extract_neighbors(city_connections):
    neighbors =[]
    separated = city_connections.split(' ')[1:]
    neighbors = [each.lstrip("north=south=west=").rstrip('\n') for each in separated]
    return neighbors
