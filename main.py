T= int(input())
for i in range(T):
  H, W,N=map(int, input().split())
  if W>=10:
    r=N%H*100
  else:
    r=N%H*10
  print(r+N//H+1)


  #print(N%H,N//H+1)
  #N//H=열수, N%H=층수