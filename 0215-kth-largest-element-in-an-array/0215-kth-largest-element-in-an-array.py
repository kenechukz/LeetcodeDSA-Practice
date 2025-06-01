import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # nums = [3,2,3,1,2,4,5,5,6], k = 4
        # 1,2,2,3,3,4,5,5,6 
        # Time complexity: O(n + klogn)
        # Space complexity: O(1)

        nums = [-num for num in nums]
        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)
            


        return -heapq.heappop(nums)
        


        