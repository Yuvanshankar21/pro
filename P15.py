y=int(input())
s=list(map(int,input().split()))
l1=[]
for i in s:
  sa=bin(i)
  l1.append(sa)
l2=sorted(l1)
l2.reverse()
for j in l2:
  print(int(j,2))
