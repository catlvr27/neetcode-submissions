class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            for column in range(len(matrix[0])): #[0] gives us the number of columns okay? think about it, matrix[0] returns the 1st row and then we take uska lenght hence we get number of columns 
                if matrix[row][column] == target:
                    return True
        return False
        