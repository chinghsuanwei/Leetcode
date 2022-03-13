class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        map<char, char> dict;
        
        dict.insert( pair('(', ')') );
        dict.insert( pair('[', ']') );
        dict.insert( pair('{', '}') );
        
        for(auto c : s)
        {
            if(dict[c])
            {
                st.push( dict[c] );
                
                
                //cout << c << endl;
            }
            else
            {
                if(st.empty() || st.top() != c )  return false;
                st.pop();
            }
        }
        
        return st.size() == 0;
    }
};