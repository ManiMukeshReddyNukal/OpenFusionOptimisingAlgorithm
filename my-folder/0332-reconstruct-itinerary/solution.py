class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph=collections.defaultdict(list)
        for [src,dest] in sorted(tickets,reverse=True):
            graph[src].append(dest)
        itenary=[]
        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            itenary.append(node)
        dfs("JFK")
        return itenary[::-1]
