path=r"C:\Users\Administrator\Desktop\username.txt"
with open(path,'r')as  f:
    names=f.read().splitlines()
    a=[]
    for name in names:
        a.append(name)
    print(a)
