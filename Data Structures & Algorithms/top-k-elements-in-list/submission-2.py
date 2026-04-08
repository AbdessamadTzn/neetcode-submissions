from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        most_common = [elm for elm, count in count.most_common(k)]

        return most_common