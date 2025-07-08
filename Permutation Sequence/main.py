class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ckn = {
            '1': 1,
            '2': 2,
            '3': 6,
            '4': 24,
            '5': 120,
            '6': 720,
            '7': 5040,
            '8': 40320
        }

        l = [i for i in range(1, n+1)]
        s = ''
        i = 1
        while len(s) < n-1:
            e = k // ckn[f'{n-i}']
            r = k % ckn[f'{n-i}']
            if (r ==0):
                e-=1
            s += str(l[e])
            l.remove(l[e])
            k = r
            i += 1

        s += str(l[0])
        return s