import pygame
from config import *
from grid import create_grid
from aco import ACO

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ACO Path Planning")

grid = create_grid(ROWS, COLS)

start = (0, 0)
goal = (ROWS-1, COLS-1)

aco = ACO(grid)
path = aco.run(start, goal)

# Simulate car movement along the path
car_index = 0


# PHASE 1: Basic visualization of grid and path

# def draw():
#     screen.fill(WHITE)

#     for i in range(ROWS):
#         for j in range(COLS):
#             rect = (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE)

#             if grid[i][j] == 1:
#                 pygame.draw.rect(screen, BLACK, rect)
#             else:
#                 pygame.draw.rect(screen, GREY, rect, 1)

#     for (x, y) in path or []:
#         pygame.draw.rect(screen, BLUE, (y*CELL_SIZE, x*CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     pygame.draw.rect(screen, GREEN, (start[1]*CELL_SIZE, start[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
#     pygame.draw.rect(screen, RED, (goal[1]*CELL_SIZE, goal[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     pygame.display.update()


# running = True
# while running:
#     draw()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#pygame.quit()

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------
# PHASE 2: Add car movement simulation

# def draw():
#     screen.fill(WHITE)

#     # Draw grid
#     for i in range(ROWS):
#         for j in range(COLS):
#             rect = (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE)

#             if grid[i][j] == 1:
#                 pygame.draw.rect(screen, BLACK, rect)
#             else:
#                 pygame.draw.rect(screen, GREY, rect, 1)

#     # Draw full path (optional light color)
#     for (x, y) in path or []:
#         pygame.draw.rect(screen, (173, 216, 230), (y*CELL_SIZE, x*CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     # Draw car (moving)
#     if path:
#         x, y = path[car_index]
#         pygame.draw.rect(screen, BLUE, (y*CELL_SIZE, x*CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     # Start and Goal
#     pygame.draw.rect(screen, GREEN, (start[1]*CELL_SIZE, start[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
#     pygame.draw.rect(screen, RED, (goal[1]*CELL_SIZE, goal[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

#     pygame.display.update()

# # Main loop with car movement
# clock = pygame.time.Clock()

# running = True
# while running:
#     clock.tick(5)  # controls speed (increase for faster car)

#     draw()

#     if path and car_index < len(path) - 1:
#         car_index += 1

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

# #
# if car_index == len(path)-1:
#     print("Reached Destination!")
# #

#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

#PHASE 3 : Dynamic obstacles and re-routing 

def draw():
    screen.fill(WHITE)

    # Draw grid
    for i in range(ROWS):
        for j in range(COLS):
            rect = (j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if grid[i][j] == 1:
                pygame.draw.rect(screen, BLACK, rect)
            else:
                pygame.draw.rect(screen, GREY, rect, 1)

    # Draw full path 
    for (x, y) in path or []:
        pygame.draw.rect(screen, (173, 216, 230), (y*CELL_SIZE, x*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw car (moving)
    if path:
        x, y = path[car_index]
        pygame.draw.rect(screen, BLUE, (y*CELL_SIZE, x*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Start and Goal
    pygame.draw.rect(screen, GREEN, (start[1]*CELL_SIZE, start[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (goal[1]*CELL_SIZE, goal[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

    if no_path:
        font = pygame.font.SysFont(None, 40)
        text = font.render("NO PATH!", True, (255, 0, 0))
        screen.blit(text, (200, 250))

    pygame.display.update()

# Main loop with car movement
clock = pygame.time.Clock()

no_path = False
running = True
recalculate = False
reached = False

aco = ACO(grid)
path = aco.run(start, goal)

# ✅ Handle initial case
if not path:
    no_path = True

while running:
    clock.tick(5)  # controls speed (increase for faster car)

    draw()

    if path and not no_path and car_index < len(path) - 1:
        car_index += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            row = my // CELL_SIZE
            col = mx // CELL_SIZE

            if (row, col) != start and (row, col) != goal:
                grid[row][col] = 1  # add obstacle
                recalculate = True

    if recalculate and path:
        #current_pos = path[car_index]
        current_pos = start if not path else path[car_index]
        aco = ACO(grid)
        new_path = aco.run(current_pos, goal)

        if new_path:
           path = new_path
           car_index = 0
           no_path = False #to show no path on screen 
        else:
            #print("No path found") # just printing on console
            path = None 
            no_path = True


        recalculate = False

#
if path and car_index == len(path) - 1:
    reached = True
    print("Reached Destination!")

            
if not reached :
    print("Simulation Ended without reaching destination.")
#
