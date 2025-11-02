class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        """
        R:
        given nums : List[int]
        given k: int

        return no. subarrays which sum to k

        E:
        1 <= nums.length <= 2 * 10^4
        -1000 <= nums[i] <= 1000
        -10^7 <= k <= 10^7

        A:
        from constraints -> we need O(n) solution (potential for n log n)

        nums = [2,1,3,0,-1,4], k = 3

        [2,1]
        [3,0]
        [-1,4]
        nums = [1,1,2,0,-1,4], k = 3
                         l
                           r
        [1,2]
        [1,2]
        [1,2,0]
        [-1,4]

        """

        count = 0
        prefixSum = 0
        prefixSums = {0: 1}  # prefixSum value → count of occurrences

        for num in nums:
            prefixSum += num
            if prefixSum - k in prefixSums:
                count += prefixSums[prefixSum - k]
            prefixSums[prefixSum] = prefixSums.get(prefixSum, 0) + 1

        return count


            

            
        