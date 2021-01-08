import numpy as np
import sys

sys.setrecursionlimit(10**6) 

input_grid = np.matrix([
[3,0,0,8,0,1,0,0,2],
[2,0,1,0,3,0,6,0,4],
[0,0,0,2,0,4,0,0,0],
[8,0,9,0,0,0,1,0,6],
[0,6,0,0,0,0,0,5,0],
[0,0,2,0,0,0,4,0,9],
[0,0,0,0,0,0,0,0,0],
[9,0,0,0,8,0,0,0,0],
[6,0,0,1,0,0,0,0,3]
])

def placeable(x,y,n,grid):
    for i in range(9):
        if grid[x, i] == n:
            return False #check row for same number
    for j in range(9):
        if grid[j, y] == n: #check collom for same number
            return False
    x_start = (x//3)*3
    y_start = (y//3)*3
    for k in range(3):
        for l in range(3):
            if grid[k + x_start,l + y_start] == n: #check 3x3 grid for same number
                return False
    return True

def solve(grid):
    for y in range(9):
        for x in range(9):
            if grid[x, y] == 0:
                for n in range(1, 10):
                    if placeable(x, y, n, grid):
                        grid[x, y] = n
                        solve(grid)
                        grid[x, y] = 0
                return
    print(grid)
    input("")


solve(input_grid)
