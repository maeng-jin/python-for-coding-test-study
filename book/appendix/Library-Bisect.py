####################################################
print ('[ bisect ] - 이진 탐색')
print('정렬된 리스트[1,2,4,4,8]에 새로운 데이터 \'4\'를 삽입하려 할때 좌,우 인덱스 값 찾기')
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))    # 2
print(bisect_right(a, x))    # 4

####################################################
print ('\n[ bisect ] - 값이 [bisect_left, bisect_right]인 데이터의 개수를 반환하는 함수')
from bisect import bisect_left, bisect_right

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    # right_index와 left_index를 빼서 left_value 이상 right_value 이하인 값들의 개수를 구한다.
    return right_index - left_index

# 값이 4인 데이터의 개수
print(count_by_range(a, 4, 4))

# 값이 [-1, 3] 범위에 있는 데이터 개수
print(count_by_range(a, -1, 3))
