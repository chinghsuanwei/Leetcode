class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        
        sort(people.begin(), people.end());
        
        int i = 0;
        int j = people.size() - 1;
        
        int boats = 0;
        while(i <= j)
        {
            int remain = limit - people[j--];
            if(remain >= people[i]) i++;
            
            boats++;
        }
        
        return boats;
    }
};