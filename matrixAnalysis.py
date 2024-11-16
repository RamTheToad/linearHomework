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
        new_matrix=[([0] * len(matrix1)) for _ in range(len(matrix1[0]))]
        for row in range(len(matrix1)):
            for col in range(len(matrix1[row])):
                new_matrix[col][row] = matrix1[row][col]
        return new_matrix

    @staticmethod
    def cofactor(matrix1):
        result = [[matrix1[row][col] * pow(-1,(row+col)) for col in range(len(matrix1[row]))] for row in range(len(matrix1))]
        return result
    @staticmethod
    def flatten(matrix1):
        flat_matrix = [matrix1[row][col] for row in range(len(matrix1)) for col in range(len(matrix1[row]))]
        return flat_matrix

    #requires a square matrix
    @staticmethod
    def determinant(matrix1):
        # print(matrix1)
        determinant = 0
        if len(matrix1)>2:
            for item in range(len(matrix1[0])):
                relevant_matrix = copy.deepcopy(matrix1)
                relevant_matrix.pop(0)
                # print(matrix1)
                for row in range(len(relevant_matrix)):
                    relevant_matrix[row].pop(item)
                    # print(relevant_matrix)
                determinant+=MatrixAnalysis.determinant(relevant_matrix)*matrix1[0][item]*pow(-1,item)
        else:
            # print(matrix1)
            determinant = matrix1[0][0]*matrix1[1][1]-matrix1[0][1]*matrix1[1][0]
            # print(determinant)
        return determinant

    #requires square matrix with non-zero determinant
    @staticmethod
    def inverse(matrix1, multiplyDet=True):
        determinant = MatrixAnalysis.determinant(matrix1)
        if determinant == 0:
            return("No inverse exists; Determinant is 0")
        result = copy.deepcopy(matrix1)
        #Make Matrix of Minors(DONE)
        if len(matrix1)>2:
            for row in range(len(matrix1)):
                for col in range(len(matrix1[row])):
                    relevant_matrix = copy.deepcopy(matrix1)
                    relevant_matrix.pop(row)
                    #print(relevant_matrix)
                    for row_nest in range(len(relevant_matrix)):
                        relevant_matrix[row_nest].pop(col)
                    # relevant_matrix = [relevant_matrix[row].pop(col) for row in range(len(relevant_matrix))]
                    #print(relevant_matrix)
                    result[row][col] = MatrixAnalysis.determinant(relevant_matrix)
        elif len(matrix1)==2:
            result = [[matrix1[(row + 1)%2][(col+1)%2] for col in range(len(matrix1[row]))] for row in range(len(matrix1))]
        else:
            print("bad matrix")
        #Make Cofactors(DONE)
        result = MatrixAnalysis.cofactor(result)
        #Make Adjugate(DONE)
        result = MatrixAnalysis.transpose(result)
        # Multiply by 1/Determinant(DONE)
        if multiplyDet:
            result = MatrixAnalysis.scale(result, 1/determinant)
            return result
        else:
            return result, determinant
    
    #only vectors
    @staticmethod
    def dot(vector1, vector2):
        result=[vector1[item]*vector2[item] for item in range(len(vector1))]
        return sum(result)
    
    #requires identical matrices
    @staticmethod
    def add(matrix1, matrix2):
        result = [[matrix1[row][col] + matrix2[row][col] for col in range(len(matrix1[row]))] for row in range(len(matrix1))]
        return result
    
    #requires identical matrices
    @staticmethod
    def subtract(matrix1, matrix2):
        result = [[matrix1[row][col] - matrix2[row][col] for col in range(len(matrix1[row]))] for row in range(len(matrix1))]
        return result
    
    @staticmethod
    def scale(matrix1, scalar):
        result = [[matrix1[row][col]*scalar for col in range(len(matrix1[row]))] for row in range(len(matrix1))]
        return result
    
    #requires mxn and nxo matrices
    @staticmethod
    def matrix_multiply(matrix1,matrix2):
        matrix2_adjust = MatrixAnalysis.transpose(matrix2)
        result = [[MatrixAnalysis.dot(matrix1[row],matrix2_adjust[row2]) for row2 in range(len(matrix2_adjust))] for row in range(len(matrix1))]
        return result
    
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

test = [[1,2,3],
        [3,2,1],
        [2,1,3]]

test1 = [[2,1],
        [1,3]]
#MatrixAnalysis.print_matrix(MatrixAnalysis.row_reduce(matrix))
#MatrixAnalysis.print_matrix(MatrixAnalysis.add(matrix,matrixe))
#MatrixAnalysis.print_matrix(MatrixAnalysis.subtract(matrix,matrixe))
# print(MatrixAnalysis.flatten(matrix))
# MatrixAnalysis.print_matrix(MatrixAnalysis.transpose(matrix))
#print(MatrixAnalysis.dot(vector,vectore))
# print(MatrixAnalysis.determinant(test))
#MatrixAnalysis.print_matrix(MatrixAnalysis.scale(test,2))
#MatrixAnalysis.print_matrix(MatrixAnalysis.cofactor(test))
#MatrixAnalysis.print_matrix(MatrixAnalysis.matrix_multiply(matrix,test))
res, det = MatrixAnalysis.inverse(test1,False)
MatrixAnalysis.print_matrix(res)
print("1/" + str(det))
