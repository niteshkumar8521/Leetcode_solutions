class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        j = 0
        max_length = 0 
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[j])
                j += 1
            char_set.add(s[i])
            max_length = max(max_length,i-j+1)
        return max_length
        