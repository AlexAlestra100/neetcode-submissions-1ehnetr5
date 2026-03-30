class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            sort = ''.join(sorted(s))
            groups.setdefault(sort, []).append(s)

        return list(groups.values())