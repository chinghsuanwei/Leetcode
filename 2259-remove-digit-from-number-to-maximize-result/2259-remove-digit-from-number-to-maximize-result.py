class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        
        #bruteforce
        q = []
        
        for i,c in enumerate(number):
            if c == digit:
              q.append(number[0:i] + number[i+1:])
        
        res = "0"
        for s in q:
            res = max(res, s)
        
        return res