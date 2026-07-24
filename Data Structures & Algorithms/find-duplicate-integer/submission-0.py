class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        duplicates = []

        for i in range(len(nums)):

            x = abs(nums[i])

            if nums[x] > 0:
                nums[x] = -nums[x]
            else:
                return x
        