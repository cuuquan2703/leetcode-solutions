class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def BT(i, curr, sum):
            if sum == target:
                res.append(curr[:])
                return
            
            if i >= len(candidates) or sum > target:
                return

            curr.append(candidates[i])
            BT(i, curr, sum + candidates[i])
            curr.pop()
            BT(i+1, curr, sum)
        
        BT(0,[],0)
        return res
            
                

