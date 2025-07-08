class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []

        def BT(openN, closeN):
            if openN == closeN == n:
                res.append("".join(cur))
                return
            
            if openN < n:
                cur.append('(')
                BT(openN + 1, closeN)
                cur.pop()

            if closeN < openN:
                cur.append(')')
                BT(openN, closeN + 1)
                cur.pop()
        BT(0,0)
        return res