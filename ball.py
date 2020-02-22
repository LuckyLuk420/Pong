import pygame as game
from constants import black, white, width, height
from random import randint, randrange


class Ball(game.sprite.Sprite):
    def __init__(self, size, color=white):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.size = size

        # Set background color transparent
        self.image = game.Surface([size, size])
        self.image.fill(black)
        self.image.set_colorkey(black)
        # Fetch the rectangle of the image
        self.rect = self.image.get_rect()
        # Set the velocity
        self.velocity = [randint(2, 6), randint(-8, 8)]

        # Draw the Ball
        game.draw.rect(self.image, color, [0, 0, size, size])

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self, paddle=(0, 0)):
        if self.rect.x < width / 2:
            self.rect.x = paddle[0] + paddle[1]
        if self.rect.x > width / 2:
            self.rect.x = paddle - self.size
        # self.rect.x -= int(self.velocity[0])
        self.velocity[0] = (randrange(100, 130, 5) / 100) * -self.velocity[0]
        # TODO bounce angle depends on where the ball hits the paddle
        self.velocity[1] = randint(-8, 8)

    def reset(self):
        self.velocity[0] = (self.velocity[0] / abs(self.velocity[0]) * randint(2, 6))
        self.rect.x = int(width / 2)
        self.rect.y = int(height / 2)
