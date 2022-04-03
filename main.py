from pygame import *

class gameSprite(sprite.Sprite):
    def __init__(self, player_img, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img),(50, 200))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(gameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 295:
            self.rect.y += self.speed

class Player2(gameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 295:
            self.rect.y += self.speed

window = display.set_mode((700,500))
display.set_caption('Пин Понг')
background = transform.scale(image.load("bg.png"),(700,500))
ball = gameSprite('ball.png', 350-80, 250-80, 3)

v_x = 3
v_y = 3


font.init()
font = font.Font(None, 35)
lose_1 = font.render('Player 1  LOSE!!!', True, (180,0,0))
lose_2 = font.render('Player 2  LOSE!!!', True, (180,0,0))

game = True
FPS = 60

player = Player("player.png",10, 250, 5)
player2 = Player2('player.png', 640, 250, 5)

finish = False

while game:
    
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.blit(background,(0, 0))
        
        ball.rect.x += v_x
        ball.rect.y += v_y

        if sprite.collide_rect(player, ball):
            v_x *= -1

        if ball.rect.y < 0 or ball.rect.y > 500 - 80:
            v_y *= -1
        
        if ball.rect.x < 0:
           finish = True
           window.blit(lose_1, (350,250))
        
        if ball.rect.x > 650:
           finish = True
           window.blit(lose_2, (350,250))
        
        
        
        
        
        
        
        
        
        player.reset()
        player.update()
        player2.reset()
        player2.update()
        ball.reset()
        
        display.update()