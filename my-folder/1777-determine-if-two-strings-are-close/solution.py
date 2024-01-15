import collections

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        mp1 = collections.Counter(word1)
        mp2 = collections.Counter(word2)
        if mp1.keys() != mp2.keys():
            return False
        l1 = list(mp1.values())
        l2 = list(mp2.values())
        l1.sort()
        l2.sort()
        return l1 == l2

