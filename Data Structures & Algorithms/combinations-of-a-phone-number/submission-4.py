from collections import deque

class Solution:
    # Adding slots is harmless but unlikely to move the needle on LeetCode
    __slots__ = () 

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        # Use a deque for faster appends/pops if the list gets huge
        res = deque([''])
        
        for d in digits:
            # 0 ms Math logic
            start_ord = ord('a') + (int(d) - 2) * 3
            if d in ('8', '9'): start_ord += 1
            count = 4 if d in ('7', '9') else 3
            
            # This is the speed engine (0 ms)
            for _ in range(len(res)):
                prev = res.popleft()
                for i in range(count):
                    res.append(prev + chr(start_ord + i))
        
        return list(res)