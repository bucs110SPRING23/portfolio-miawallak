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

#Part B
display = pygame.display.set_mode((800, 600))
pygame.init()
def graph_coordinates(threenplus1_iters_dict):
    coordinates = list(threenplus1_iters_dict.items())
    pygame.draw.lines(display, "Purple" , False, coordinates )
    new_display = pygame.transform.flip(display, False, True)
    font = pygame.font.Font(None, 16)
    msg = font.render("Hello", False, "black")
    display.blit(msg, (10, 10))
    width, height = new_display.get_size()
    new_display = pygame.transform.scale(new_display, (width * 5, height *5))
    new_display.blit(new_display, (0, 0)) 
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