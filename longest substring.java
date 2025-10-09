import java.util.*;

public class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> lastSeen = new HashMap<>();
        int left = 0, maxLen = 0;

        for (int right = 0; right < s.length(); right++) {
            char c = s.charAt(right);

            // If character was seen and is within the current window
            if (lastSeen.containsKey(c) && lastSeen.get(c) >= left) {
                left = lastSeen.get(c) + 1; // Move left pointer past duplicate
            }

            lastSeen.put(c, right); // Update latest position
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }

    // Optional test
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.lengthOfLongestSubstring("abcabcbb")); // 3 ("abc")
        System.out.println(sol.lengthOfLongestSubstring("bbbbb"));    // 1 ("b")
        System.out.println(sol.lengthOfLongestSubstring("pwwkew"));   // 3 ("wke")
        System.out.println(sol.lengthOfLongestSubstring(""));         // 0
    }
}
