import pygame

pygame.init()
surface = pygame.display.set_mode()

surface.fill("blue")
pygame.display.flip()

radius = 50
center1 = (200, 100)
center2 = (200, 200)
center3 = (200, 300)
pygame.draw.circle(surface, "red", center1, radius)
pygame.draw.circle(surface, "red", center2, radius + 25)
pygame.draw.circle(surface, "red", center3, radius + 50)

pygame.time.wait(500)

