import copy
class MatrixAnalysis:
    #all matrices must be rectangular
    @staticmethod
    def row_reduce(matrix1):
        """
        Outputs Matrix in Row Reduced Echelon Format.
        """
        inputMatrix = copy.deepcopy(matrix1)
        for rownum in range(len(inputMatrix)):
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
        """
        Transposes matrix(rows to columns columns to rows)
        """
        new_matrix=[([0] * len(matrix1)) for _ in range(len(matrix1[0]))]
        for row in range(len(matrix1)):
            for col in range(len(matrix1[row])):
                new_matrix[col][row] = matrix1[row][col]
        return new_matrix

    @staticmethod
    def cofactor(matrix1):
        """
        Creates a cofactor matrix(checkerboard signs)
        """
        result = [[matrix1[row][col] * pow(-1,(row+col)) for col in range(len(matrix1[row]))] for row in range(len(matrix1))]
        return result
    
    @staticmethod
    def flatten(matrix1):
        """
        Flattens Matrix/Turns N-Dimension Matrix to 1-Dimension Matrix. Does not sort.
        """
        flat_matrix = [matrix1[row][col] for row in range(len(matrix1)) for col in range(len(matrix1[row]))]
        return flat_matrix

    #needs a check
    @staticmethod
    def determinant(matrix1):
        """
        Finds Determinant of a matrix. Requires a NxN square Matrix where N>1.
        """
        determinant
        if len(matrix1)>2:
            for item in range(len(matrix1[0])):
                relevant_matrix = copy.deepcopy(matrix1)
                relevant_matrix.pop(0)
                for row in range(len(relevant_matrix)):
                    relevant_matrix[row].pop(item)
                determinant+=MatrixAnalysis.determinant(relevant_matrix)*matrix1[0][item]*pow(-1,item)
        elif len == 2:
            determinant = matrix1[0][0]*matrix1[1][1]-matrix1[0][1]*matrix1[1][0]
        else:
            determinant = "Unable to calculate Matrix. Ensure the dimensions of your matrix are greater than 1."
        return determinant

    #needs a check
    @staticmethod
    def inverse(matrix1, multiplyDet=True):
        """
        Finds the inverse of the provided matrix. Requires a square Matrix.
        """
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
                    for row_nest in range(len(relevant_matrix)):
                        relevant_matrix[row_nest].pop(col)
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
    
    #needs a check
    @staticmethod
    def dot(vector1, vector2):
        """Finds dot product of vectors. Vectors must be the same length."""
        result=[vector1[item]*vector2[item] for item in range(len(vector1))]
        return sum(result)

    #needs a check
    @staticmethod
    def add(matrix1, matrix2):
        """Adds Matrices. Matrices must be identical."""
        result = [[matrix1[row][col] + matrix2[row][col] for col in range(len(matrix1[row]))] for row in range(len(matrix1))]
        return result
    
    #needs a check
    @staticmethod
    def subtract(matrix1, matrix2):
        """Subtracts Matrices. Matrices must be identical."""
        result = [[matrix1[row][col] - matrix2[row][col] for col in range(len(matrix1[row]))] for row in range(len(matrix1))]
        return result
    
    @staticmethod
    def scale(matrix1, scalar):
        """Multiplies Matrix by a scalar. (Works on any 2d array even non-rectangular ones so long as every entry is a number)"""
        result = [[matrix1[row][col]*scalar for col in range(len(matrix1[row]))] for row in range(len(matrix1))]
        return result
    
    #needs a check
    @staticmethod
    def matrix_multiply(matrix1,matrix2):
        """Multiplies two matrices. Matrix1 must be an MxN matrix and Matrix2 must be an NxO matrix. Resulting Matrix will be MxO."""
        matrix2_adjust = MatrixAnalysis.transpose(matrix2)
        result = [[MatrixAnalysis.dot(matrix1[row],matrix2_adjust[row2]) for row2 in range(len(matrix2_adjust))] for row in range(len(matrix1))]
        return result
    
    @staticmethod
    def print_matrix(matrix1):
        """Prints Matrices more legibly"""
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

linear_dep = [
    [1,0,-3,0,0,1],
    [1,8,-5,-2,0,2],
    [1,6,-6,0,-1,4],
    [3,7,-7,-1,-2,3]
]
vector=[1,2,3]
vectore=[2,3,4]

test = [[1,2,3],
        [3,2,1],
        [2,1,3]]

test1 = [[2,1],
        [1,3]]
MatrixAnalysis.print_matrix(MatrixAnalysis.row_reduce(linear_dep))
#MatrixAnalysis.print_matrix(MatrixAnalysis.add(matrix,matrixe))
#MatrixAnalysis.print_matrix(MatrixAnalysis.subtract(matrix,matrixe))
# print(MatrixAnalysis.flatten(matrix))
# MatrixAnalysis.print_matrix(MatrixAnalysis.transpose(matrix))
#print(MatrixAnalysis.dot(vector,vectore))
# print(MatrixAnalysis.determinant(test))
#MatrixAnalysis.print_matrix(MatrixAnalysis.scale(test,2))
#MatrixAnalysis.print_matrix(MatrixAnalysis.cofactor(test))
#MatrixAnalysis.print_matrix(MatrixAnalysis.matrix_multiply(matrix,test))
#res, det = MatrixAnalysis.inverse(test1,False)
#MatrixAnalysis.print_matrix(res)
#print("1/" + str(det))
