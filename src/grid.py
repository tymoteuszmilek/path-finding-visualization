from box import Box as Box

def createGrid(columns, rows):
    grid = []
    for x in range(columns):
        arr = []
        for y in range(rows):
            arr.append(Box(x, y))
        grid.append(arr)
    return grid

def neighbourListGenerator(grid, columns, rows):
    for i in range(columns):
        for j in range(rows):
            grid[i][j].setNeigbours(grid, columns, rows)