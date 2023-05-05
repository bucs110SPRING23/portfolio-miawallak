#Part A
import pygame

objs_in_sequence = {}

def threenp1(n):
    count = 0
    while n > 1.0:
       count = count + 1
       if n % 2 == 0:
        n = int(n / 2)
       else:
        n = int(3 * n + 1)
    return count

def threenp1range(upper_limit):
    for i in range(2, upper_limit+1): 
        val = threenp1(i)
        objs_in_sequence[i] = val
    print(objs_in_sequence)
    return objs_in_sequence

#Part B
display = pygame.display.set_mode((800, 600))
pygame.init()
def graph_coordinates(threenplus1_iters_dict):
    display_info = pygame.display.Info()
    screen_width = display_info.current_w
    screen_height = display_info.current_h
    
    coordinates = list(threenplus1_iters_dict.items())
    max_x = max(coordinates, key=lambda x: x[0])[0]
    max_y = max(coordinates, key=lambda x: x[1])[1]
    normalized_coords = [(x / max_x, y / max_y) for x, y in coordinates]
    pixel_coords = [(int(x * screen_width), int(y * screen_height)) for x, y in normalized_coords]
    
    pygame.draw.lines(display, "Purple", False, pixel_coords)
    pygame.display.flip()



def main():
    pygame.init()
    display = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("3n+1 Graph")
    upper_limit = 20
    coords = threenp1range(upper_limit)
    if len(coords) > 1:
        graph_coordinates(coords)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

main()
 