from collections import Counter
import random
from generate_io import generate_map, print_output

def identify_fighting_aliens(aliens):
    cities = []
    reoccuring_cities = []
    fighting_aliens = {}
    for alien in aliens:
        cities.append(alien.city)
    city_count = Counter(cities)
    for city, count in city_count.items():
        if count > 1:
            reoccuring_cities.append(city)
    fighting_aliens = {}
    for city in reoccuring_cities:
        hosted_aliens = []
        for alien in aliens:
            if city == alien.city:
                hosted_aliens.append(alien.id)   
        fighting_aliens[city] = hosted_aliens
    return fighting_aliens

def surviving_aliens(aliens, fighting_aliens):
    alien_index = []
    aliens_new_state = []
    for index, alien in enumerate(aliens):
        if alien.city in fighting_aliens.keys():
            alien_index.append(index)
    for index, alien in enumerate(aliens):
        if index not in alien_index:
            aliens_new_state.append(alien)
    return aliens_new_state
