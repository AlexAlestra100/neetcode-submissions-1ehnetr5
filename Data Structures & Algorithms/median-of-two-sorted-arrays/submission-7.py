class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        sLen = len(A) + len(B)
        half = sLen // 2

        if A > B:
            A, B = B, A
        
        l = 0
        r = len(A) - 1
        while True:
            mA = l + (r - l) // 2
            mB = half - mA - 2

            lA = A[mA] if mA >= 0 else float('-inf')
            lB = B[mB] if mB >= 0 else float('-inf')

            rA = A[mA + 1] if mA + 1 < len(A) else float('inf')
            rB = B[mB + 1] if mB + 1 < len(B) else float('inf')

            if lA <= rB and lB <= rA:
                if sLen % 2:
                    return min(rA, rB)
                return (max(lA, lB) + min(rA, rB)) / 2
            elif lA > rB:
                r = mA - 1
            else:
                l = mA + 1