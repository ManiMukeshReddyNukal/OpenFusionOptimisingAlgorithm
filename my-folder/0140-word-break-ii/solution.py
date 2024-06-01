class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset=set(wordDict)
        result=[]
        self.backtrack(s, 0, result, wordset, [])
        return result
    def backtrack(self,s,curIndex,result,wordset,curSentense):
        if curIndex==len(s):
            result.append(" ".join(curSentense))
        for i in range(curIndex+1,len(s)+1):
            word=s[curIndex:i]
            if word in wordset:
                curSentense.append(word)
                self.backtrack(s, i, result, wordset, curSentense)
                curSentense.pop()

