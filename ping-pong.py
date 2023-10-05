from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

win_width = 470
win_height = 500
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')

back = (45, 207, 147)
window.fill(back)

ball = GameSprite('ball.png', 200, 100, 3, 60, 60)

platform_1 = Player('platform.png', 550, 200, 3, 70, 100)

platform_2 = Player('platform.png', 100, 200, 3, 70, 100)

font.init()
font_1 = font.Font(None, 35)
lose_1 = font_1.render('PLAYER 1 LOSE!', True, (100,0,0))
font_2 = font.Font(None, 35)
lose_2 = font_2.render('PLAYER 2 LOSE!', True, (100,0,0))

speed_x = 3
speed_y = 3

game = True
finish = False 
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)

        ball.rect.x += speed_x
        ball.rect.y += speed_y 

        platform_1.update_r()
        platform_2.update_l()

        platform_1.reset()
        platform_2.reset()
        ball.reset()

        if sprite.collide_rect(platform_1, ball) or sprite.collide_rect(platform_2, ball):
            speed_x *= -1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose_1, (200,200))
        if ball.rect.x > 640:
            finish = True
            window.blit(lose_2, (200,200))

    display.update()
    clock.tick(FPS)
