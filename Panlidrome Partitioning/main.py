class Solution:
    def isPali(self, s: list, l: int, r: int) -> bool:
        while l < r:
            if s[l] != s[r]:
                return False
            l , r = l + 1, r - 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []

        def BT(i):
            if i >= len(s):
                res.append(cur[:])
                return
            for j in range(i, len(s)):
                if self.isPali(s, i , j):
                    cur.append(s[i:j+1])
                    BT(j+1)
                    cur.pop()
        BT(0)
        return res