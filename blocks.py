class Blocks:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def collide_with_blocks(self, mario):
        if (mario.x < self.x + self.w and
            mario.x + self.w > self.x and
            mario.y < self.y + self.h and
                mario.h + mario.y > self.y):

            if mario.x+mario.w > self.x and mario.y+mario.h < self.y+self.h/2:
                pass
            elif ((self.x <= mario.x <= self.x+self.w) or (self.x <= mario.x+mario.w <= self.x+self.w)) and (self.y <= mario.y <= self.y+self.h):
                self.collide_below = True
            else:
                self.collide_below = False



class Question(Blocks):

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.collide_below = False
        self.sprite = (0, 16, 0, 16, 16)

    def update(self):
        pass

    def move(self, velocity: int):
        self.x += velocity


class Brick(Blocks):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.collide_below = False
        self.sprite = (0, 0, 16, 16, 16)

    def update(self):
        pass

    def move(self, velocity: int):
        self.x += velocity





