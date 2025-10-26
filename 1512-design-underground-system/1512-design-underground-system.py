class UndergroundSystem:
    """
    R:
    average travel times between different stations

    getAverageTime(string startStation, string endStation) - Returns the average time it takes 
    to travel from startStation to endStation.


    when customer checks out -> stations[endStation] = {startStation: [end_time - start_time]}


    call to getAverageTime -> sum(stations[endStation][startStation]) / no. trips (len of stations[endStation]
    [startStation])

    """

    def __init__(self):
        
        # customers[id] = [start_time, checked_in?, prev_station]
        self.customers = {}
        # when customer checks out -> stations[endStation] = {startStation: [end_time - start_time]}
        self.stations = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:

        if id not in self.customers:
            self.customers[id] =[-1, False, stationName]

        if stationName not in self.stations:
            self.stations[stationName] = {}

        # check if customer is checked in already
        elif self.customers[id][1] == True:
            return

        self.customers[id][0] = t 
        self.customers[id][1] = True  
        self.customers[id][2] = stationName  

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station = self.customers[id][2]
        start_time = self.customers[id][0]

        if stationName not in self.stations:
            self.stations[stationName] = {}

        if start_station not in self.stations[stationName]:
            self.stations[stationName][start_station] = []

        self.stations[stationName][start_station].append(t- start_time)
        self.customers[id][1] = False

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        total_time = sum(self.stations[endStation][startStation])
        trips = len(self.stations[endStation][startStation])

        return total_time / trips


        
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


