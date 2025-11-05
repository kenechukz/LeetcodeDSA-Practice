class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
        R:
        given nums
        return nums[i], nums[j], nums[k], s.t. their sum == 0
        i != j != k
        unqiue answers

        E:
        3 <= nums.length <= 3000 - suggests O(N^2 / N LOG N)

        -10^5 <= nums[i] <= 10^5
         
        can have negatives

        A:
        Solution #1 (O(n^3)):

        3 for loops
        i, j, k

        Solution #2 (O(n^2))

        [-1,0,1,2,-1,-4]

        [[-1,-1,2],[-1,0,1]]

        sort input:
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]
             c  l     r 

             c  l   r
                  l r

        for each elem:
            have pointers at c+1 (l) and len(nums)-1 (r)

            if nums[c] + nums[l] + nums[r] == 0:



        """


        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            c = nums[i]
            l = i + 1
            r = n-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break
                
            while l < r:
                if c + nums[l] + nums[r] == 0:
                    res.append([c, nums[l], nums[r]])
                    r-=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1

                elif c + nums[l] + nums[r] < 0:
                    l+=1

                else:
                    r-=1
                        

        return res