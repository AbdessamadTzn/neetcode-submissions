class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # for k in range(1, max(piles)+1):
        #     hours = 0
        #     for i in piles:
        #         hour_per_pile = i/k

        #         hours+=math.ceil(hour_per_pile)

        #     if hours <= h:
        #         return k
        
        # return -1

        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = lo + (hi-lo)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid)
            
            if hours <= h:
                hi = mid
            else:
                lo = mid+1
        
        return lo



            