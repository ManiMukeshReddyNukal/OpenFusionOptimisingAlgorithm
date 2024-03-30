from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes: list[list[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(set)
        for i, route in enumerate(routes):
            for stop in route:
                graph[stop].add(i)

        visited_stops = set()
        visited_routes = set()
        visited_stops.add(source)
        queue = [(source, 0)]

        while queue:
            current_stop, bus_count = queue.pop(0)
            for route_i in graph[current_stop]:
                if route_i not in visited_routes:
                    visited_routes.add(route_i)
                    for stop in routes[route_i]:
                        if stop == target:
                            return bus_count + 1
                        if stop not in visited_stops:
                            visited_stops.add(stop)
                            queue.append((stop, bus_count + 1))
        return -1

