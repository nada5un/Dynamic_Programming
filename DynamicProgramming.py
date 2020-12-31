# 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화 
d = [0]*100

# 피보나치 함수 by 재귀함수 => 탑다운 방식 
def pibo1(x):
  print('f('+str(x)+')',end= ' ')
  if x==1 or x==2:
    return 1
  if d[x] !=0:
    return d[x]
  d[x] = pibo1(x-1)+pibo1(x-2)
  return d[x]

# 피보나치 함수 by 반복문 => 보텀업 방식 
def pibo2(x):
  # DP 테이블 초기화 
  d = [0]*100
  d[1]=1
  d[2]=1
  n=6
  for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]
  print("pibo2(6): ",d[n])

print("\npibo1(6): ",pibo1(6))
pibo2(6)