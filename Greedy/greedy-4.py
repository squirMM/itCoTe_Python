# 정당성?
# 최소 횟수를 구하는 방법인데 나누기를 하는게 횟수를 줄이는 방법임

from sys import stdin

N,K=map(int,stdin.readline().split())

cnt=0
while N>1:
    if N%K==0:
        N=N//K
    else:
        N-=1
    cnt+=1
print(cnt)