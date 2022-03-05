# pg312
# 정당성?
# 큰 수를 생성하기 위해서는 0을 제외하고는 모두 곱셈을 하여야한다.

from sys import stdin

numbers = stdin.readline().strip()
ans = 0
for n in numbers:
    if n == '0' or ans==0:
        ans += int(n)
    else:
        ans *= int(n)

print(ans)
