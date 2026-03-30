class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = {}
        s2_map = {}

        # Populate initial hashmaps for the first window
        for char_code in range(ord('a'), ord('z') + 1):
            s1_map[chr(char_code)] = 0
            s2_map[chr(char_code)] = 0

        for i in range(len(s1)):
            s1_map[s1[i]] = s1_map[s1[i]] + 1
            s2_map[s2[i]] = s2_map[s2[i]] + 1
        
        matches = 0
        for char in s1_map:
            if s1_map[char] == s2_map[char]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:  # Still 26 because we are tracking all lowercase English letters
                return True

            # Add the new character at 'r'
            char_r = s2[r]
            s2_map[char_r] += 1

            if s1_map[char_r] == s2_map[char_r]:
                matches += 1
            elif s1_map[char_r] + 1 == s2_map[char_r]:
                matches -= 1

            # Remove the character at 'l'
            char_l = s2[l]
            s2_map[char_l] -= 1

            if s1_map[char_l] == s2_map[char_l]:
                matches += 1
            elif s1_map[char_l] - 1 == s2_map[char_l]:
                matches -= 1
            
            l += 1

        return matches == 26