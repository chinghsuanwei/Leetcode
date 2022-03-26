class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& mat1, vector<vector<int>>& mat2) {
        //brute force way to solve it
        
        int m = mat1.size();
        int k = mat1[0].size();
        int n = mat2[0].size();
        
        vector<vector<int>> ans(m, vector<int>(n));
        
        for(int r=0; r<m; r++)
        {
            for(int c=0; c<n; c++)
            {
                
                    for(int i=0; i<k; i++)
                    {
                        //0 0   0 0
                        //0 1   1 0
                        //0 2   2 0
                        
                        //0 0   0 1
                        // ..
                        //
                        
                        
                        ans[r][c] += mat1[r][i] * mat2[i][c];
                    }
                    
                
                
                
            }
        }
        
        return ans;
    }
};