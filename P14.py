ys,sa=map(int,input().split())
ls=list(map(int,input().split()))
ys=[]
ls.insert(0,0)
for a in range(sa):
     v=[]
     s=0
     y,x=map(int,input().split())
     for b in range(y,x+1):         
         s^=ls[b]     
     ys.append(s)
for c in ys:
    print(c)
