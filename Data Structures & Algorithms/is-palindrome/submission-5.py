class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = True
        s = [c.lower() for c in s if c.isalpha() or c.isdigit()]


        range_num = int(len(s) / 2)
        for num in range(range_num):
            if s[num] == s[len(s) - num - 1]:
                output = True
            else:
                output = False
        return output
        