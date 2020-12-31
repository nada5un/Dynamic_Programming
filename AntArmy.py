n = int(input())
arr = list(map(int,input().split()))
d = [0]*100

sum = 0

for i in range(n):
  d[i] = arr[i]
  if i>=2:
    d[i] += d[i-2]

print(max(d))