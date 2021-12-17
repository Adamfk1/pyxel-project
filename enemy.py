
class Enemy:
    def __init__(self, x: int,  y: int,  w: int,  h: int, count_lives, sprite):
        
        
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.sprite = sprite
        self.count_lives = count_lives

    def collide_enemies_with(self, mario):
        if (mario.x < self.x + self.w and
            mario.x + self.w > self.x and
            mario.y < self.y + self.h and
            mario.h + mario.y > self.y):
            
            if (self.x <= mario.x + mario.w <= self.x + 8) and ((self.y <= mario.y + mario.h <= self.y + self.h) or (self.y < mario.y < self.y + self.h)):
                if self.sprite != (0, 0, 120, 16, 16):
                    mario.alive = False
                

                print('Collision from left')

            elif (self.x + self.w - 8 <= mario.x <= self.x + self.w) and ((self.y <= mario.y + mario.h <= self.y + self.h) or (self.y < mario.y < self.y + self.h)):
                
                mario.alive = False
                print('Collision from right')



            elif mario.x + mario.w > self.x and mario.y + mario.h < self.y + self.h/2:
                self.count_lives -= 1
                
                print('Collision from above')
                
 