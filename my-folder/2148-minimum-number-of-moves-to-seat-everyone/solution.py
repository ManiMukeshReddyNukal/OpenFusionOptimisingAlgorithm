class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats=sorted(seats)
        students=sorted(students)
        ans=0
        for i in range(len(students)):
            ans+=abs(students[i]-seats[i])
        return ans
