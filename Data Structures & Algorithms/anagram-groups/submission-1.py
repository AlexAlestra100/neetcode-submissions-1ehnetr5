class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapS = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            mapS[key].append(s)

        return mapS.values()