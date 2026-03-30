class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            print(row)
            l, r = 0, len(row) - 1

            if row[l] > target:
                return False
            elif row[r] < target:
                continue
            
            while l <= r:
                m = (l + r) // 2

                print('l:', l, 'r:', r, 'm:', m)
                print('row[m]:', row[m], 'target:', target)

                if row[m] > target:
                    r = m - 1
                elif row[m] < target:
                    l = m + 1
                else:
                    return True
        
        return False