class Solution:
    def simplifyPath(self, path: str) -> str:
        s=[]
        for c in path.split("/"):
            if c == "..":
                if s:
                    s.pop()
            elif c=="." or not c:
                continue
            else:
                s.append(c)
        return "/"+"/".join(s)
