class StockSpanner(object):

    def __init__(self):
        self.stack=[]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        q=self.stack
        count=1
        while q and price>=q[-1][0]:
            count+=q.pop()[1]
        q.append([price,count])
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
