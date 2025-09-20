import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        answer is unique
        R:
        
        return top k freq elems

        constraints: 1 <= k <= len(nums)
        E:
        if len(nums) == 1
        [1, 1, 2, 2, 3 ,3]

        set
        tuple
        not in set
            set: {1, 2}
        lst: [(2, 1), (2, 2), (2, 3)] - O(n)
        maxHeap [(-2, 1), (-2, 2), (-2, 3)] - O(n)
        pop k times from heap - k * log(n)
        k = 2
        """

        seen = dict()
        lst = []
        n = len(nums)
        if n == 1 and k == 1:
            return nums

        j = 0
        for i in range(n):
            x = nums[i]
            if not x in seen:
                seen[x] = j
                lst.append([-1, x])
                j+=1
            else:
                #print(seen[x])
                lst[seen[x]][0] -=1

        heapq.heapify(lst)
        print(lst)
        res = [(heapq.heappop(lst))[1] for _ in range(k)] 
        return res


        