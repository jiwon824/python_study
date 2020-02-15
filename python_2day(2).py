#실습2 형변환을 이용한 소수점 자리수 제한
from math import*

print("math 모듈에서 제공하는 원주율 값:", pi)
print("원주율의 자료형:", type(pi))

#슬라이싱을 위해 str형태로 형변환, 자른 값을 pi에 저장
pi=str(pi)
pi=pi[0:6]

print("\n소수점 네번째 자리까지의 원주율 값:", pi)

#저장한 pi값을 실수형으로 다시 변환, 계산
pi=float(pi)
print("2*pi =", 2*pi)


#str형태로 형변환해야 오류가 안 남
