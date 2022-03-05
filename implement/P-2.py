# 왕실의 나이트 / pg.115

from sys import stdin

night=stdin.readline().rstrip()
map_dict= dict(a=1, b=2, c=3, d=4, e=5, f=6, g=7, h=8)

y= int(map_dict[night[0]])
x= int(night[1:])

cnt=0
dx=[2,-2,2,-2,1,-1,1,-1]
dy=[1,-1,-1,1,2,-2,-2,2]

for i in range(8):
    if 0<x+dx[i]<=8 and 0<y+dy[i]<=8: cnt+=1

print(cnt)