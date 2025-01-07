class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_val = max(candies)
        res = []
        for i in range(0, len(candies)):
            if (candies[i] + extraCandies) >= max_val:
                res.append(True)
            else:
                res.append(False)
        
        return res