import pygame

class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.start = False
        self.target = False
        self.wall = False
        self.visited = False
        self.queued = False
        self.neighbours = []
        self.prior = None

    def draw(self, window, blockColor, boxWidth, boxHeight):
        rect = pygame.Rect(self.x * boxWidth, self.y * boxHeight, boxWidth - 2, boxHeight - 2)
        pygame.draw.rect(window, blockColor, rect)

    def setNeigbours(self, grid, columns, rows):
        if self.x > 0:
            self.neighbours.append(grid[self.x - 1][self.y])
        if self.x < columns - 1:
            self.neighbours.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y - 1])
        if self.y < rows - 1:
            self.neighbours.append(grid[self.x][self.y + 1])