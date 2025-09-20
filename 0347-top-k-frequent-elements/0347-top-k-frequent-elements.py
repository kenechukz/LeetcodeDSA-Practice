class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Step 1: count frequencies
        freq_map = Counter(nums)   # O(n)

        # Step 2: bucket where index = frequency
        bucket_arr = [[] for _ in range(n+1)]

        # O(n)
        for num, freq in freq_map.items():
            bucket_arr[freq].append(num)
        
        # pop k freq elems
        res = []

        for i in range(n, -1,-1):
            bucket = bucket_arr[i]
            for num in bucket:
                res.append(num)
                if len(res) == k:
                    return res
            