class Solution {
public:
    string removeDuplicateLetters(string s) {
        
        
        stack<char> st;
        
        int count[26] = {0};
        
        for(auto c : s)
        {
            count[c - 'a']++;
        }
        
        bool existed[26] = {false};
        for(auto c : s)
        {
            if(!existed[c - 'a'])
            {
                while( !st.empty() && st.top() > c && count[st.top()-'a'] > 0 )
                {
                    existed[st.top() - 'a'] = false;
                    st.pop();
                }
                
                st.push(c);
            }
            
            existed[c - 'a'] = true;
            count[c - 'a']--;
        }
        
        s = "";
        while(!st.empty())
        {
            s += st.top();
            st.pop();
        }
        
        reverse(s.begin(), s.end());
        
        return s;
        
    }
};