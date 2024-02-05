class Solution:
    def firstUniqChar(self, s: str) -> int:
        st=set()
        q=[]
        for c in s:
            if c in st:
                if c in q:
                    q.remove(c)
                continue
            else:
                st.add(c)
                q.append(c)
        if q==[]:
            return -1
        return s.index(q.pop(0))


