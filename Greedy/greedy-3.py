from sys import stdin

n,m=map(int,stdin.readline().split())
arr=[]
for _ in range(n):
    data=list(map(int,stdin.readline().split()))
    arr.append(min(data))

print(max(arr))