import copy

def remove_city_references(cities_map, fighting_aliens):
    latest_cities_map = copy.deepcopy(cities_map)

    def find_references(city_name):
        references = cities_map.get(city_name)
        if not references:
            return []
        return references

    for destroyed_city in fighting_aliens:
        references = find_references(destroyed_city)
        for reference in references:
            reference_neighbors = find_references(reference)
            if reference_neighbors and (destroyed_city in reference_neighbors):
                latest_reference_neighbors = copy.deepcopy(reference_neighbors)
                latest_reference_neighbors.remove(destroyed_city)
                latest_cities_map[reference] = latest_reference_neighbors
    return latest_cities_map

def remove_city(cities_map, fighting_aliens):
    for destroyed_city in fighting_aliens:
        if destroyed_city in cities_map:
            del cities_map[destroyed_city]
    return cities_map
    
def print_destroyed_cities(fighting_aliens):
    for city, alien_ids in fighting_aliens.items():
        alien_id_to_print = ''
        for alien_id in alien_ids:
            alien_id_str = f'alien {alien_id}, '
            if alien_id == alien_ids[-1]:
                alien_id_str = f'and alien {alien_id}.'
            alien_id_to_print = alien_id_to_print + alien_id_str
        print(f'{city} has been destroyed by {alien_id_to_print}')

def destroy_city(cities_map, fighting_aliens):
    latest_city_map = remove_city_references(cities_map, fighting_aliens)
    latest_city_map = remove_city(latest_city_map, fighting_aliens)
    print_destroyed_cities(fighting_aliens)
    return latest_city_map