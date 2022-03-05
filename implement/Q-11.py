# 뱀 / pg.327 / https://www.acmicpc.net/problem/3190
from sys import stdin
from collections import deque

N = int(stdin.readline())
K = int(stdin.readline())

Dmap = [[0] * N for i in range(N)]
for i in range(K):
    a, b = map(int, stdin.readline().split())
    Dmap[a- 1][b - 1] = -1

L = int(stdin.readline())
times={}
for i in range(L):
    num, s = stdin.readline().split()
    times[int(num)]=s


def boundary(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    else:
        return False


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]



def move(direction, c):
    if c == "D":
        direction = (direction + 1) % 4
    else:
        direction = (direction - 1) % 4
    return direction


x,y=0,0
time = 1
direction = 1
Dmap[x][y]=1
q=deque([[y,x]])
while True:
    # move
    x, y = x + dx[direction], y + dy[direction]
    if boundary(x,y) and Dmap[x][y]!=1:
        if Dmap[x][y] != -1:
            tail_y,tail_x=q.popleft()
            Dmap[tail_y][tail_x]=0
        Dmap[x][y] = 1
        q.append([y,x])
        if time in times.keys():
            direction=move(direction,times[time])
        time += 1
    else:
        break

print(time)
