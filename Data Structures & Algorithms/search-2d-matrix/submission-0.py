class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binsearch2D():

            l,r = 0, len(matrix[0]) * len(matrix) - 1

            while l <= r:
                m = l + (r - l) // 2
                mrow, mcol = m // len(matrix[0]), m % len(matrix[0])

                if matrix[mrow][mcol] == target:
                    return True
                elif matrix[mrow][mcol] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            return False
        
        return binsearch2D()