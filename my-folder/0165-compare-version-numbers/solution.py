class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a=version1.split(".")
        b=version2.split(".")
        n1,n2=len(a),len(b)
        for i in range(max(n1,n2)):
            i1=int(a[i]) if n1>i else 0
            i2=int(b[i]) if n2>i else 0
            if i1!=i2:
                return 1 if i1>i2 else -1
        return 0
