s=int(input("enter a number:"))
t=str(s)
res=[]
for i in range(str(len(s))):
    res.append(s[i])
    res.reverse()
res= res+1
print(res)

    