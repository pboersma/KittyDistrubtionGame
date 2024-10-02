from pygame import sprite, image, key
from pygame.locals import *

class Player(sprite.Sprite):
    ACC = 1
    FRIC = -0.12
    BASE_ASSET_PATH = './assets/images/characters/player'

    def __init__(self, vector):
        super().__init__()

        self.vector = vector
        self.playerImage = image.load(f'{Player.BASE_ASSET_PATH}/player_idle.png', 'Player Character - Idle')

        self.moveRight = False
        self.moveLeft = False

        self.moveRightList = [
            image.load(f'{Player.BASE_ASSET_PATH}/player_right_1.png'),
            image.load(f'{Player.BASE_ASSET_PATH}/player_right_2.png'),
            image.load(f'{Player.BASE_ASSET_PATH}/player_right_3.png'),
            image.load(f'{Player.BASE_ASSET_PATH}/player_right_4.png'),
            image.load(f'{Player.BASE_ASSET_PATH}/player_right_5.png'),
            image.load(f'{Player.BASE_ASSET_PATH}/player_right_6.png'),
        ]

        self.pos = vector((10, 385))
        self.vel = vector(0,0)
        self.acc = vector(0,0)
        
    def move(self):
        self.acc = self.vector(0,0)
 
        pressed_keys = key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.moveRight = False
            self.moveLeft = True
            self.acc.x = - Player.ACC
        elif pressed_keys[K_RIGHT]:
            self.moveRight = True
            self.moveLeft = False
            self.acc.x = Player.ACC
        else:
            self.moveRight = False
            self.moveLeft = False

        self.acc.x += self.vel.x * Player.FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > 1280:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = 720
