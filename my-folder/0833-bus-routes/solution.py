class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        map=defaultdict(list)
        for i,rs in enumerate(routes):
            for route in rs:
                map[route].append(i)
        if source==target:
            return 0
        q=deque([(source,0)])
        visited=set([source])
        visited_buses=set()
        while q:
            node,busno=q.popleft()
            if node==target:
                return busno
            buses=map[node]
            for bus in buses:
                if bus not in visited_buses:
                    visited_buses.add(bus)
                    for n in routes[bus]:
                        if n not in visited:
                            visited.add(n)
                            q.append((n,busno+1))
        return -1


