class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        res = []

        _chr = chr
        _int = int
        _len = len
        target_len = _len(digits)

        def backtrack(i, path):
            if i == target_len:
                res.append(path)
                return

            d_int = _int(digits[i])
            
            diff = d_int - 2
            start_ord = 97 + (diff + (diff << 1))

            if d_int > 7:
                start_ord += 1

            count = 4 if (d_int == 7 or d_int == 9) else 3
            
            for j in range(count):
                backtrack(i + 1, path + _chr(start_ord + j))

        backtrack(0, '')
        return res
