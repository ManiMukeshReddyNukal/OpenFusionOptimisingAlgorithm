class Solution(object):
    def getWinner(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        max_element=max(arr)
        curr = arr[0]
        winstreak=0
        queue=deque(arr[1:])
        while queue:
            oppenent=queue.popleft()
            if curr > oppenent:
                queue.append(oppenent)
                winstreak+=1
            else:
                queue.append(curr)
                curr=oppenent
                winstreak=1
            if winstreak == k or curr ==max_element:
                return curr
