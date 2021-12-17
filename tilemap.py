import pyxel
import random
from goomba import Goomba
from koopa import Koopa
from blocks import Question, Brick, Blocks


class Map:


    def __init__(self, x: int, y: int):

        self.x = x
        self.y = y
        self.sprite = (2, 0, 66, 256, 256)
        self.bricks = self.create_brick_blocks()
        self.questions = self.create_question_blocks()
        self.goombas = self.create_goombas()
        self.koopas = self.create_koopas()
        self.h = self.sprite[4]
        self.w = self.sprite[3]


    def detect_collision(self, mario):

        for i in self.goombas:
            i.collide_enemies_with(mario)
            if i.count_lives == 0:
                self.goombas.remove(i)
                mario.score += 100
        for i in self.koopas:
            i.collide_enemies_with(mario)
            if i.count_lives < 3 and i.count_lives > 0:
                i.y = 208
                i.sprite = (0, 0, 120, 16, 16)
            if i.count_lives < 0:
                self.koopas.remove(i)
                mario.score += 100

        for i in self.questions:
            i.collide_with_blocks(mario)
            if i.collide_below:
                self.questions.remove(i)
                mario.score += 100
                    

        for i in self.bricks:
            i.collide_with_blocks(mario)
            if i.collide_below:
                self.bricks.remove(i)


    def create_goombas(self):
        goombas = [
                    Goomba(170, 208, True, self),
                   Goomba(170*3, 208, True, self)]
        return goombas


    def create_koopas(self):
        koopas = [ 
                   Koopa(179*2, 200, True, self,False, False),
                   Koopa(179*3, 200, True, self,False, False)]
        return koopas

   
    def create_question_blocks(self):
        question_blocks = [Question(176, 160, 16, 16),Question(144,160,16,16)]

        return question_blocks
 
 
    def create_brick_blocks(self):
       brick_blocks = [Brick(160, 160, 16, 16)]
       return brick_blocks


 
    def move(self, velocity: int): 
        self.x += velocity
        for goomba in self.goombas:
            goomba.move(velocity)
        for koopa in self.koopas:
            koopa.move(velocity)
        for question in self.questions:
            question.move(velocity)
        for brick in self.bricks:
            brick.move(velocity)




    def update(self):
        for goomba in self.goombas:
            goomba.update()
        for koopa in self.koopas:
            koopa.update()
        
                

    def draw(self):
          
        pyxel.bltm(self.x, 0, self.sprite[0], self.sprite[1], self.sprite[2], self.sprite[3], self.sprite[4])

        for goomba in self.goombas:
            pyxel.blt(goomba.x, goomba.y, 0, goomba.sprite[1],goomba.sprite[2], goomba.w, goomba.h, 12)

        for koopa in self.koopas:
            pyxel.blt(koopa.x, koopa.y, 0, koopa.sprite[1],koopa.sprite[2], koopa.w, koopa.h, 12)
        
        if len(self.questions) > 0:    
          for question in self.questions:
              pyxel.blt(question.x, question.y, 0, question.sprite[1],question.sprite[2], question.w, question.h, 12)
        
        if len(self.questions) > 0: 
          for brick in self.bricks:
              pyxel.blt(brick.x, question.y, 0, brick.sprite[1],brick.sprite[2], brick.w, brick.h, 12)

