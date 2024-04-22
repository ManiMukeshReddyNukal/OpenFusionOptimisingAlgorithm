class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        next_slot = {
            "0": "1",
            "1": "2",
            "2": "3",
            "3": "4",
            "4": "5",
            "5": "6",
            "6": "7",
            "7": "8",
            "8": "9",
            "9": "0",
        }
        # Map the previous slot digit for each current slot digit.
        prev_slot = {
            "0": "9",
            "1": "0",
            "2": "1",
            "3": "2",
            "4": "3",
            "5": "4",
            "6": "5",
            "7": "6",
            "8": "7",
            "9": "8",
        }
        q=deque()
        visited=set(deadends)
        if '0000' in visited:
            return -1
        depth=0
        q.append('0000')
        visited.add('0000')
        while q:
            cur_level_nodes=len(q)
            for _ in range(cur_level_nodes):
                node=q.popleft()
                if node==target:
                    return depth
                for i in range(4):
                    new_node=list(node)
                    new_node[i]=next_slot[new_node[i]]
                    new_node="".join(new_node)
                    if new_node not in visited:
                        q.append(new_node)
                        visited.add(new_node)
                    new_node=list(node)
                    new_node[i]=prev_slot[new_node[i]]
                    new_node="".join(new_node)
                    if new_node not in visited:
                        q.append(new_node)
                        visited.add(new_node)
            depth+=1
        return -1
