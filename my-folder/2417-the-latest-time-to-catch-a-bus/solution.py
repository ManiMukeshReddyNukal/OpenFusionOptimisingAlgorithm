class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort() # m
        passengers.sort()  # n
        p=0
        timearrival=-1
        for bus in buses:
            if p==len(passengers):
                return buses[-1]
            cap=0
            while p<len(passengers) and cap<capacity and passengers[p]<=bus:
                p+=1
                cap+=1
            timearrival=bus if cap<capacity else passengers[p-1]
        while timearrival in passengers:
            timearrival-=1
        return timearrival
