from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        return_list = []
        for i in range(k):
            key_max = max(d, key=d.get)
            return_list.append(key_max)
            del d[key_max]
        return return_list