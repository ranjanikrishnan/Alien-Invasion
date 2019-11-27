def extract_city(city_connections):
    return city_connections.split(' ')[0]

def extract_neighbors(city_connections):
    neighbors = []
    separated = city_connections.split(' ')[1:]
    neighbors = [each.lstrip("north=south=west=east=").rstrip('\n') for each in separated]
    return neighbors

def extract_directions(city_connections):
    directions = {}
    separated = city_connections.split(' ')[1:]
    for each in separated:
        neighbor = each.lstrip("north=south=west=east=").rstrip('\n')
        cardinal = each.split('=')[0]
        directions[neighbor] = cardinal
    return directions