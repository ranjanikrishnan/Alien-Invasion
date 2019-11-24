import argparse
from read_map import extract_city, extract_neighbors
from unleash_aliens import unleash_aliens
from aliens_state import move_aliens

def generate_map(input_file):
    city_map = {}
    with open(input_file,'r') as file:
        for line in file:
            city = extract_city(line)
            neighbors = extract_neighbors(line)
            city_map.setdefault(city, neighbors)
    print(city_map)
    return city_map

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Alien Simulation')
    parser.add_argument('input_file', help='input file path')
    parser.add_argument('num_aliens', help='number of aliens')
    args = parser.parse_args()
    num_aliens = int(args.num_aliens)
    input_file = args.input_file
    map = generate_map(input_file)  
    aliens_state = unleash_aliens(num_aliens, map)
    move_aliens(aliens_state, map)
