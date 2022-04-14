class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        w_idx = 0
        a_idx = 0
        while w_idx < len(word) and a_idx < len(abbr):
            digit = ""
            while a_idx < len(abbr) and abbr[ a_idx ].isdigit():
                digit += abbr[ a_idx ]
                a_idx += 1
            
            
            
            if digit:
                #skip
                if digit[0] == '0':
                    return False
                w_idx += int(digit)
            else:
                #compare 
                #print(abbr[ a_idx ], word[ w_idx ])
                if abbr[ a_idx ] != word[ w_idx ]:
                    return False
                w_idx += 1
                a_idx += 1
            
            
        
                
        return a_idx == len(abbr) and w_idx == len(word)