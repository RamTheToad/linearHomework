import copy
class MatrixAnalysis:
    #all matrices must be rectangular

    #only works for linearly independent
    @staticmethod
    def row_reduce(matrix1):
        inputMatrix = copy.deepcopy(matrix1)
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
    
    @staticmethod
    def transpose(matrix1):
        new_matrix=[]
        for _ in range(len(matrix1[0])):
            new_matrix.append([0] * len(matrix1))
        for row in range(len(matrix1)):
            for col in range(len(matrix1[row])):
                new_matrix[col][row] = matrix1[row][col]
        return new_matrix

    @staticmethod
    def flatten(matrix1):
        flat_matrix = []
        for row in range(len(matrix1)):
            for col in range(len(matrix1[row])):
               flat_matrix.append(matrix1[row][col])
        return flat_matrix

    @staticmethod
    def determinant(matrix1, matrix2):
        return "In development"

    #requires square matrix with non-zero determinant
    @staticmethod
    def inverse(matrix1, matrix2):
        return "In development"
    
    #only vectors
    @staticmethod
    def dot(vector1, vector2):
        result=[vector1[item]*vector2[item] for item in range(len(vector1))]
        return result
    
    #requires identical matrices
    @staticmethod
    def add(matrix1, matrix2):
        result = [[matrix1[row][col] + matrix2[row][col] 
                   for col in range(len(matrix1[row]))] 
                   for row in range(len(matrix1))]
        return result
    
    #requires identical matrices
    @staticmethod
    def subtract(matrix1, matrix2):
        result = [[matrix1[row][col]-matrix2[row][col] 
                   for col in range(len(matrix1[row]))] 
                   for row in range(len(matrix1))]
        # for row in range(len(matrix1)):
        #     for col in range(len(matrix1[row])):
        #         matrix1[row][col] -= matrix2[row][col]
        return result
    
    #requires mxn and nxo matrices
    @staticmethod
    def matrix_multiply(matrix1,matrix2):
        return "In development"
    
    @staticmethod
    def print_matrix(matrix1):
        for row in matrix1:
            print(row)
    
    
matrix = [
    [1, 2, 3],
    [5, 12, 5]
]
matrixe = [
    [1, 2, 3],
    [5, 12, 6]
]
vector=[1,2,3]
vectore=[2,3,4]

#MatrixAnalysis.print_matrix(MatrixAnalysis.row_reduce(matrix))
MatrixAnalysis.print_matrix(MatrixAnalysis.add(matrix,matrixe))
MatrixAnalysis.print_matrix(MatrixAnalysis.subtract(matrix,matrixe))
#MatrixAnalysis.print_matrix(MatrixAnalysis.flatten(matrix))
#MatrixAnalysis.print_matrix(MatrixAnalysis.transpose(matrix))
#print(MatrixAnalysis.dot(vector,vectore))
