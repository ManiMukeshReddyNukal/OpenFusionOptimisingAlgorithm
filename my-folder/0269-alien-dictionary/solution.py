from collections import defaultdict

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        # Initialize graph with all unique characters to ensure they're included in the final graph
        unique_chars = set(''.join(words))
        for char in unique_chars:
            graph[char] = set()

        n = len(words)
        for i in range(n - 1):
            word1, word2 = words[i], words[i + 1]
            minlen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minlen] == word2[:minlen]:
                return ""
            for j in range(minlen):
                if word1[j] != word2[j]:
                    graph[word1[j]].add(word2[j])
                    break

        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nc in graph[c]:
                if dfs(nc):
                    return True
            visit[c] = False
            res.append(c)
            return False

        # Use a static list of keys for safe iteration
        for c in list(graph.keys()):
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)

# Your test case
solution = Solution()
print(solution.alienOrder(["z", "z"]))

