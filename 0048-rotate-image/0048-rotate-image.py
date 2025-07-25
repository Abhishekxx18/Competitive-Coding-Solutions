class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(i+1,col):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        for i in range(row):
            for j in range(col//2):
                matrix[i][j],matrix[i][col-j-1] = matrix[i][col-j-1] , matrix[i][j]
        
