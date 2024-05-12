class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def sumofotherchars(dic):
            maxchar, maxcount = '',0
            for k,v in dic.items():
                if v>maxcount:
                    maxchar=k
                    maxcount=v
            c = maxchar
            total = 0
            for k,v in dic.items():
                if k!=c: total+=v
            return total
        dic = {}
        start = 0
        n=len(s)
        maxlen = 0
        for i in range(n):
            if sumofotherchars(dic)==k:
                # print(dic, start)
                if s[i] not in dic:
                    dic[s[i]] = 0
                dic[s[i]] += 1
                # print(dic,start, i)
                # print(sumofotherchars(dic))
                while sumofotherchars(dic) > k:
                    # print(sumofotherchars(dic)
                    # print(dic,start)
                    dic[s[start]]-=1
                    if not dic[s[start]]: del dic[s[start]]
                    start += 1
                    # print(dic,start)
                maxlen = max(maxlen, i-start+1)
            else:
                # print(dic)
                if s[i] not in dic: dic[s[i]] = 0
                dic[s[i]]+=1
                maxlen = max(maxlen, i-start+1)
        return maxlen
