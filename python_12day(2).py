#문제 2-9 x라는 변수에 'abcdef'라는 문자열이 바인딩돼 있다고 했을 때 x의 값을 'bcdefa'로 변경해 보세요.

x = 'abcdef'
print(x, ", x를 변경합니다.")
x = x[1:]+'a'
print(x)
