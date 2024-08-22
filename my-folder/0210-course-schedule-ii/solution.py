class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
        order=[]
        while q:
            node=q.pop()
            order.append(node)
            completed+=1
            for adjnode in graph[node]:
                indegree[adjnode]-=1
                if indegree[adjnode]==0:
                    q.append(adjnode)
        return order if completed==numCourses else []
