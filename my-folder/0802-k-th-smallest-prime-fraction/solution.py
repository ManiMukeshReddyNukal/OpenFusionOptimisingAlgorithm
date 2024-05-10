class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        left=0
        right=1.0
        while left<right:
            mid=(left+right)/2
            max_fraction=0.0
            max_num_index=0
            max_den_index=0
            total_small_fractions=0
            j=1
            for i in range(n-1):
                while j<n and arr[i]>=mid*arr[j]:
                    j+=1
                total_small_fractions+=(n-j)
                if j==n:
                    break
                fraction=arr[i]/arr[j]
                if fraction>max_fraction:
                    max_fraction=fraction
                    max_den_index,max_num_index=j,i
            if k==total_small_fractions:
                return [arr[max_num_index],arr[max_den_index]]
            elif k>total_small_fractions:
                left=mid
            else:
                right=mid
        return []


