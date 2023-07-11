class Solution:
  def maximumEvenSplit(self, finalSum: int) -> List[int]:
    if finalSum & 1 :
      return []
    list=[]
    sum=finalSum
    even=2
    while(sum-even >= even + 2):
      list.append(even)
      sum-=even
      even+=2
    return list + [sum]
