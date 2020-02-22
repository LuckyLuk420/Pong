import pygame as game

from constants import black, white, top, border


class Paddle(game.sprite.Sprite):

    def __init__(self, width, height, color=white):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.width = width
        self.height = height
        # Set background color transparent
        self.image = game.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)
        # Fetch the rectangle of the image
        self.rect = self.image.get_rect()

        # Draw the Paddle
        game.draw.rect(self.image, color, [0, 0, width, height])

    def up(self, pixel=15):
        self.rect.y -= pixel
        if self.rect.y <= top:
            self.rect.y = top

    def down(self, pixel=15):
        self.rect.y += pixel
        if self.rect.y > border[3] - self.height:
            self.rect.y = border[3] - self.height


class AI:

    def __init__(self, paddle):
        self.paddle = paddle

    def move(self, ball, blind=20):
        velocity = (abs(ball.rect.y - (self.paddle.rect.y + (self.paddle.height / 2)))) / 10
        if ball.rect.y + ball.velocity[1] - blind > self.paddle.rect.y + (self.paddle.height / 2):
            self.paddle.rect.y += velocity
            if self.paddle.rect.y > border[3] - self.paddle.height:
                self.paddle.rect.y = border[3] - self.paddle.height
        elif ball.rect.y - ball.velocity[1] + blind < self.paddle.rect.y + (self.paddle.height / 2):
            self.paddle.rect.y -= velocity
            if self.paddle.rect.y <= top:
                self.paddle.rect.y = top
