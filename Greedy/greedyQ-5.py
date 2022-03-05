# pg315
# 정당성?
# 동일한 무게가 얼마나 있는지만 파악하면 그중에 하나씩 고른다고 생각하면 쉽다.
# 시간 n+m(m-1)/2 이므로 거의 O(n)임

from sys import stdin
n,m=map(int,stdin.readline().split())
arr=list(map(int,stdin.readline().split()))

arrSet=[0]*(m+1)
for x in arr:
    arrSet[x]+=1

result=0
for i in range(1,m+1):
    for j in range(i+1,m+1):
        result+=arrSet[i]*arrSet[j]

print(result)
