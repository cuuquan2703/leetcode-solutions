from functools import lru_cache
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)

        # Filter out useless offers (where the offer isn't cheaper than buying individually)
        filtered_special = []
        for sp in special:
            total = sum(sp[i] * price[i] for i in range(n))
            if total > sp[-1]:  # Only use if the offer actually saves money
                filtered_special.append(sp)

        @lru_cache(maxsize=None)
        def dfs(cur_needs):
            # Base case: Buy all items individually
            total = sum(cur_needs[i] * price[i] for i in range(n))

            for offer in filtered_special:
                valid = True
                new_needs = []
                for i in range(n):
                    if offer[i] > cur_needs[i]:
                        valid = False
                        break
                    new_needs.append(cur_needs[i] - offer[i])
                if valid:
                    total = min(total, offer[-1] + dfs(tuple(new_needs)))

            return total

        return dfs(tuple(needs))
            