import heapq
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        R:
        inp: sorted nums1, num2
        m =len nums1
        n = len nums2

        merge + sort into nums1
        return None

        E: 
        if n == zero -> do nothing

        A:
        #1
        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6]
                       3 
        add num2 to nums1 from index m to end of list - O(m)
        sort - (n log n)

        #2
        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6]
                     l                         
                                               r
        sorted_array [1, 2, 2]

        ...
        nums1 = sorted_array


        """

        sorted_array = []
        if n == 0:
            return None

        n1,n2 = 0,0
        while n1 < m and n2 < n:
            if nums1[n1] <= nums2[n2]:
                sorted_array.append(nums1[n1])
                n1+=1
            else:
                sorted_array.append(nums2[n2])
                n2+=1

        if n1 >= m and n2 < n:
            while n2 < n:
                sorted_array.append(nums2[n2]) 
                n2+=1

        if n2 >= n and n1 < m:
            while n1 < m:
                sorted_array.append(nums1[n1]) 
                n1+=1
        
        print(sorted_array)
        for i in range(m+n):
            nums1[i] = sorted_array[i]

        




        




        