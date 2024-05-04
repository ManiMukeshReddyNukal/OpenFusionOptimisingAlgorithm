class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        count=0
        l=0
        r=len(people)-1
        while l<=r:
            count+=1
            if people[l]+people[r]<=limit:
                l+=1
                r-=1
            else:
                l+=1
        return count
