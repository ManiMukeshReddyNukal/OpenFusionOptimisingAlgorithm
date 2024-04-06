class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=collections.defaultdict(list)
        indegre=[0]*numCourses
        for (a,b) in prerequisites:
            graph[a].append(b)
            indegre[b]+=1
        q=collections.deque()
        for i in range(numCourses):
            if indegre[i]==0:
                q.append(i)
        processorder=[]
        processcount=0
        while q:
            node=q.popleft()
            for adjnode in graph[node]:
                indegre[adjnode]-=1
                if indegre[adjnode]<=0:
                    q.append(adjnode)
            processorder.append(node)
            processcount+=1
        print(processorder[::-1])
        if processcount==numCourses:
            return True
        return False
