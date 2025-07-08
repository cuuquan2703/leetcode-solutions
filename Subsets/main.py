class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        def BT(i):
            print(i)
            if i>=len(nums):
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            BT(i+1)

            sub.pop()
            BT(i+1)

        BT(0)
        return res