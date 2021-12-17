import pyxel

class Decorations:
    
    def __init__(self):
        self.__cloud = [(-10, 40), (90, 25)]
        self.score = 0
    
    @property
    def cloud(self):
        return self.__cloud
    
    def draw(self, x_coord, y_coord):

        # Draw Clouds
        offset = (pyxel.frame_count // 16) % 160
        for i in range(2):
            for x, y in self.__cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 16, 64, 48, 24, 12)
        
