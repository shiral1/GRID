#basic A* implementation

def A_star(start: tuple, goal: tuple, h) -> list:
    '''
    Compute the lowest-cost path from start to goal using the A* search algorithm.

    Parameters:
        start: starting grid position (x, y)
        goal: target grid position (x, y)
        h: heuristic function h(current, goal) -> float

    Return:
        path: list of positions for path from start to goal, or None if no path
    '''

    # --- init 
# ----- helper funcs ------
def get_neighbours(x,y):
    pass

def heuristic(pos1,pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])