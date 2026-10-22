class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # duplicates = []

        # for i in range(len(nums)):

        #     x = abs(nums[i])

        #     if nums[x] > 0:
        #         nums[x] = -nums[x]
        #     else:
        #         return x

        fast, slow = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break

        return slow