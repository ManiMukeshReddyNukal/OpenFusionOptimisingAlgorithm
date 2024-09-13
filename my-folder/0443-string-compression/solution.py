class Solution:
    def compress(self, chars: List[str]) -> int:
        i,k,n=0,0,len(chars)
        while i<n:
            j=i+1
            while j<n and chars[j]==chars[i]:
                j+=1
            chars[k]=chars[i]
            k+=1
            if (j-i)>1:
                for c in str(j-i):
                    chars[k]=c
                    k+=1
            i=j
        return k
