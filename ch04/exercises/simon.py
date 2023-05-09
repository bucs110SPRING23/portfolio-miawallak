import random
import pygame

pygame.init()
screen = pygame.display.set_mode()
width, height = screen.get_window_size()

hitbox_width = width / 2
hitbox_height = height / 2

hitboxes = {
    (hitbox_width, hitbox_height),
     "purple": pygame.Rect(hitbox_width,
    hitbox_height, hitbox_width, hitbox_height)

}
