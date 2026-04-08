class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_pre = max_suff = 0
        walls_left = [0]*n
        walls_right = [0]*n

        for i in range(n):
            j = -i-1
            walls_left[i] = max_pre
            walls_right[j] = max_suff
            max_pre = max(max_pre, height[i])
            max_suff = max(max_suff, height[j])
        
        res = 0
        for i in range(n):
            pot = min(walls_left[i], walls_right[i]) - height[i]
            res+=max(0, pot)
        return res

        