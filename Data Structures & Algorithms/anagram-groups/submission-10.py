class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            sortS = ''.join(sorted(s))
            if sortS not in res:
                res[sortS] = []

            res[sortS].append(s)

        return list(res.values())