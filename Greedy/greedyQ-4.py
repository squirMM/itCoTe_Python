# pg314
# 정당성?
# 특정 숫자를 만들 수 있는가? 를 확인하면 돼

from sys import stdin

_=int(stdin.readline())
coin=list(map(int,stdin.readline().split()))
coin.sort()

# allN=[i for i in range (1,1000001)]
# makeN=[]
#
# for i in range(len(coin)):
#     coinM=coin[i]
#     makeN.append(coinM)
#     for j in range(i+1,len(coin)):
#         coinM+=j
#         makeN.append(coinM)
#
# print(min(list(set(allN)-set(makeN))))

target=1
for c in coin:
    if target<c:
        break
    target+=c

print(target)