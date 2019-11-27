import argparse
from read_map import extract_city, extract_neighbors, extract_directions
from unleash_aliens import unleash_aliens
from aliens_state import move_aliens
from destroy_city import destroy_city

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Alien Simulation')
    parser.add_argument('input_file', help='input file path')
    parser.add_argument('num_aliens', help='number of aliens')
    args = parser.parse_args()
    num_aliens = int(args.num_aliens)
    input_file = args.input_file
    city_map = generate_map(input_file)
    city_map_cardinal = generate_map(input_file, include_directions=True)
    aliens_state = unleash_aliens(num_aliens, city_map)
    latest_city_map = move_aliens(aliens_state, city_map)
    print_output(latest_city_map, city_map_cardinal)
