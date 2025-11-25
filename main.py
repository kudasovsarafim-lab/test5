from pygame import *

window = display.set_mode((900, 800))
display.set_caption('Peng-pong')

game = True
timer = time.Clock()

while game:
    window.fill((200, 200, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    timer.tick(60)
    