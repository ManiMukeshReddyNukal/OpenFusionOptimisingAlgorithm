from collections import defaultdict, deque

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        # If the source is the same as the target, no travel is needed.
        if source == target:
            return 0

        # routes = [set(route) for route in routes]  # Convert each route to a set for O(1) lookups
        stop_to_routes = defaultdict(set)  # Use set to prevent duplicates
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].add(i)

        visited_routes = set()  # To keep track of visited routes
        visited_stops = {source}  # To keep track of visited stops
        queue = deque([(source, 0)])  # Queue now only needs the current stop and the bus count

        while queue:
            current_stop, bus_count = queue.popleft()
            for route_i in stop_to_routes[current_stop]:
                if route_i not in visited_routes:  # Check the route only if not visited
                    visited_routes.add(route_i)
                    for next_stop in routes[route_i]:
                        if next_stop == target:  # Found the target
                            return bus_count + 1
                        if next_stop not in visited_stops:  # If stop is not visited, add to queue
                            visited_stops.add(next_stop)
                            queue.append((next_stop, bus_count + 1))

        return -1  # If the target is unreachable

