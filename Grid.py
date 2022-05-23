from tkinter import *

import Solution
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

root = Tk()
root.title("Sudoku Solver")
root.geometry("520x500")
label = Label(root, text = "Fill in the numbers and click solve"). grid(row=0, column=1, columnspan=10)
errLabel =Label(root,text="", fg="red")
errLabel.grid(row=15, column=1, columnspan=10, pady=5)
solvedLabel =Label(root,text="", fg="green")
solvedLabel.grid(row=15, column=1, columnspan=10, pady=5)

def valid_val(P):
    out = (P.isdigit() or P=="") and len(P)<2
    return out
reg = root.register(valid_val)


def drawGrid(board):
    for box in range(len(board)):
        for i in range((len(board[0]))):
            if board[box][i] != 0:
                e = Entry(root, width=5)
                e.configure(state="disabled")
                e.insert(0, str(board[box][i]))

                e.grid(row=box+1, column=i+1)
            else:
                e = Entry(root, width=5, validate="key", validatecommand=(reg, "%P"))
                e.insert(0, "")
                e.grid(row=box+1, column=i+1)




drawGrid(board)








def check_solution():
    answers=[]
    for i in range(9):
        for j in range(9):
            answers[i][j]=

















btn= Button(root, command=lambda: drawGrid(Solution.sudoku_solver(board)), text= "Solve", width=10)
btn= Button(root, command= check_solution(), text= "Check", width=10)

btn.grid(row=20, column=1, columnspan=5, pady=20)

# btn= Button(root, command=getValues, text= "Clear", width=10)
# btn.grid(row=20, column=5, columnspan=5, pady=20)


root.mainloop()








