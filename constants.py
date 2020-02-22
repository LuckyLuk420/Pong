import pygame
# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
game_color = [white, red, green, blue]


# Window
width = 800
height = 700
fps = 60

# Paddle
paddle_speed = height / 60

# Playing field
top = int(height / 7)
half = [int(width / 2), int(height / 2)]
border = [int(width / 80), int(height / 60), int(width - width / 80), int(height - height / 60)]

field = [[border[0], border[1]],
         [border[2], border[1]],
         [border[2], border[3]],
         [border[0], border[3]]]
line_size = 10
