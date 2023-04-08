####################################################
# [ 조건문 ]

score = 69

if score >= 90:
    print('90점 이상 학점: A')
elif score >= 80:
    print('80점 이상 학점: B')
elif score >= 70:
    print('70점 이상 학점: C')
else:
    print('그 외 학점: F')

print()
####################################################

score = 90

if score >= 70:
    print('성적이 70점 이상입니다.')
    if score >= 90:
        print('90점 이상이라니 우수합니다!')
else:
    print('성적이 70점 미만입니다.')
    print('조금 더 분발하세요.')

print('프로그램을 종료합니다.')

####################################################
print('\n[ 비교 연산자 ]')
print('X == Y\nX != Y\nX > Y\nX < Y\nX >= Y\nX <= Y')

print('\n[ 논리 연산자 ]')
print('X and Y\nX or Y\nnot X')

print('\n[ 파이썬의 기타 연산자 ]')
print('X in 리스트')
print('X not in 문자열')

####################################################
print('\n[ 조건문 pass ]')

score = 70

if score >= 80:
    pass # 나중에 작성할 코드 영역으로 남겨두기 (pass 처리)
else:
    print('성적이 80점 미만입니다')

# 조건문에서 실행 될 코드가 한 줄일 경우 줄 바꿈 안하고도 표현 가능
if score >= 80: result = 'Success'
else: result = 'Fail'
print(result)

# 조건부 표현식으로 한줄 작성
result = 'Success' if score >= 80 else 'Fail'
print(result)

a = [1,2,3,3,4,5,5,5]
remove_set = {3,5}
result = [i for i in a if i not in remove_set]
print('조건부 표현식으로 또 다른 리스트 생성: ', result)

# 파이썬은 조건문 안에서 수학의 부등식을 그대로 사용할 수 있다
# x > 0 and x < 20
# 0 < x < 20
