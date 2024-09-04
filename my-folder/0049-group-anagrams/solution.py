class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dit=defaultdict(list)
        for str in strs:
            count=[0]*26
            for c in str:
                count[ord(c)-ord('a')]+=1
            dit[tuple(count)].append(str)
        return dit.values()
