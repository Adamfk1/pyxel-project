

import time
import pyxel
from fireball import Fireball


class Mario():

    def __init__(self, x: int, y: int, velocity: int, h: int, w: int, map):
        
        self.x = x
        self.y = y
        self.vx = velocity
        self.vy = 0
        self.h = h
        self.w = w

        self.map = map
        self.fireball = Fireball()

        self.score = 0
        
        self.jump_speed = -8
        self.gravity = 0.4

        self.sprite = (0, 0, 48, 16, 16)
        self.alive = True

    def hit_wall_left(self):
        left_bottom = self.get_tile_type_at(self.x, self.y + 13)
        left_top = self.get_tile_type_at(self.x, self.y)

        if left_bottom != 0 or left_top != 0:
            self.x += 1
            self.hit_wall_left()
            
    def hit_wall_right(self):
        right_bottom = self.get_tile_type_at(self.x + 14, self.y + 13)
        right_top = self.get_tile_type_at(self.x + 14, self.y)

        if (right_bottom != 0 or right_top != 0):
            self.x -= 1
            self.hit_wall_right()

    def is_not_on_ground(self):
        left_foot = self.get_tile_type_at(self.x, self.y + 17)
        right_foot = self.get_tile_type_at(self.x + 10, self.y + 17)

        if (left_foot != 0 or right_foot != 0) and self.vy >= 0:
            return False
        else:
            return True

    def not_hit_head(self):
        right_head = self.get_tile_type_at(self.x + 10, self.y)
        left_head = self.get_tile_type_at(self.x, self.y)

        if (right_head != 0 or left_head != 0):
            return False
        else:
            return True
        

    def move(self, velocity: int):
        self.x += velocity
        self.x = min(self.x, 238)
        self.x = max(self.x, 0)
        

    def get_tile_type_at(self, screen_x, screen_y):
        return pyxel.tilemap(2).get((screen_x - self.map.x) // 8, (screen_y // 8) + 66)

    def entity_jump(self):
        self.vy = self.jump_speed

    def accelerate(self, gravity: int):
        self.vy += gravity
        self.y += self.vy

    def move_y(self):
        if self.is_not_on_ground():
            self.accelerate(self.gravity)
            if not self.not_hit_head():
                mario_head = self.y
                self.vy = 0
                self.y = ((mario_head) - ((mario_head) % 16)) + self.h

        else:
            if not self.is_not_on_ground():
                mario_feet = self.y + 17
                self.vy = 0
                self.y = ((mario_feet) - ((mario_feet) % 16)) - self.h
                if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_SPACE):
                    self.entity_jump()

    def move_x(self):

        if pyxel.btn(pyxel.KEY_RIGHT):
            if self.x < 165:
                self.sprite = (0, 0, 48, 16, 16)
                self.move(3)

            if self.x >= 165:
                self.move(0)
                self.map.move(-3)

            self.hit_wall_right()

        elif pyxel.btn(pyxel.KEY_LEFT):
            self.sprite = (0, 0, 48, -16, 16)
            self.move(-3)

            self.hit_wall_left()

    def mario_shoot(self):

        if self.sprite == (0, 0, 48, 16, 16):
            if pyxel.btnp(pyxel.KEY_F):
                self.fireball.fire(self.x, self.y)
                if self.fireball.y >= 208:
                    pass
            self.fireball.update_pve()

        if self.sprite == (0, 0, 48, -16, 16):
            if pyxel.btnp(pyxel.KEY_F):
                self.fireball.fire(self.x + (16 - 8) / 2, self.y - 8 / 2)
                if self.fireball.y >= 208:
                    pass
            self.fireball.update_nve()

    def update(self):
        self.move_y()

        self.move_x()

        self.mario_shoot()

        self.map.detect_collision(self)

    def draw(self):

        pyxel.blt(self.x, self.y, self.sprite[0],
                  self.sprite[1], self.sprite[2], self.sprite[3], self.sprite[4], 12)

        pyxel.blt(self.fireball.x, self.fireball.y, self.fireball.sprite[0],
                  self.fireball.sprite[1], self.fireball.sprite[2], self.fireball.sprite[3], self.fireball.sprite[4], 12)
