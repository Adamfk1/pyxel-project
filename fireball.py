import pyxel


class Fireball:
    def __init__(self):
        self.x = -10
        self.y = 0
        self.vx = 0
        self.vy = 0
        self.GRAVITY = 0.075
        self.B_SPD_X = 1.25
        self.B_SPD_Y = 2
        
        self.sprite = (0, 48, 104, 8, 8)
        
    
    def fire(self, x, y):
        self.x = x
        self.y = y
        self.vx = self.B_SPD_X
        self.vy = -self.B_SPD_Y
        

    def update_pve(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.GRAVITY
        self.sprite = (0, 48, 104, -8, 8)
        
    def update_nve(self):
        self.x -= self.vx
        self.y += self.vy
        self.vy += self.GRAVITY
        self.sprite = (0, 48, 104, 8, 8)