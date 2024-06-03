from collections import deque, defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Create a set of all unique characters
        uniqchars = set("".join(words))
        # Initialize graph and in-degree count
        graph = defaultdict(set)
        inorder = {char: 0 for char in uniqchars}
        
        # Build the graph
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minlen = min(len(word1), len(word2))
            # Check for a prefix condition that would indicate an invalid input
            if len(word1) > len(word2) and word1[:minlen] == word2[:minlen]:
                return ""
            # Build the graph from the first point of difference
            for j in range(minlen):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        inorder[word2[j]] += 1
                    break
        
        # Use Kahn's algorithm for topological sorting
        queue = deque([char for char in inorder if inorder[char] == 0])
        res = []
        
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in graph[node]:
                inorder[neighbor] -= 1
                if inorder[neighbor] == 0:
                    queue.append(neighbor)
        
        # If the result does not contain all characters, there must be a cycle
        if len(res) != len(uniqchars):
            return ""
        
        return "".join(res)

