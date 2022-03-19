
// bool compare(vector<int> a, vector<int> b)
// {
//     cout << "compare" << endl;
//     cout << a.size() << endl;
//     cout << b.size() << endl;
//     if(a[0] != b[0])
//         return a[0] > b[0];
    
//     if(a[1] != b[1])
//         return a[1] < b[1];
    
//     return a[2] < b[2];
// }
        

class Solution {

public:    
    
    vector<int> assignBikes(vector<vector<int>>& workers, vector<vector<int>>& bikes) {
        
        
        vector<vector<pair<int, int>>> bucket(2000);
        
        for(int i=0; i<workers.size(); i++)
        {
            for(int j=0; j<bikes.size(); j++)
            {
                //cout << i << endl;
                //cout << j << endl;
                
                
                int dist = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1]);
                
                bucket[ dist ].push_back(make_pair(i, j));
            }
        }
        
        
        
        vector<bool> bikesAssigned( bikes.size() );
        vector<int> ans( workers.size(), -1 );
        
        int count = 0;
        for(int i=0; i<2000 && count < workers.size(); i++)
        {
            for(auto& p : bucket[i])
            {
                int workerIdx = p.first;
                int bikeIdx = p.second;
                
                if( ans[ workerIdx ] == -1 && !bikesAssigned[ bikeIdx ] )
                {
                    bikesAssigned[ bikeIdx ] = true;
                    count++;
                    ans[workerIdx] = bikeIdx;
                }
            }
            
            
            //cout << "worker = " << workerIdx << ",bike = " << bikeIdx << endl;
            
            
        }
        
        
        return ans;
    }
    
};