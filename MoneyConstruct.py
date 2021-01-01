n,m = map(int,input().split())

arr=[]
dx=[]
d = [0]*100

for i in range(n):
  arr.append(int(input()))
  d[arr[i]-1]=1

for i in range(n,m+1):
  dx.clear()
  for j in arr:
    if d[i-j] != 0:
      dx.append(d[i-j]+1)
    # d[i] = d[i-j]+1
    if i%j == 0:
      dx.append(i//j)
      # d[i]= min(i//j,d[i-j]+1)
    if len(dx)!=0:
      d[i-1]=min(dx)
  if i==m and len(dx)==0:
    print("-1")
  elif i==m and len(dx)!=0:
    print(d[i-1])
