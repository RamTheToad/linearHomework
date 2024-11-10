class MatrixAnalysis:
    initialMatrix = [1]
    rrefMatrix = [0]

    def __init__(self, inputMatrix):
        self.initialMatrix=inputMatrix
        self.rrefMatrix = self.row_reduce(self.initialMatrix)

    def row_reduce(self, inputMatrix):
        for rownum in range (len(inputMatrix)):
            pivot = 0
            pivot_colnum = "WAIT"
            for colnum in range(len(inputMatrix[rownum])):
                if pivot == 0:
                    pivot = inputMatrix[rownum][colnum]
                if pivot != 0:
                    if pivot_colnum == "WAIT": pivot_colnum = colnum
                    #divide everything by the pivot
                    inputMatrix[rownum][colnum] = inputMatrix[rownum][colnum]/pivot
            if pivot_colnum == "WAIT":
                continue
            for nest_rownum in range (len(inputMatrix)):
                #check every row to ensure the pivot alone is the nonzero one(literally)
                if inputMatrix[nest_rownum][pivot_colnum] != 0 and nest_rownum != rownum:
                    scalar = inputMatrix[nest_rownum][pivot_colnum]/inputMatrix[rownum][pivot_colnum]
                    for nest_colnum in range(len(inputMatrix[nest_rownum])):
                        inputMatrix[nest_rownum][nest_colnum] -= inputMatrix[rownum][nest_colnum]*scalar
        return inputMatrix
    
    def print_rref(self):
        for row in self.rrefMatrix:
            print(row)
                        
matrix = [
    [4, -2, 5, -5],
    [-9, 7, -8, 0],
    [-6, 4, 5, 3],
    [5, -3, 8, -4]

]
matrixSolver = MatrixAnalysis(matrix)

matrixSolver.print_rref()