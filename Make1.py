n = int(input())

d = [0]*100
dx = []
d[1]=0
d[2]=1
d[3]=1
d[4]=2
d[5]=1

# 숫자까지 1부터 시작해서 만들 수 있는 최소 연산을 저장 
count = 0

for i in range(6,n+1):
  dx.clear()
  if i %5 == 0:
    dx.append(d[i//5]+1)
  elif i% 3 == 0:
    dx.append(d[i//3]+1)
  elif i% 2 == 0:
    dx.append(d[i//3]+1)
  else:
    dx.append(d[i-1]+1)
  d[i]= min(dx)
  
print(d[n])