
from mario import Mario
from tilemap import Map
from random import randint
from decorations import Decorations
import pyxel
from tilemap import Map
from enemy import Enemy
import time

# The interface is where all code comes together and is drawn on the screen
class Interface:

    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h

        self.death_counter = 0
        self.game_attempt = 0

        self.reset_game = False

        self.decorations = Decorations()
        self.map = Map(0, 200)

        self.mario = Mario(20, 1, "mario", 16, 16, self.map)


    def update(self):
        self.mario.update()
        self.map.update()

        if pyxel.btnp(pyxel.KEY_K):
            self.mario.alive = False

 
        if self.reset_interface():
            self.mario.y = 0
            self.mario.x = 20
            self.map.koopas = self.map.create_koopas()
            self.map.goombas = self.map.create_goombas()
            self.map.bricks = self.map.create_brick_blocks()
            self.map.questions = self.map.create_question_blocks()
            self.map.x = 0
            self.mario.alive = True
            self.death_counter += 1
        
        if self.death_counter == 3:
            self.reset_game = True
            self.death_counter = 0
            self.game_attempt += 1

    def draw(self):
        pyxel.cls(0)

        self.map.draw()
        self.mario.draw()
        self.decorations.draw(self.mario.x, self.mario.y)

        
        if self.reset_game:
            pyxel.text(
                4, 40, f"You died 3 times! Game Repeated. {self.game_attempt}", 4)

        lives = "Lives: {}".format(3 - self.death_counter)
        pyxel.text(4, 30, lives, 7)

                
        time = 100 - pyxel.frame_count // 30
        pyxel.text(50, 4, f"Time remaining: {time}", 7)
        
        if time == 0:
            self.mario.alive = False 
        
        
        s = "score: {}".format(self.mario.score)
        pyxel.text(4, 4, s, 7)
        

    def reset_interface(self):
        if not self.mario.alive:
            return True
