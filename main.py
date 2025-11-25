from pygame import *

window = display.set_mode((900, 800))
display.set_caption('Peng-pong')

game = True
timer = time.Clock()



class GameSprite(sprite.Sprite):
    def __init__(self, filename, x, y, width=30, height=200):
        super().__init__()
        self.image = transform.scale(image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

player_left = GameSprite('platform.png', 5, 300)
player_right = GameSprite('platform.png', 865, 300)
ball = GameSprite('ball.png', 400, 350, width=100, height=100)

speed_x = 5
speed_y = 5

while game:
    keys = key.get_pressed()
    if keys[K_w] and player_left.rect.y > 0:
        player_left.rect.y -= 10
    if keys[K_s] and player_left.rect.y < 600:
        player_left.rect.y += 10
    if keys[K_UP] and player_right.rect.y > 0:
        player_right.rect.y -= 10
    if keys[K_DOWN] and player_right.rect.y < 600:
        player_right.rect.y += 10

    ball.rect.x += speed_x
    ball.rect.y += speed_y

    if ball.rect.y <= 0 or ball.rect.y >= 700:
        speed_y *= -1

    if sprite.collide_rect(player_left, ball) or sprite.collide_rect(player_right, ball):
        speed_x *= -1

    window.fill((200, 200, 255))
    for e in event.get():
        if e.type == QUIT:
            game = False
    player_left.draw()
    player_right.draw()
    ball.draw()
    display.update()
    timer.tick(60)
