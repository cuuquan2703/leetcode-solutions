class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        res = None
        if len(s) == 1:
            return 1
        for i in range(len(s) - 1):
            t = s[i]
            for j in range(i+1, len(s)):
                if s[j] in t:
                    if len(t) > max:
                        max = len(t)
                        res = t
                        break
                else:
                    t += s[j]

        return len(res)