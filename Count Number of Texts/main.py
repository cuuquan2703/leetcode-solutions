from functools import lru_cache
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def backtrack(index):
            print('index: ', index)
            if index == len(pressedKeys):
                return 1

            total = 0
            digit = pressedKeys[index]
            print('digit: ', digit)
            max_len = 4 if digit in '79' else 3
            print('max_len: ', max_len)
            for l in range(1, max_len + 1):
                print(pressedKeys[index:index + l], digit * l)
                if index + l > len(pressedKeys):
                    break
                if pressedKeys[index:index + l] == digit * l:
                    total = (total + backtrack(index + l)) % MOD
                else:
                    break

            return total

        return backtrack(0)
        