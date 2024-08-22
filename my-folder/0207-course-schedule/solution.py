class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        graph=defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            indegree[prereq[0]]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        completed=0
        while q:
            node=q.pop()
            completed+=1
            for adjnode in graph[node]:
                indegree[adjnode]-=1
                if indegree[adjnode]==0:
                    q.append(adjnode)
        return completed==numCourses
