class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        length=len(students)
        sq=deque()
        sandwiches_stack=[]
        for i in range(length):
            sandwiches_stack.append(sandwiches[length-i-1])
            sq.append(students[i])
        last_served=0
        while len(sq)>0 and last_served<len(sq):
            if sandwiches_stack[-1]==sq[0]:
                sandwiches_stack.pop()
                sq.popleft()
                last_served=0
            else:
                sq.append(sq.popleft())
                last_served+=1
        return len(sq)
