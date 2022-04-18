class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        S = set()
        for i,c in enumerate(s):
            if c == ')':
                if len(stack):
                    stack.pop(-1)
                else:
                    S.add(i)
            elif c == '(':
                stack.append(i)
                
        while stack:
            S.add( stack.pop(0) )
            
            
        res = ""
        for i,c in enumerate(s):
            if i not in S:
                res += c
                
        
        return res
                