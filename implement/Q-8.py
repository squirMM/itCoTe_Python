# 문자열 재정렬 / pg.322
from sys import stdin

S=stdin.readline().rstrip()

S=sorted(S)
ans=""
num=0

for s in S:
    if s.isalpha():
        ans+=s
    else:
        num+=int(s)

print(ans+str(num))