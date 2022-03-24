class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        
        
        
        map<int, int> dict;
        
        for(auto w : people)
        {
            if(dict.find(w) == dict.end())
            {
                dict[w] = 1;
            }
            else
            {
                dict[w]++;
            }              
        }
        
        //find heaviest one and try to find the other person whos weight is smaller than and closest to remained weight
        
        int boats = 0;
        
        while(dict.size() > 0)
        {
            boats++;
            int w = std::prev(dict.end())->first;
            
            //cout << "Try to remove " << w << endl;
            dict[w]--;
            if(dict[w] == 0) dict.erase(w);
            
            //try to find if someone fit?
            
            if(dict.size() == 0) break;
            
            map<int, int>::iterator it = dict.upper_bound(limit-w);
            
            if(it != dict.begin())
            {
                it--;    
                //cout << "found suitable " << it->first << endl;
                dict[it->first]--;
                if(dict[it->first] == 0)
                {
                    dict.erase(it);
                }
            }
            
            
        }
        
        
        return boats;
        
    }
};