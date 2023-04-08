####################################################
print('[ 입력을 위한 전형적인 소스코드 ]')

print('데이터의 개수 입력: ', end='')
n = int(input())

# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))
print(data)

# 내림차순
data.sort(reverse = True)
print(data, end='\n\n')

####################################################
print('[ 공백을 기준으로 구분하여 적은 수의 데이터 입력 ]')

print('n, m, k를 공백으로 구분하여 입력: ', end='')
n, m, k = map(int, input().split())

print(n, m, k, end ='\n\n')

####################################################
print('[ readline() 사용 소스코드 예시 | print()보다 빠른 입력 방식 ]')

import sys

print('문자열 입력받기: ', end='')
data = sys.stdin.readline().rstrip()    # rstrip() -> 공백 문자 제거
print(data)
