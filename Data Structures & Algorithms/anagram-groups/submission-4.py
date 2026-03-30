class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            sort = ''.join(sorted(s))
            groups[sort].append(s)

        return groups.values()