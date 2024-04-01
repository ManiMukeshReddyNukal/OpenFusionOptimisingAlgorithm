class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st=[]
        i=0
        m=len(popped)
        for n in pushed:
            st.append(n)
            while i<m and st and st[-1]==popped[i]:
                st.pop()
                i+=1
        return not st
