####################################################
print ('[ collections - deque ] - 큐')
print('기본 리스트 자료형은 첫번째 원소를 추가, 삭제 시 시간 복잡도가 O(N), deque는 O(1) 대신 인덱싱, 슬라이싱 불가능, 스택 혹은 큐 자료구조의 대용으로 사용 가능')
from collections import deque

data = deque([2, 3, 4])
data.appendleft(1)    # 가장 앞쪽 원소에 삽입 (큐)
data.append(5)    # 가장 뒤쪽 원소에 삽입 (스택)

print(data)    # deque([1, 2, 3, 4, 5])
print(list(data))    # 리스트 자료형으로 변환 | [1, 2, 3, 4, 5]

####################################################
print ('\n[ collections - Counter ] - 등장 횟수 카운팅')
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['red'])
print(counter['blue'])
print(counter)
print(dict(counter))   # 사전 자료형으로 변환
