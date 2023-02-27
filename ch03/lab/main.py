
import pygame
import random
import math
pygame.init()

screen_size = pygame.display.get_window_size()
screen = pygame.display.set_mode(screen_size)

background_color = (255, 255, 255)
board_color = (0, 0, 0)
miss_color = (255, 0, 0)
hit_color = (0, 255, 0)

board_radius = min(screen_size) // 2
board_center = (screen_size[0] // 2, screen_size[1] // 2)
running = True
while running:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    screen.fill(background_color)


    pygame.draw.circle(screen, board_color, board_center, board_radius, 10)  # outer circle
    pygame.draw.circle(screen, background_color, board_center, board_radius - 10)  # inner circle
    for i in range(0, 360, 18):
        start_pos = (board_center[0] + int(0.8 * board_radius * math.cos(math.radians(i))),
                     board_center[1] + int(0.8 * board_radius * math.sin(math.radians(i))))
        end_pos = (board_center[0] + int(board_radius * math.cos(math.radians(i))),
                   board_center[1] + int(board_radius * math.sin(math.radians(i))))
        pygame.draw.line(screen, board_color, start_pos, end_pos, 10)  # radial lines


    for _ in range(10):
    
        dart_x = random.randrange(screen_size[0])
        dart_y = random.randrange(screen_size[1])

   
        distance_from_center = math.hypot(dart_x - board_center[0], dart_y - board_center[1])
        if distance_from_center <= board_radius - 10:
        
            pygame.draw.circle(screen, hit_color, (dart_x, dart_y), 2)
        else:
           
            pygame.draw.circle(screen, miss_color, (dart_x, dart_y), 2)

 
    pygame.display.flip()


pygame.quit()