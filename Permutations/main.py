class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if (len(nums) == 1):
            return [nums.copy()]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for j in perms:
                j.append(n)
            res.extend(perms)
            nums.append(n)

        return res
