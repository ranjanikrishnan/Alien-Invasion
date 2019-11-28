class Alien:
    def __init__(self, id, city):
        self.id = id
        self.city = city

    def __str__(self):
        return f'id: {self.id} city: {self.city}'
