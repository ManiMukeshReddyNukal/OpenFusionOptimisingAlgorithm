class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        st=[]
        cars=[[p,s] for p,s in zip(position,speed)]
        for p,s in sorted(cars)[::-1]:
            st.append(float(target-p)/s)
            if len(st)>=2 and st[-1]<=st[-2]:
                st.pop()
        print(st)
        return len(st)
