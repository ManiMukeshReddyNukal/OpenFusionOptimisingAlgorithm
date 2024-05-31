from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def backtrackEvaluate(current, target, visited, product):
            """ Helper function to evaluate division from current to target using DFS """
            visited.add(current)
            # Direct connection found
            if target in graph[current]:
                return product * graph[current][target]
            # Search through neighbors
            result = -1.0
            for neighbor, value in graph[current].items():
                if neighbor not in visited:
                    result = backtrackEvaluate(neighbor, target, visited, product * value)
                    if result != -1.0:
                        break
            visited.remove(current)
            return result

        # Building the graph
        graph = defaultdict(lambda: defaultdict(float))
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        
        # Processing queries
        responses = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                responses.append(-1.0)  # Either variable not in graph
            elif dividend == divisor:
                responses.append(1.0)   # Dividing something by itself
            else:
                visited = set()
                responses.append(backtrackEvaluate(dividend, divisor, visited, 1))
        return responses

