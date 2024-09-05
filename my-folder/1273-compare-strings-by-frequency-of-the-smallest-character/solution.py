class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        freq=[]
        for word in words:
            f=1
            word=sorted(word)
            prev=None
            for c in word:
                if prev and c==prev:
                    f+=1
                elif prev and c!=prev:
                    break
                prev=c
            freq.append(f)
        qf=[]    
        for query in queries:
            f=1
            word=sorted(query)
            prev=None
            for c in word:
                if prev and c==prev:
                    f+=1
                elif prev and c!=prev:
                    break
                prev=c
            qf.append(f)
        resp=[]
        for q in qf:
            resp.append(sum( 1 for c in freq if c>q))
        return resp
