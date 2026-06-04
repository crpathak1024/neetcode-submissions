class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        return [item[0] for item in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
        