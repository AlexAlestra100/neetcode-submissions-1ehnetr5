class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowL = 0
        rowR = len(matrix) - 1

        while rowL <= rowR:
            rowM = ((rowR - rowL) // 2) + rowL

            if matrix[rowM][-1] < target:
                rowL = rowM + 1
            elif matrix[rowM][0] > target:
                rowR = rowM - 1
            else:
                l = 0
                r = len(matrix[rowM]) - 1

                while l <= r:
                    m = ((r - l) // 2) + l

                    if matrix[rowM][m] < target:
                        l = m + 1
                    elif matrix[rowM][m] > target:
                        r = m - 1
                    else: 
                        return True

                return False

        return False