class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l = []
        cur = 1
        while len(l) < n:
            l.append(cur)

            if cur*10 <= n:
                cur *= 10
            else:
                while cur == n or cur % 10 == 9:
                    cur = cur // 10
                cur += 1

        return l
                