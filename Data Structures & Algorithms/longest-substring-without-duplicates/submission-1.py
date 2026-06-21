class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_value = 0
        for i in range(len(s)):
            j_long_value = 1
            long_word = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in long_word:
                    j_long_value += 1
                else:
                    break
                long_word += s[j]
            if max_value < j_long_value:
                max_value = j_long_value
        return max_value