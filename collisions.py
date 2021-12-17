import pyxel

class Collisions:
    

    def __init__(self, map):
        self.map = map

    def get_tile_type_at(self, screen_x, screen_y):
        return pyxel.tilemap(2).get((screen_x - self.map.x) // 8, (screen_y // 8) + 66)
        