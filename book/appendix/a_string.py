####################################################
print('[ 문자열 자료형 ]')

data = '"Hello world"'
print(data)

data = "Don't you know \"Python\"?"
print(data)

####################################################
print('\n[ 문자열 연산 ]')

a = "Hello"
b = "World"
print(a + " " + b)
print(a * 3)

# 문자열은 내부적으로 리스트와 같이 처리 됨, 인덱싱과 슬라이싱 가능
a = "ABCDEFG"
print(a[0])
print(a[2 : 4])

####################################################
print('\n[ 튜플 자료형 ]')
# 리스트와 흡사하지만, 한 번 선언된 값을 바꿀 수 없다는 차이가 있음
# 리스트는 [] 대괄호로 선언 하지만 튜플은 () 소괄호를 이용
# 튜플 자체의 인덱스는 수정 할 수 없지만, 튜플 내부의 리스트 값은 변경 할 수 있음

a = (1, 2, 3, 4)
print(a)

# 인덱스 값을 바꾸려 하면 에러 발생
# a[0] = 99

list1 = [1,2,3]
list2 = [4,5,6]
tuple = (list1,list2)
print(tuple)
tuple[0][0] = 99
print(tuple)

# 인덱스 값을 바꾸려 하면 에러 발생
# tuple[0] = [7,8,9]

####################################################
print('\n[ 사전(딕셔너리) 자료형 ]')

data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'
print(data)

# 리스트, 문자열, 튜플 등 순차적인 정보를 담는 자료형을 iterable 자료형이라 한다.
# in 문법은 이런 iterable 자료형에 모두 사용이 가능하다.
if '사과' in data:
    print('사과를 키로 가지는 데이터가 존재합니다!')

####################################################
print('\n[ 사전(딕셔너리) 자료형 관련 함수 ]')

data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'coconut'

# 키 데이터만 담은 리스트
key_list = data.keys()
print(key_list)

value_list = data.values()
print(value_list)

# 각 키에 따른 값을 하나씩 출력하기
for key in key_list:
    print(data[key])