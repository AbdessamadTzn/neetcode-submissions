from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        most_freq_element = [elm for elm, count in counter.most_common(k)]

        return most_freq_element