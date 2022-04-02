class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> dict = new HashSet<Character>();
        int max = 0;
        int count = 0;
         for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if( !dict.contains(c) ){
                dict.add(c);
                count++;
                if(count > max){
                    max = count;
                }
            }
            else{
                for(int j=i-count; j<i; j++){
                    char oldC = s.charAt(j); 
                    
                    if(oldC != c){
                        dict.remove(oldC);
                        count--;
                    }
                    else{
                        //System.out.println("oldC = " + oldC + ", count = " + count);
                        break;
                    }
                }
            }
        }
        
        return max;
    }
}