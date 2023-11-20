class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """        
        lastindex={"M":0,"P":0,"G":0}
        count=0
        for i in range(len(garbage)):
            c={char:garbage[i].count(char) for char in garbage[i]}
            for key in c.keys():
                lastindex[key]=i
            count+=len(garbage[i])
        print(travel[:lastindex.get("M")])
        return count+sum(travel[:lastindex.get("M")])+sum(travel[:lastindex.get("G")])+sum(travel[:lastindex.get("P")])

