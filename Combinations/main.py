class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def BT(start, comb):
            if (len(comb) == k):
                res.append(comb[:])
                return

            for i in range(start, n+1):
                comb.append(i)
                BT(i+1, comb)
                comb.pop()

        if n > 0 and k > 0:
            BT(1,[])
        return res