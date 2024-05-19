class Solution {
   /*
    * pseudocode
    * hashmap = new hashmap();
    * foreach(int num : nums) {
    * if (!hashmap.contains(num)) {
    * hashmap.put(num, 1);
    * } else {
    * hashmap.put(num, hashmap.getOrDefault(num, 0) + 1);
    * }
    * }
    */
   public int[] topKFrequent(int[] nums, int k) 
   {
    Map<Integer,Integer> map = new HashMap<>();
    for(int i : nums)
    {
        if(!map.containsKey(i))
        {
            map.put(i, map.getOrDefault(i,0)+1);
        }
        map.put(i, map.getOrDefault(i, 0) + 1);
    }
    
    List<Map.Entry<Integer, Integer>> sortedEntries = new ArrayList<>(map.entrySet());
    sortedEntries.sort(Map.Entry.<Integer, Integer>comparingByValue().reversed());
    int[] result = new int[k];
    for (int i = 0; i < k; i++) {
        result[i] = sortedEntries.get(i).getKey();
    }

    return result;
   }
}