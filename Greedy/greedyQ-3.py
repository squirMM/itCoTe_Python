# pg313 / https://www.acmicpc.net/problem/1439
# 정당성?
# 0혹은 1이 연속된 개수를 비교하면 돼 여기서 작은 수가 최소로 뒤집을 수 있는 방법이 된다.

from sys import stdin

numbers = stdin.readline().rstrip()

# 연속된 숫자가 1이라면 0임
cnt=[0]*2
for n in range(len(numbers)):
    if n>0:
       if numbers[n]==numbers[n-1]:
           continue
    cnt[int(numbers[n])]+=1

print(min(cnt))