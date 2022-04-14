class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        w_idx = 0
        a_idx = 0
        while w_idx < len(word) and a_idx < len(abbr):
            
            if abbr[ a_idx ] == word[ w_idx ]:
                a_idx += 1
                w_idx += 1
            elif abbr[ a_idx ] == '0':
                return False
            elif abbr[a_idx ].isnumeric():
                
                k = a_idx
                while k < len(abbr) and abbr[ k ].isdigit():
                    k += 1
                
                w_idx += int(abbr[a_idx:k]);
                a_idx = k
            else:
                #not equal
                return False
        
                
        return a_idx == len(abbr) and w_idx == len(word)