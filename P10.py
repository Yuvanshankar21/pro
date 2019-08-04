yu=int(input())
sa=[int(i) for i in input().split()]
c=0
for i in range(yu):
   for j in range(i):
      if sa[j]<sa[i]:
         c+=sa[j]
print(c)
