# 게임 개발 / pg.118
from sys import stdin

N,M=map(int,stdin.readline().split())
A,B,D=map(int,stdin.readline().split())

map=[list(map(int,stdin.readline().split()))for i in range(M)]

map[A][B]=-1

# 0-> 3 -> 2 -> 1 ->0 .....
arr_direct= [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turnLeft(D):
    if D==0:
        return 3
    else : return D-1

count=1
turnTime=0
while True:

    if turnTime==4:
        # 회전하지 않음
        nA, nB = A - arr_direct[D][0], B - arr_direct[D][1]
        if not 0 <= nA < N and 0 <= nB < M or map[nA][nB]==1: break
        else:
            A, B = nA, nB
            turnTime=0
            continue

    # 회전
    D=turnLeft(D)
    # 위치
    nA,nB=A+arr_direct[D][0],B+arr_direct[D][1]

    # 이동할수 없어
    if not 0<=nA<N and 0<=nB<M or not map[nA][nB]==0:
        turnTime+=1
    else:
        count+=1
        map[nA][nB] = -1
        A, B = nA, nB
        turnTime=0

print(map)
print(count)