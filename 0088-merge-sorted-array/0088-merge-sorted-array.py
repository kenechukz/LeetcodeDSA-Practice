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

        nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6]
                       3 
        add num2 to nums1 from index m to end of list - O(m)
        sort - (n log n)
        """

        if n == 0:
            return None

        for i in range(m, m+n):
            nums1[i] = nums2[i-m]

        nums1.sort()




        