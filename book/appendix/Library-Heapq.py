####################################################
print ('[ Heapq ] - 파이썬의 힙은 최소힙으로 구성되어 있으므로 단순히 원소를 힙에 넣었다가 빼는 것만으로도 오름차순 정렬이 완료된다.')
import heapq

# iterable을 입력받아 heap에 저장할 리스트와 정렬 결과를 저장할 리스트를 초기화한다
def heapsort(iterable):
    h = []
    result = []

    # iterable의 값을 하나씩 가져와 heap에 추가한다
    for value in iterable:
        heapq.heappush(h, value)

    # heap의 원소를 하나씩 꺼내서 정렬 결과 리스트에 추가한다
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    # 정렬된 결과 리스트를 반환한다
    return result

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]), end='\n\n')    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

####################################################
print('[ 최대 힙 구현 ] - 기본적으로는 최대 힙을 제공하지 않음')
import heapq

def heapsort(iterable):
    h = []
    result = []

    # 모든 원소의 부호를 바꿔 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)

    # 힙에 삽입 된 원소의 부호를 다시 바꿔 결과에 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))