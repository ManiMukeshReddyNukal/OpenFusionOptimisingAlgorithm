class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph=defaultdict(list)
        itenary=[]
        for ticket in sorted(tickets, reverse=True):
            graph[ticket[0]].append(ticket[1])
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            itenary.append(node)
        dfs("JFK")
        return itenary[::-1]
            
