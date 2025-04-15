class Solution:
    def maxArea(self, height: List[int]) -> int:

        l,r = 0,len(height)-1
        #base = [i,0]
        #top = [i, height[i]]
        
        maxArea = 0
        


        while l != r:
            #minHeight = min(height[l], height[r])
            #length = r-l

            #area = min(height[l], height[r]) * (r-l)

            if min(height[l], height[r]) * (r-l) > maxArea:
                maxArea = min(height[l], height[r]) * (r-l)
            
            
            if height[l] > height[r]:
                
                r -= 1
            elif height[l] < height[r]:
                l+= 1
            else:
                r-=1
        
        return maxArea