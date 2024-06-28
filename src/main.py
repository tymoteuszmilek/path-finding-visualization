import pygame
from grid import createGrid as createGrid
from grid import neighbourListGenerator as neighbourListGenerator
from utils import display_message as display_message

# Adjust As Needed
columns = 30
rows = 30
boxSize = 20
fps = 200
backGroundColor = '#535A53'  # Grey-ish
defaultBlockColor = '#000000'  # Black
startColor = '#FF00FF'  # Magenta
targetColor = '#E4D00A'  # Citrine
wallColor = '#696969'  # Dim Gray
visitedColor = '#32CD32'  # Lime Green
queuedColor = '#DC143C'  # Crimson
pathColor = '#1E90FF'  # Dodger Blue

# Do Not Modify
windowWidth = columns * boxSize
windowHeight = rows * boxSize
boxWidth = windowWidth // columns
boxHeight = windowHeight // rows
queue = []
path = []

# Create Main Grid
mainGrid = createGrid(columns, rows)

# Neighbour List Generator
neighbourListGenerator(mainGrid, columns, rows)


def main():
    beginSearch = False
    startBoxSet = False
    targetBoxSet = False

    pygame.init()
    screen = pygame.display.set_mode((windowWidth, windowHeight))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Draw wall
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                i = x // boxWidth
                j = y // boxWidth
                if event.buttons[0]:
                    mainGrid[i][j].wall = True
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                i = x // boxWidth
                j = y // boxWidth
                mainGrid[i][j].wall = True

            # Set Start
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not startBoxSet:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                i = x // boxWidth
                j = y // boxWidth
                mainGrid[i][j].start = True
                mainGrid[i][j].queued = True
                startBoxSet = True
                queue.append(mainGrid[i][j])

            # Set Target
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3 and not targetBoxSet:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                i = x // boxWidth
                j = y // boxWidth
                mainGrid[i][j].target = True
                targetBoxSet = True
                searching = True

            # Start Algorithm
            if event.type == pygame.KEYDOWN and targetBoxSet:
                beginSearch = True

        # Perform Search
        if beginSearch:
            if len(queue) > 0 and searching:
                currBox = queue.pop(0)
                currBox.visited = True
                if currBox.target:
                    searching = False
                    while not currBox.prior.start:
                        path.append(currBox.prior)
                        currBox = currBox.prior
                else:
                    neighbours = currBox.neighbours
                    for neighbour in neighbours:
                        # BFS In Action
                        if not neighbour.visited and not neighbour.queued and not neighbour.wall:
                            queue.append(neighbour)
                            neighbour.queued = True
                            neighbour.prior = currBox
            else:
                if searching:
                    display_message('No Solution')
                    searching = False

        # Color Boxes and Background
        screen.fill(backGroundColor)
        for x in range(columns):
            for y in range(rows):
                box = mainGrid[x][y]
                if box.start:
                    box.draw(screen, startColor, boxWidth, boxHeight)
                elif box.target:
                    box.draw(screen, targetColor, boxWidth, boxHeight)
                elif box in path:
                    box.draw(screen, pathColor, boxWidth, boxHeight)
                elif box.visited:
                    box.draw(screen, visitedColor, boxWidth, boxHeight)
                elif box.queued:
                    box.draw(screen, queuedColor, boxWidth, boxHeight)
                elif box.wall:
                    box.draw(screen, wallColor, boxWidth, boxHeight)
                else:
                    box.draw(screen, defaultBlockColor, boxWidth, boxHeight)

        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
main()
