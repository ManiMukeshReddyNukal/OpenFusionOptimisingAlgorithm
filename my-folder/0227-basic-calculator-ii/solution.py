class Solution:
    def calculate(self, s: str) -> int:
        arr=[]
        smb="+"
        prefix=0
        for ch in s+"+":
            if ch.isdigit():
                prefix=prefix*10+int(ch)
            elif ch in "+-/*":
                if smb=="+":
                    arr.append(prefix*1)
                    prefix=0
                elif smb=="-":
                    arr.append(prefix*-1)                    
                elif smb=="*":
                    num=arr.pop()
                    arr.append(num*prefix)
                elif smb=="/":
                    num=arr.pop()
                    if num<0:
                        arr.append(-1*(abs(num)//prefix))
                    else:
                        arr.append((abs(num)//prefix))
                smb=ch
                prefix=0
        arr.append(prefix)
        return sum(arr)
