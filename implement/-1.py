from sys import stdin

n=int(stdin.readline())
move=list(stdin.readline().split())
x,y=1,1

def check(nx,ny):
    if 0<nx<=n and 0<ny<=n:
        return True
    else:
        return False

def moving(direct):
    dy=[-1,1,0,0]
    dx=[0,0,-1,1]
    m=0
    if "L" == direct:m=0
    elif direct=="R":m=1
    elif direct=="U":m=2
    elif direct=="D":m=3

    if check(x+dx[m],y+dy[m]):
        return x + dx[m], y + dy[m]
    else:
        return x,y

for d in move:
    x,y=moving(d)

print(x,y)