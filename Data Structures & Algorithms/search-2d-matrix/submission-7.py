class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lArr = 0
        rArr = len(matrix) - 1

        mainArr = None

        while lArr <= rArr:
            mArr = lArr + ((rArr - lArr) // 2)

            if target < matrix[mArr][0]:
                rArr = mArr - 1
            elif target > matrix[mArr][-1]:
                lArr = mArr + 1
            else:
                mainArr = matrix[mArr]
                break

        if lArr > rArr:
            return False

        l = 0
        r = len(mainArr) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if mainArr[m] < target:
                l = m + 1
            elif mainArr[m] > target:
                r = m - 1
            else:
                return True

        return False