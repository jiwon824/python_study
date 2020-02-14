from math import *

#사용자가 각 도형의 길이를 입력하도록
r=input("원의 반지름의 길이 :")
a=input("정삼각형 한 변의 길이: ")

#입력된 변수를 정수로 바꾼다.
r=int(r)
a=int(a)

#내장 함수와 입력된 변수를 이용한 계산 출력
print("원의 둘레=", 2*pi*r)
print("원의 넓이=", pi*r**2)

print("정삼각형의 둘레=", a*3)
print("정삼각형의 넓이=", sqrt(3)/4*a**2)


#루트3 - 내장 함수 sqrt호출
sqrt(3)
#원주율 - 내장 상수 pi호출
pi
