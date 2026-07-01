class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = []

        m1 = {}
        m2 = {}

        for n in nums1:
            m1[n] = m1.get(n, 0) + 1

        for n in nums2:
            m2[n] = m2.get(n, 0) + 1

        res1 = []
        res2 = []

        for k, v in m1.items():
            if k not in m2:
                res1.append(k)

        for k, v in m2.items():
            if k not in m1:
                res2.append(k)

        return [res1, res2]