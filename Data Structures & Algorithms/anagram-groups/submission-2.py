class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashS = {}

        for s in strs:
            if''.join(sorted(s)) not in hashS:
                hashS[''.join(sorted(s))] = [s]
            else:
                hashS[''.join(sorted(s))].append(s)
        
        return hashS.values()