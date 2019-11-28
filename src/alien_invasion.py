import argparse
import random
from read_map import extract_city, extract_neighbors, extract_directions
from unleash_aliens import unleash_aliens
from destroy_city import destroy_city
from generate_io import generate_map, print_output
from aliens_state import identify_fighting_aliens, surviving_aliens

def move_aliens(aliens, cities_map):
    latest_city_map = cities_map
    aliens_current_state = aliens
    for step in range(10000):
        fighting_aliens = identify_fighting_aliens(aliens_current_state)
        aliens_current_state = surviving_aliens(aliens_current_state, fighting_aliens)
        latest_city_map = destroy_city(latest_city_map, fighting_aliens)
        if latest_city_map == {}:
            print('All cities destroyed!')
            break
        if not aliens_current_state:
            print('All aliens dead!')
            break
        for alien in aliens_current_state:
            alien.city = random.choice(list(latest_city_map))
    city_map_cardinal = generate_map(input_file, include_directions=True)
    print_output(latest_city_map, city_map_cardinal)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Alien Simulation')
    parser.add_argument('input_file', help='input file path')
    parser.add_argument('num_aliens', help='number of aliens')
    args = parser.parse_args()
    num_aliens = int(args.num_aliens)
    input_file = args.input_file
    city_map = generate_map(input_file)
    aliens_state = unleash_aliens(num_aliens, city_map)
    move_aliens(aliens_state, city_map)
