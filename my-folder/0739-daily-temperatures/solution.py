class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        st=[]
        output=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while st and t>st[-1][0]:
                stackT,stackIndex=st.pop()
                output[stackIndex]=i-stackIndex
            st.append([t,i])
        return output
