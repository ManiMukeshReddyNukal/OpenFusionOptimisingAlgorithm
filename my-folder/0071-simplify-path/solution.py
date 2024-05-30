class Solution:
    def simplifyPath(self, path: str) -> str:
        di=path.split("/")
        q=[]
        for d in di:
            if d:
                if d==".." :
                    if len(q)>0:
                        q.pop()
                elif d==".":
                    pass
                else:
                    q.append(d)

        return "/"+"/".join(q)

