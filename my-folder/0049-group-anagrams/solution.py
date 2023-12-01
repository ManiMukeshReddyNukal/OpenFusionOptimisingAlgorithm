class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        diclist={}
        for i in strs:
            key=tuple(sorted(i))
            if key not in diclist:
                diclist[key]=[]
            diclist[key].append(i)
        return [diclist[i] for i in diclist]
        
