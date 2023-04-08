####################################################
print('[ Itertools ]')
print('반복되는 데이터를 처리하는 기능을 포함한 라이브러리')
print('순열은 순서가 중요한 경우의 수를 계산하고, 조합은 순서가 중요하지 않은 경우의 수를 계산', end='\n\n')

####################################################
print('[ permutations ] - 순열')
print('iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산 | permutations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용')
from itertools import permutations

data = ['A', 'B', 'C']    # 데이터 준비
print(list(permutations(data, 3)), end='\n\n')    # 모든 순열 구하기 | [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

####################################################
print('[ combinations ] - 조합')
print('iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)를 계산 | combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용')
from itertools import combinations

data = ['A', 'B', 'C']    # 데이터 준비
print(list(combinations(data, 2)), end='\n\n')    # 2개를 뽑는 모든 조합 구하기 | [('A', 'B'), ('A', 'C'), ('B', 'C')]

####################################################
print('[ product ] - 중복 허용 순열')
print('permutations와 동일하지만 원소를 중복하여 뽑는다. 뽑고자 하는 데이터의 수를 repeat 속성값으로 넣어준다. | product는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용')
from itertools import product

data = ['A', 'B', 'C']    # 데이터 준비
print(list(product(data, repeat=2)), end='\n\n')    # 2개를 뽑는 모든 순열 구하기(중복 허용) | [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

####################################################
print('[ combinations_with_replacement ] - 중복 허용 조합 ')
print('combinations와 동일하지만 원소를 중복하여 뽑는다. | combinations_with_replacement는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용')
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']    # 데이터 준비
print(list(combinations_with_replacement(data, 2)))
