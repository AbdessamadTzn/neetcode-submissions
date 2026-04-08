class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for val in range(0, len(nums)):
            for val1 in range(val+1, len(nums)):
                if nums[val]+nums[val1] == target:
                    return [val, val1]

        
        