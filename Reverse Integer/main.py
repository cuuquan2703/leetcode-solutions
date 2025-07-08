class Solution:
    def reverse(self, x: int) -> int:
        tmp = x
        if x < 0:
            tmp = -tmp

        result = 0
        while tmp != 0:
            res = tmp % 10
            result =result*10 + res
            tmp //= 10

        if x < 0:
            result = -result
        
        if -2**31 <= result <= 2**31 - 1:
            return result
        
        return 0
        
