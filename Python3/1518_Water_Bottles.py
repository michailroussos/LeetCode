class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drunkBottles=numBottles
        emptyBottles=drunkBottles

        while emptyBottles//numExchange>0:
            drunkBottles+=emptyBottles//numExchange
            emptyBottles=emptyBottles//numExchange + emptyBottles%numExchange
        
        return drunkBottles

