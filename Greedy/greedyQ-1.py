# pg311
# 정당성?
# 그룹을 매핑하기 위해서는 공포도가 낮은 사람부터 집어 넣으면 돼
# 공포도가 낮은 사람이 개별적인 그룹을 가질때 개수가 더 많아지니까

from sys import stdin

_=int(stdin.readline())
arr=list(map(int,stdin.readline().split()))
arr.sort()

ans=0
cnt=0
for i in arr:
    cnt+=1
    if cnt==i:
        ans+=1
        cnt=0
print(ans)
