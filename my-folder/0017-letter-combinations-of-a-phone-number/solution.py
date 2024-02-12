class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans=[]
        letters={"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def recur(index,str):
            if len(str)==len(digits):
                ans.append(str)
                return
            for c in letters[digits[index]]:
                recur(index+1,str+c)
        if digits:
            recur(0,"")
        return ans
