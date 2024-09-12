class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowset=set(allowed)
        count=0
        for word in words:
            s=set(word)
            if not s-allowset:
                count+=1
        return count

