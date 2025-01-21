import math
import pygame
import random

pygame.init()


width = 800
height = 800
running = True

def x_equal_y():
    pygame.display.set_caption("y = x")
    screen_x_equal_y = pygame.display.set_mode((width, height))
    screen_x_equal_y.fill((255, 255, 255))

    while True:
        pixel = random.randint(0, width)
        screen_x_equal_y.set_at((pixel, (800-pixel)), (0, 0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    x_equal_y()