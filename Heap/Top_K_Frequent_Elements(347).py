class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = []

        for key in freq.keys():
            if len(heap) == k:
                heapq.heappushpop(heap, (freq[key], key))
            else:
                heapq.heappush(heap, (freq[key], key))
            
        ans = []
        while k > 0:
            k -= 1
            ans.append(heappop(heap)[1])
        
        return ans