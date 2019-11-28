import random
from alien import Alien

def unleash_aliens(num_aliens, cities_map):
    aliens = []
    for alien_id in range(1, num_aliens):
        random_city = random.choice(list(cities_map))
        alien = Alien(alien_id, random_city)
        aliens.append(alien)
    return aliens