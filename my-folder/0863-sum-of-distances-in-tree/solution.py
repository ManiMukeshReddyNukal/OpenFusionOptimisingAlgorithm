class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        count=[1]*n
        ans=[0]*n
        def dfs1(node=0,parent=None):
            for adjnode in graph[node]:
                if adjnode!=parent:
                    dfs1(adjnode,node)
                    count[node]+=count[adjnode]
                    ans[node]+=ans[adjnode]+count[adjnode]
        def dfs2(node=0,parent=None):
            for adjnode in graph[node]:
                if adjnode!=parent:
                    ans[adjnode]=ans[node]-count[adjnode]+n-count[adjnode]
                    dfs2(adjnode,node)
        
        graph=defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)
        dfs1()
        dfs2()
        return ans
