class Solution {
    public int openLock(String[] deadends, String target) {
        Set<String> seen = new HashSet<>();

        for(String s : deadends)
            seen.add(s);
        if( seen.contains("0000") ) return -1;
        
        seen.add("0000");

        Queue<String> q = new LinkedList<>();
  	    q.add("0000");
        //"0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".

        
        
        int step = 0;
        while(q.size() > 0)
        {
            int size = q.size();

            for(int i=0; i<size; i++)
            {
                String lock = q.poll();

                if(lock.equals(target)) return step;

                // for dir, and +1 -1

                for(int pos=0; pos<4; pos++)
                {
                    StringBuilder sb = new StringBuilder(lock);
                    char c = sb.charAt(pos);

                    char new_c = c == '9'? '0' : (char)(c+1);
                    sb.setCharAt(pos, new_c);

                    String new_lock = sb.toString();
                    //System.out.println(new_lock);
                    if( !seen.contains(new_lock) )
                    {
                        seen.add(new_lock);
                        q.offer(new_lock);
                    }

                    new_c = c == '0'? '9' : (char)(c-1);
                    sb.setCharAt(pos, new_c);

                    //System.out.println(new_lock);
                    new_lock = sb.toString();
                    if( !seen.contains(new_lock) )
                    {
                        seen.add(new_lock);
                        q.offer(new_lock);
                    }

                }
            }

            step++;
        }
  
        return -1;
    }
}