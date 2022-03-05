# 럭키스트레이트 / pg321
from sys import stdin

#문자열
N=list(map(int,stdin.readline().split()))
half=len(N)//2

if sum(N[:half])==sum(N[half:]):
    print("LUCKY")
else:
    print("READY")