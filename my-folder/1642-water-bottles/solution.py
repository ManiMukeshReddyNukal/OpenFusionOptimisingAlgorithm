class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        resp=numBottles
        while numBottles>=numExchange:
            resp+=numBottles//numExchange
            numBottles=numBottles//numExchange+numBottles%numExchange
        return resp
