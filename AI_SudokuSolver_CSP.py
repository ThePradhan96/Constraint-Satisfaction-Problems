import numpy as np
import random
import time

### basic displaying the sudoku puzzle board 
def print_board(puzzle):
    for row in range(len(puzzle)):
        if row % 3 == 0 and row != 0:
            print("-----------------------")
        for column in range(len(puzzle[0])):
            if column % 3 == 0 and column != 0:
                print(" | ", end ="")
            if column == 8:
                print(puzzle[row][column])
            else:
                print(str(puzzle[row][column]) + " ",end="")

def check_constraints(sudoku, number, row, column):
    ##a conditional statement that checks to see if value
    ##is not  found in any of the rows or columns inside of sudoku
      
    if number not in sudoku[row, :]:
        if number not in sudoku[:,column]:
            ##define where each row or column begins respectively
            rowStart, rowEnd = (0, 3) if row <= 2 else (3,6) if 3 <= row <= 5 else (6,9)
            columnStart, columnEnd = (0, 3) if column <= 2 else (3, 6) if 3 <= column <= 5 else (6, 9)

            ## reduce the domain by removing all values that are not in the given above rangeT
            ###reduces the domain from 9x9 to 3x3
            reducedSudoku = sudoku[rowStart:rowEnd, columnStart:columnEnd]
            if number not in reducedSudoku:
                return True
    return False


def reduce_domain(sudoku, domain, row, column):
    domain = list(filter((lambda x: check_constraints(sudoku, x, row, column) == True) , domain))
    return domain

def get_next_position(row, column):
    column = column + 1 if column < 8 else 0
    row = row + 1 if column == 0 else row

    return (row, column)

def solve(sudoku):
    return sudokuSolver(sudoku, row=0, column=0)

def sudokuSolver(sudoku, row, column):
    #two arguments: the first is the current state of the puzzle,(within which row and col)
    ###$ and the second is an index that starts at 0 and goes up to 9
    if row < 9:
#######create empty list : for temp. storage 
        domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if sudoku[row][column] == 0:
            domain = reduce_domain(sudoku, domain, row, column)

    
            nextSudoku = None

            while nextSudoku is None:
                if len(domain) > 1:
                    ###randomly choose one element out of the list
                    value = domain[random.randint(0, len(domain)-1)]
                elif len(domain) == 1:
                    value = domain[0]
                else:
                    return None
                ## None : either no number exists at all or it's already been solved

                domain.remove(value)
                nextSudoku = sudoku.copy()

                nextSudoku[row][column] = value
                nextRow, nextColumn = get_next_position(row, column)
                nextSudoku = sudokuSolver(nextSudoku, nextRow, nextColumn)
            return nextSudoku
        else:
            row, column = get_next_position(row, column)
            nextSudoku = sudokuSolver(sudoku, row, column)
            return nextSudoku
    else:
        return sudoku

    ####test function takes in a sudoku puzzle as input and checks if all of the constraints are satisfied or not.
def test(sudoku):
    emptylist = []
    for row in range(9):
        for column in range(9):
            emptylist.append(check_constraints(sudoku, sudoku[row][column], row, column))
           

    return (not all(emptylist))
### returns TRUE if there are no constraints found in the list or False otherwise.


############# EASY PUZZLE ###############
sudokueasy = np.array( [[6,0,8,7,0,2,1,0,0],
               [4,0,0,0,1,0,0,0,2],
               [0,2,5,4,0,0,0,0,0],
               [7,0,1,0,8,0,4,0,5],
               [0,8,0,0,0,0,0,7,0],
               [5,0,9,0,6,0,3,0,1],
               [0,0,0,0,0,6,7,5,0],
               [2,0,0,0,9,0,0,0,8],
               [0,0,6,8,0,5,2,0,3]]
               )


###############  HARD PUZZLE   ##################
sudokuhard = np.array([[0,7,0,0,4,2,0,0,0],
               [0,0,0,0,0,8,6,1,0],
               [3,9,0,0,0,0,0,0,7],
               [0,0,0,0,0,4,0,0,9],
               [0,0,3,0,0,0,7,0,0],
               [5,0,0,1,0,0,0,0,0],
               [8,0,0,0,0,0,0,7,6],
               [0,5,4,8,0,0,0,0,0],
               [0,0,0,6,1,0,0,5,0]]
               )

print('The Initial Easy Sudoku board:- \n') 
print_board(sudokueasy)
print ()
print('Satisfies all constraint? :-',(test(sudokueasy)))
start_time = time.time()
print('The final solution of the above Sudoku puzzle - \n')  
print(print_board(solve(sudokueasy)))
print('Total time for solving the Sudoku Puzzle :%s seconds ' % (time.time() - start_time))


print('\n' 'The Initial hard Sudoku board:- \n') 
print_board(sudokuhard)
print ()
print('Satisfies all constraint? :-',(test(sudokuhard)))
start_time1 = time.time()
print('The final solution of the above Sudoku puzzle - \n')  
print(print_board(solve(sudokuhard)))
print('Total time for solving the Sudoku Puzzle :%s seconds ' % (time.time() - start_time1))