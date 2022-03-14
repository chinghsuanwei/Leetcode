class Solution {
public:
    string simplifyPath(string path) {
        stack<string> st;
        
        
        path += "/";
        
        string name;
        for(auto c : path)
        {
            if(c == '/')
            {
                if(name.length() > 0)
                {
                    if(name == ".")
                    {
                        //donothing
                    }
                    else if(name == "..")
                    {
                        if( !st.empty() ) st.pop();
                    }
                    else
                    {
                        st.push(name);
                    }
                    
                    name = "";
                }
            }
            else
            {
                name += c;
            }
        }
        
        string ans;
        
        stack<string> reverse_st;
        
        while(st.size() > 0)
        {
            reverse_st.push( st.top() );
            st.pop();
        }
        
        while(reverse_st.size() > 0)
        {
            ans += "/";
            ans += reverse_st.top();
            reverse_st.pop();
        }
        
        
        
        return ans.length() == 0? "/" : ans;
    }
};