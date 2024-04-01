class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row_dict = defaultdict(list)
        col_dict = defaultdict(list)
        
        for a,b in stones:
            row_dict[a].append(b)
            col_dict[b].append(a)
        
        visited = set()

        ans = 0
        que = deque()
        for a,b in stones:
            if (a,b) not in visited:
                #BFS start here for each connected component
                que.append((a,b))
                
                while que:
                    x,y = que.popleft()
                    if (x,y) in visited:
                        continue
                        
                    visited.add((x,y))
                    ans+=1
                    for e in row_dict[x]:  #append all points which are in same line as (x,y)
                        if e!=y:
                            que.append((x,e))
                                            
                    for e in col_dict[y]:  #append all points which are in same column as (x,y)
                        if e!=x:
                            que.append((e,y))
                            
                            
                    # here are two line which make code time complexity O(n^2) to O(n) :-
                    # if any point covers its entire row and column points, then again no need to cover these points again.
                    
                    row_dict[x].clear()
                    col_dict[y].clear()
                
                # each component can not destroy it self completely , there is only one point always exist , so
                ans -=1    
            
        return ans
		
