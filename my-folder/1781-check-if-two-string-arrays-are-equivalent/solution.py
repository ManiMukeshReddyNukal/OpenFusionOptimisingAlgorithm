class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        st="".join(word1)
        st2="".join(word2)
        if st==st2:
            return True
        return False
