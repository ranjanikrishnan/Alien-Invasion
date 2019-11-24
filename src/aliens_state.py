from collections import Counter
import random
from destroy_city import destroy_city

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
            aliens_new_state = alien
            print(f'City:{aliens_new_state.city}, Id:{aliens_new_state.id}')
    return aliens_new_state

def move_aliens(aliens, cities_map):
    for step in range(1):
        fighting_aliens = identify_fighting_aliens(aliens)
        aliens_new_state = surviving_aliens(aliens, fighting_aliens)
        new_map = destroy_city(cities_map, fighting_aliens)
        for alien in aliens:
            alien.city = random.choice(cities_map[alien.city])