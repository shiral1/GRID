import pygame
import sys
from settings import COLORS

def main():
    # --- init ---
    pygame.init()

    # --- screen settings ---
    WIDTH = HEIGHT = 800
    FPS = 60

    # --- create display ---
    screen = pygame.display.setmode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()

    # --- main loop ---
    play = True
    while play:
        clock.tick(FPS)

        # --- event handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False

    # --- update ---


    # --- draw ---
    screen.fill(COLOURS("background"))

    pygame.display.flip()                               # displays all drawing at once

    # --- shutdown node ---
    pygame.quit()
    sys.exit()

# ----- mouse input transformer to grid -----
def mouse_to_grid(pos, tile_size):
    """
    taking in position of mouse and converting it in respect to tile size
    Param:
        pos:
    Retunr:
        pos:
    """
    x = pos[0] // tile_size
    y = pos[1] // tile_size
    return (x,y)

# ----- helper func for logic ------
def in_bounds(x, y, grid_width, grid_height):
    return 0 <= x < grid_width and 0 <= y < grid_height

# ----- helper func for display past this point -----
def draw_grid():
    """ """
    pass

def draw_tile(size, type):
    """drawing one tile on grid """
    pass

def draw_path():
    pass

if __name__ == "__main__":
    main()