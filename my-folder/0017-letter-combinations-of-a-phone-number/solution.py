class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        letters={"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        def backtrack(index,curString):
            if len(curString)==len(digits):
                res.append(curString)
                return
            for c in letters[digits[index]]:
                backtrack(index+1,curString+c)
        if digits:
            backtrack(0,"")
            return res
