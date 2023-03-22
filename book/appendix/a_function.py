####################################################
print('[ 함수 ]')

def add(a, b):
    print('더하기 함수 (return 이뜸)')
    return a+b
print(add(3, 7))
print()

def add(c, d):
    print('더하기 함수 (return 없뜸):', c + d)
print()

# 함수를 호출하는 과정에서 다음과 같이 인자(아규먼트)를 넘겨줄 때 파라미터의 변수를 직접 지정해서 값을 넣을 수 있다 (순서 상관 X)
add(d = 3, c = 7)
print()

e = 0
def func():
    # global : 함수 내에서 지역변수를 생성하지 않고 전역 변수에 직접 접근 (코드 가독성이 떨어지고, 버그 위험도가 높아지는 위험이 있음)
    global e
    e += 1
for i in range(10):
    func()
print('더하기 함수 (global 사용):', e)
print()

####################################################
print('[ 람다 표현식 ]')

def add(a, b):
    return a + b
print('일반적인 add() 메서드 사용:', add(3, 7))
print('람다 표현식으로 구현한 add() 메소드:', (lambda a, b : a + b)(3,7))
