class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        beginind = {}
        n = len(fruits)
        beginind[0]=0
        for i in range(1,n):
            if fruits[i-1]==fruits[i]:
                beginind[i]=beginind[i-1]
            else:
                beginind[i]=i
        
        i=0
        length = 0
        curtypes = set()
        for j in range(n):
            curtypes.add(fruits[j])
            if len(curtypes)>2:
                i=beginind[j-1]
                curtypes = {fruits[j],fruits[j-1]}
            else:
                length = max(length,j-i+1)
        return length
