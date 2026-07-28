class Solution(object):
    def findKthLargest(self, nums, k):
        #min heap keeps smallest element at the root of the tree / index 0
        #popping from a min heap will remove and return min element in heap
        #we always pop min element when there are more than k elements in heap
        #by the end we are left with k largest elements, and return the root which is the kth largest
        heap = []
        for num in nums:
            heapq.heappush(heap,num)
            
            if(len(heap) > k):
                heapq.heappop(heap)
            
        return heap[0]