from sys import stdin

num=int(stdin.readline())

def perHour3():
    count=0
    for i in range(60):
        for j in range (60):
            if '3' in str(i)+str(j):
                count+=1
    return count

if num<3:
    print(perHour3()*(num+1))
else:
    print(perHour3()*num+60*60)