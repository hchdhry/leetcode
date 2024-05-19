class Solution {
    public List<List<String>> groupAnagrams(String[] strs) 
    {
        Map<String, List<String>> map = new HashMap();
        for(String a: strs)
        {
            char[] wordToArray = a.toCharArray();
            Arrays.sort(wordToArray);
            String sortedWord = new String(wordToArray);
            if(!map.containsKey(sortedWord))
            {
                map.put(sortedWord, new ArrayList<>());

            } 
            map.get(sortedWord).add(a);

        }
        return new ArrayList<>(map.values());

    }
}