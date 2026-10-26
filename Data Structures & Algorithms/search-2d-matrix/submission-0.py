class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix) #nbre de lignes
        n = len(matrix[0]) #nbre de colonnes

        lo = 0
        hi = (m*n) - 1


        while lo <= hi:

            mid = lo + (hi - lo)//2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                lo = mid + 1
            elif matrix[row][col] > target:
                hi = mid - 1
        
        return False

        