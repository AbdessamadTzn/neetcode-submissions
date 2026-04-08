class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            u=1
            j = 0
            while j<len(nums):
                if i != j:
                    u *= nums[j]
                j+=1
            res.append(u)

        return res


        
        