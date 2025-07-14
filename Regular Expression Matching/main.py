from functools import lru_cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def DP(i, j):
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            dot = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                if DP(i, j + 2) or (dot and DP(i + 1, j)):
                    return True
                else:
                    return False

            if dot:
                return DP(i + 1, j + 1)

            return False

        return DP(0, 0)
