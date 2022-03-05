import heapq


def solution(food_times, k):
    # k초전에 종료될 경우
    if sum(food_times)<=k:
        return -1

    # 우선순위큐를 만드는 과정
    q=[]
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i],i+1))

    # 먹기 위해 사용한 시간
    sum_value=0
    # 직전에 다먹은 음식 시간
    previous=0
    length=len(food_times)

    # (sum_value+(현재음식시간-이전음식시간)*남아있는음식개수)가 k보다 작은지
    while sum_value+((q[0][0]-previous)*length)<=k:
        now=heapq.heappop(q)[0]
        sum_value+=(now-previous)*length
        previous=now
        length-=1

    # 남은 음식 중 몇 번째 음식인지 확인
    result=sorted(q,key=lambda x: x[1])
    return result[(k-sum_value)%length][1]