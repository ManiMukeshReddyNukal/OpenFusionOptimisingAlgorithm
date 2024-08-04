class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        memo={}
        def recursive(i):
            if i==len(books):
                return 0
            if i in memo:
                return memo[i]
            height=0
            width=shelfWidth
            minheight=math.inf
            for j in range(i,len(books)):
                bookw,bookheight=books[j]
                if bookw>width:
                    break
                height=max(height,bookheight)
                width-=bookw
                minheight= min(height+recursive(j+1),minheight)
            memo[i]=minheight
            return minheight
        return recursive(0) 
