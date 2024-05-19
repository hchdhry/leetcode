class Solution {
    public boolean isAnagram(String s, String t) {
    
        if(s.length()!= t.length()) return false;
        Map<Character,Integer> map = new HashMap<>();
        for(char x : s.toCharArray())
        {
           map.put(x, map.getOrDefault(x, 0) + 1);
        }
        for(char z : t.toCharArray())
        {
            map.put(z, map.getOrDefault(z,0)-1);
        }
        for(int value:map.values())
        {
            if (value!=0) return false;

        }
        return true;
    




    }
}