public class Solution {
    public bool IsAnagram(string s, string t) {
 
        if (s.Length != t.Length) {
            return false;
        }

     
        Dictionary<char, int> charFrequency = new Dictionary<char, int>();

      
        foreach (char c in s) {
            if (charFrequency.ContainsKey(c)) {
                charFrequency[c]++;
            } else {
                charFrequency[c] = 1;
            }
        }

       
        foreach (char c in t) {
            if (!charFrequency.ContainsKey(c)) {
                return false; 
            } else {
                charFrequency[c]--;
            }
        }

        
        foreach (int value in charFrequency.Values) {
            if (value != 0) {
                return false;
            }
        }

        return true; 
    }
}