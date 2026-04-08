class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        l, r = 0, n-1
        max_area = 0

        while l < r:
            area = (r-l) * min(heights[l], heights[r])
            if max_area < area:
                max_area = area
            if min(heights[l], heights[r]) == heights[l]:
                l+=1
            else:
                r-=1
        return max_area
            
        