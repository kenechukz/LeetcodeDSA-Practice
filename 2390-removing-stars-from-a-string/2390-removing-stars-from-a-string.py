class Solution:
    def removeStars(self, s: str) -> str:
        
        #lee*cod*e
        #lecoe
        
        #given string which can contains *

        # if char is star remove top of stack and remove star

        stack = []


        for i in range(len(s)):


            if s[i] == "*":
                if stack:
                    stack.pop()

            else:
                stack.append(s[i])

        
        return ''.join(stack)
        
                
            

        
    


        
                