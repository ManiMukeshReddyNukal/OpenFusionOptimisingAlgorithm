class Solution(object):
    def winnerOfGame(self, colors):
        count = 0
        for i in range(1,len(colors)-1):
            if colors[i-1] + colors[i] + colors[i+1] == "AAA":
                count += 1
            if colors[i-1] + colors[i] + colors[i+1] == "BBB":
                count -= 1
        if count > 0 :
            return True
        return False

        
