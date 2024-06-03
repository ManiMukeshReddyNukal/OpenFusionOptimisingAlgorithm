class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj={i:[] for i in range(numCourses)}
        indegree=[0]*numCourses
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        noofcourses=0
        while q:
            node=q.pop()
            noofcourses+=1
            for c in adj[node]:
                indegree[c]-=1
                if indegree[c]==0:
                    q.append(c)
        return noofcourses==numCourses
