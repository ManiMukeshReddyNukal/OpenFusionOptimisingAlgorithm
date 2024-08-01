class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for det in details:
            if int(det[11])>6 or ( det[11]=="6" and int(det[12])>0):
                count+=1
        return count
