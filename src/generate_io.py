from read_map import extract_city, extract_directions, extract_neighbors

def generate_map(input_file, include_directions=False):
    city_map = {}
    with open(input_file,'r') as file:
        for line in file:
            city = extract_city(line)
            if include_directions:
                neighbors = extract_directions(line)    
            else:
                neighbors = extract_neighbors(line)
            city_map.setdefault(city, neighbors)
    return city_map

def print_output(latest_city_map, city_map_cardinal):
    for city, neighbors in latest_city_map.items():
        if city in city_map_cardinal:
            city_directions = []
            cardinal_neighbors = (city_map_cardinal[city])
        for neighbor in neighbors:
            for cardinal_city, direction in cardinal_neighbors.items():
                if cardinal_city == neighbor:
                    city_directions.append(f'{direction}={cardinal_city} ')    
        print_directions = ''.join(city_directions)      
        print(f'{city} {print_directions}')