# 정당성?
# 큰수를 겹치지 않는 선에서 더하는게 당연히 가장 큰 값을 불러 올 것이다.
from sys import stdin

n, m, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

# 답안 1
# 이 답안은 시간 초과를 불러 일으킬수 있다.
arr.sort()

ans1 = 0
for i in range(1, m + 1):
    if i % k == 0:
        ans1 += arr[-2]
    else:
        ans1 += arr[-1]

print(ans1)

# 답안 2
# 규칙성을 파악하여 시간초과가 일어나지 않게 함

# 예를 들어 k=3 이라면, 제일 큰 수*3 + 두번째로 큰수 가 하나의 묶음이 되게된다.
# 그러므로 제일 큰 수는 (묶음이 반복되는 횟수*k)+나머지 개수 만큼 나와야한다.

count=m//(k+1)*k
count+=m%(k+1)

ans2=count*arr[-1]+(m-count)*arr[-2]

print(ans2)
