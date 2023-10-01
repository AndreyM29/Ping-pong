from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((700, 500))
display.set_caption('Пинг-понг')

back = (45, 207, 147)
window.fill(back)

game = True 
clock = time.Clock()
FPS = 60
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)