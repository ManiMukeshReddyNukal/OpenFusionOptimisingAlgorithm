class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mapping=defaultdict(list)
        for piece in pieces:
            mapping[piece[0]]=piece
        idx=0
        while idx<len(arr):
            if arr[idx] not in mapping:
                return False
            array=mapping[arr[idx]]
            for num in array:
                if num!=arr[idx]:
                    return False
                idx+=1
        return True
