####################################################
print('[ 집합 자료형 ]')

# 집합 자료형 초기화 방법 1
data = set([1,1,2,3,4,5])
print(data)

# 집합 자료형 초기화 방법 2
data = {1,1,2,3,4,5}
print(data)

####################################################
print('\n[ 집합 자료형의 연산 ]')

a = {1,2,3,4,5}
b = {3,4,5,6,7}

print('합집합: ', a | b)
print('교집합: ', a & b)
print('차집합: ', a - b)

####################################################
print('\n[ 집합 자료형 관련 함수 ]')
data = set([1, 2, 3])
print(data)

data.add(4)
print('새로운 원소 추가: ', data)

data.update([5, 6])
print('새로운 원소 여러개 추가: ', data)

data.remove(3)
print('특정 값을 갖는 원소 삭제: ', data)