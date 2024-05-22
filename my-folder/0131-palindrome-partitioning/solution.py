class Solution:
    def isPalindrome(self,s:str):
        return s==s[::-1]
    def dfs(self,s,path,results):
        if not s:
            results.append(path)
            return
        for i in range(1,len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], path+[s[:i]], results)
    def partition(self, s: str) -> List[List[str]]:
        results=[]
        self.dfs(s, [], results)
        return results

