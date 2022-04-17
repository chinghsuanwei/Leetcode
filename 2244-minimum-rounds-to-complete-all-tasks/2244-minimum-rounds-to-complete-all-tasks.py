class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = {}
        
        for item in tasks:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
                
        res = 0
        for key in freq:
            
            val = freq[key]
            if val == 1:
                return -1
            elif val == 2:
                res += 1
            else:
                # 3, 4
                if val % 3 == 1:
                    val -= 4
                    res += 2
                elif val % 3 == 2:
                    val -= 2
                    res += 1
                    
                res += val // 3
                
        return res