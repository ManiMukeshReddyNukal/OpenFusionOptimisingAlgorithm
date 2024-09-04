class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        out=[]
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(index,currpath):
            if index==len(digits):
                out.append("".join(currpath))
                return
            for letter in letters[digits[index]]:
                currpath.append(letter)
                backtrack(index+1, currpath)
                currpath.pop()
        backtrack(0, [])
        if len(digits)==0:
            return []
        return out
