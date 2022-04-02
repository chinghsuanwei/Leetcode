// #include <vector>

// class bool_array { 
// public:
//     bool *data_;
//      size_t width_;

//      // no assignment or copying
     
     

//      bool_array(size_t y, size_t x) : width_(x) {
//          data_ = new bool[y*x];
//          std::fill_n(data_, y*x, false);
//      }

//      bool &operator()(size_t y, size_t x) { 
//          return data_[y+width_+x];
//      }

//      ~bool_array() { 
//          delete [] data_; 
//      }
// };

// class Solution {
    

// public:
//     string longestPalindrome(string s) {
//         bool_array dp = bool_array(s.length(), s.length());
        
//         string answer;
//         int N = s.length();
//         int index = 1;
//         int len = 1;
//         for(int i=0; i<s.length(); i++){
//             for(int j=0, k=i; k<N; j++, k++){
                
//                 if(i==0){
//                     dp(j,j) = true;
                    
//                 } else if(i==1){
//                     if( s[j] == s[j+1] ){
//                         dp(j,j+1) = true;
//                     }
//                 } else if(dp(j+1,k-1) && s[j] == s[k]){
//                     dp(j,k)  = true;
//                 }
                
//                 if(dp(j,k) ){
//                     index = j;
//                     len = i+1;
//                 }
                
//             }
//         }
        
//         return s.substr(index, len);
//     }
// };

#include <vector>

class Solution {
public:
    string longestPalindrome(string s) {
        vector<vector<bool>> dp;
        for(int i=0; i<s.length(); i++){
            dp.push_back(vector<bool>(s.length(), false));
        }
        
        string answer;
        int N = s.length();
        int index = 0;
        int len = 1;
        for(int i=0; i<s.length(); i++){
            for(int j=0, k=i; k<N; j++, k++){
                
                if(i==0){
                    dp[j][j] = true;
                    
                } else if(i==1){
                    if( s[j] == s[j+1] ){
                        dp[j][j+1] = true;
                    }
                } else if(dp[j+1][k-1] && s[j] == s[k]){
                    dp[j][k] = true;
                }
                
                if(dp[j][k]){
                    index = j;
                    len = i+1;
                }
                
            }
        }
        
        return s.substr(index, len);
    }
};