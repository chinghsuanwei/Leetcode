class Encrypter {

    Map<Character, String> en_dict = new HashMap<>();
    Map<String, List<Character>> de_dict = new HashMap<>();
    boolean[][] bucket;
    
    TrieNode _root;
    
    class TrieNode{
        
        Map<Character, TrieNode> children = new HashMap<>();
        boolean isWord;
    }
    
    int max_decrypt_len = 0;
    public Encrypter(char[] keys, String[] values, String[] dictionary) {
        for(int i=0; i<keys.length; i++)
        {
            char c = keys[i];
            en_dict.put(c, values[i]);
            List<Character> list = de_dict.computeIfAbsent(values[i], f -> new ArrayList<>());
            list.add(c);
        }
        
        _root = new TrieNode();
        
        //build
        
        bucket = new boolean[200][26];
        
        for(String s : dictionary)
        {
            max_decrypt_len = Math.max(max_decrypt_len, s.length());
            
            TrieNode node = _root;
            for(int i=0; i<s.length(); i++)
            {
                char c = s.charAt(i);
                bucket[i][c-'a'] = true;
                node = node.children.computeIfAbsent(c, f -> new TrieNode());
            }
            
            node.isWord = true;
        }
    }
    
    public String encrypt(String word1) {
        
        StringBuilder sb = new StringBuilder();
        for(char c : word1.toCharArray())
        {
            sb.append( en_dict.get(c) );
        }
        
        return sb.toString();
    }
    
    public int decrypt(String word2) {
        
        //System.out.println(word2.length());
        //System.out.println(max_decrypt_len);
        if(word2.length()/2 > max_decrypt_len)
        {
            return 0;
        }
        
        //build Trie tree?    
        
        //pre-search
        
        for(int i=0; i<word2.length()/2; i++)
        {
            List<Character> list = de_dict.get(word2.substring(i*2, i*2+2));
            if(list == null) return 0;
            
            boolean found = false;
            for(char c : list)
            {
                found |= bucket[i][c-'a'];
            }
            
            if(!found) return 0;
        }
        
        return _decrypt(word2, _root);
    }
    
    int _decrypt(String word, TrieNode root)
    {
        if(word.length() == 0)
        {
            return root.isWord? 1 : 0;
        }
        
        List<Character> list = de_dict.get( word.substring(0, 2) );
        
        if(list == null) return 0;
        
        int count = 0;
        for(char c : list)
        {
            TrieNode next = root.children.get(c);
            if(next != null)
            {
                count += _decrypt(word.substring(2), next);
            }
        }
        
        return count;
    }
}

/**
 * Your Encrypter object will be instantiated and called as such:
 * Encrypter obj = new Encrypter(keys, values, dictionary);
 * String param_1 = obj.encrypt(word1);
 * int param_2 = obj.decrypt(word2);
 */