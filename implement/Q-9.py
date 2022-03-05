# 문자열 압출 / pg.323 / https://programmers.co.kr/learn/courses/30/lessons/60057

from sys import stdin

s = stdin.readline().strip()

def solution(s):
    arr = []
    arr.append(s)
    for i in range(1, len(s) // 2 + 1):
        compS = ""
        tmp = s[:i]
        count = 1
        for j in range(i, len(s) + 1, i):
            if s[j:j + i] == tmp:
                count += 1
            else:
                if count == 1:
                    compS += tmp
                else:
                    compS += str(count) + tmp
                count = 1
                tmp = s[j:j + i]
            # print(j, s[j:j + i],compS)
        compS += s[len(s) - len(s) % i:]
        if compS != s:
            arr.append(compS)
    arr = sorted(arr, key=lambda x: len(x))
    return len(arr[0])


print(solution(s))
