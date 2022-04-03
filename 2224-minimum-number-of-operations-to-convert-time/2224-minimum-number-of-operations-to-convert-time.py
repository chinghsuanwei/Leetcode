class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        start = int(current[0:2])*60 + int(current[3:5])
        
        
        end = int(correct[0:2])*60 + int(correct[3:5])
        
        
        diff = end - start
        
        ans = 0
        
        ans += diff // 60
        diff %= 60
        
        ans += diff // 15
        diff %= 15
        
        ans += diff // 5
        diff %= 5
        
        ans += diff
        
        return ans
        
        