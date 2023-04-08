####################################################
print('[ 내장 함수 ]')
print('별도의 import 명령어 없이 바로 사용할 수 있는 내장 함수', end='\n\n')

print('sum() : 리스트와 같은 iterable 객체가 입력으로 주어졌을 때 모든 원소의 합을 반환')
print(sum([1,2,3,4,5]), end='\n\n') # 15

print('min() : 파라미터 2개 이상이 들어오면, 그 중 가장 작은 값을 반환')
print(min(7, 3, 5, 2), end='\n\n')  # 2

print('max() : 파라미터 2개 이상이 들어오면, 그 중 가장 큰 값을 반환')
print(max(7, 3, 5, 2), end='\n\n')  # 7

print('eval() : 수학 수식이 문자열 형식으로 들어오면 해당 수식 계산 결과를 반환')
print(eval('(3 + 5) * 7'), end='\n\n')  # 56

print('sorted() : iterable 객체의 정렬 결과를 반환, reverse 속성')
print(sorted([9,1,8,5,4]))  # 오름차순 정렬 | 1, 4, 5, 8, 9
print(sorted([9,1,8,5,4], reverse = True), end='\n\n')  # 내림차순 정렬 | 9, 8, 5, 4, 1

# 리스트의 원소로 리스트나 튜플이 존재할 때 특정한 기준에 따라서 정렬을 수행할 수 있다.
# 정렬 기준은 key 속성을 이용해 명시할 수 있다.
print('sorted() : iterable 객체의 정렬 결과를 반환, key 속성 | 튜플의 두번째 원소로 정렬')
list = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
print(sorted(list, key = lambda x: x[1], reverse=True), end='\n\n')    # [('이순신', 75), ('아무개', 50), ('홍길동', 35)]

print('iterable 객체는 기본적으로 sort() 메소드를 내장하고 있어서 굳이 sorted() 함수를 사용하지 않아도 정렬 할 수 있음')
print('이 경우 리스트 객체의 내부 값이 정렬된 값으로 바로 변경 된다.')
list2 = [9,1,8,5,4]
list2.sort()
print(list2)    # 오름차순 정렬 | [1, 4, 5, 8, 9]
