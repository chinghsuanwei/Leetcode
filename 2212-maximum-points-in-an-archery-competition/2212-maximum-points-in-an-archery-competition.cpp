class Solution {
public:
    vector<int> maximumBobPoints(int numArrows, vector<int>& aliceArrows) {
        
        //brute force for 3^10
        
        int max_score = 0; 
        int max_pattern = 0;
        
        
        for(int i=0; i<2048; i++)
        {
            int arrows = numArrows;
            int score = 0;
            for(int j=0; j<11; j++)
            {
                if( (i >> j) & 1 )
                {
                    //mean try to win 1-10
                    
                    arrows -= aliceArrows[j+1] + 1;
                    score += j+1;
                    if(arrows < 0){
                        score = -1;
                        break;
                    }
                }
            }
            
            if(score > max_score)
            {
                max_score = score;
                max_pattern = i;
            }
            
        }
        
        vector<int> ans(12, 0);
        int arrows = numArrows;
        for(int j=0; j<11; j++)
        {
            if( (max_pattern >> j) & 1 )
            {
                ans[j+1] = aliceArrows[j+1] + 1;
                arrows -= aliceArrows[j+1] + 1;
            }
        }
        ans[11] += arrows;
        
        return ans;
    }
};