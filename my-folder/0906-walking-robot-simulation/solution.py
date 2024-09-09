class Solution:
    def __init__(self):
        self.HASH_MULTIPLIER=60013
    def _hash_condition(self,x,y):
        return x*self.HASH_MULTIPLIER+y
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set={self._hash_condition(x, y) for x,y in obstacles}
        direction=[(0,1),(1,0),(0,-1),(-1,0)]
        x,y=0,0
        max_distance=0
        current_direction=0
        for command in commands:
            if command==-1:
                current_direction=(current_direction+1)%4
                continue
            elif command==-2:
                current_direction=(current_direction+3)%4
                continue
            else:
                dx,dy=direction[current_direction]
                for _ in range(command):
                    nx,ny=x+dx,y+dy
                    if self._hash_condition(nx, ny) in obstacle_set:
                        break
                    x,y=nx,ny
                    max_distance=max(max_distance,x*x+y*y)
        return max_distance
