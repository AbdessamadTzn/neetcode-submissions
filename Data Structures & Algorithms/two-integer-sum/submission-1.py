class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for idx, val in enumerate(nums):
            hash_map[val] = idx

        for idx in range(len(nums)):
            y = target - nums[idx]
            if y in hash_map and hash_map[y] != idx:
                return [idx, hash_map[y]]

        
        