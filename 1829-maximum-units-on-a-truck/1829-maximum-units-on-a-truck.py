class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        """
        R:



        return max no. units that can be put in truck (as long as no. boxes < truckSize)

        E:

        if boxTypes.length == 1:

        
        A:

        boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4

        unitsPerBox {0: 3, 1: 2, 2: 1}

        1 * 3 + 2* 2 + 1 * 1 = 8


        """

        boxTypes.sort(key= lambda x: x[1], reverse=True)

        res = 0

        print(boxTypes)
        for i in range(len(boxTypes)):
            boxes = boxTypes[i][0]
            units = boxTypes[i][1]

            if boxes > truckSize:
                res += truckSize * units
                return res

            res += boxes * units
            truckSize -= boxes

        return res

        

            

            






