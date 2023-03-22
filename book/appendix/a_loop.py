####################################################
print('[ 반복문 : while ]')

i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    result += i
    i += 1

print(result)
print()

####################################################
print('[ 반복문 : while (홀수의 합) ]')

i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1

print(result)
print()

####################################################
print('[ 반복문 : for (인수 2개) ]')
print('리스트, 튜플, 문자열 등으로 반복문을 돌리 수 있음')

result = 0

# i는 1부터 9까지의 모든 값을 순회
# 시작 값(1)은 범위에 포함 되고
# 끝 값(10)은 범위에 포함 되지 않음
# 1 ~ 9
for i in range(1, 10):
    result += i

print(result)

####################################################
print('[ 반복문 : for (인수 1개) ]')
print('range 함수에 인수를 하나만 넘기면 시작 값은 자동으로 0 | 리스트 전체를 반복할때 사용')

scores = [90, 85, 77, 65, 97]

for i in range(5):
    # print(i)
    if scores[i] >= 80:
        print(i + 1, '번 학생은 80점 이상 합격입니다.')
print()

####################################################
print('[ 반복문 : for (continue) ]')
print('반복문의 처음으로 돌아감')

scores = [90, 85, 77, 65, 97]
black_list = {2, 4} # set 자료형 (중복 x)

for i in range(5):
    if i + 1 in black_list:
        continue
    if scores[i] >= 80:
        print(i + 1, '번 학생은 80점 이상 합격입니다.')
print()

####################################################
print('[ 반복문 : for (2중 반복문) ]')

# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(i, 'x', j, '=', i * j)
    print()
