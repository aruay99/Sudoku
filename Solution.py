def solve(cells):
    find = find_empty(cells)
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if valid(cells,i,(row,col)):
            cells[row][col]=i
            if solve(cells):
                return True
            cells[row][col]=0
    return False


def valid(cells, num,pos):
    for i in range(len(cells[0])):
        if cells[pos[0]][i]==num and pos[1]!=i:
            return False
    for i in range(len(cells)):
        if cells[i][pos[1]]==num and pos[0]!=i:
            return False
    box_x=pos[1]//3
    box_y = pos[0]//3
    for i in range(box_y*3,box_y*3+3):
        for j in range(box_x*3,box_x*3+3):
            if cells[i][j]==num and (i,j)!=pos:
                return False
    return True


def find_empty(cells):
    for i in range(len(cells)):
        for j in range(len(cells[0])):
            if cells[i][j]==0:
                return(i,j)
    return None

def sudoku_solver(board):
    solve(board)
    return board

