#문제 2-8 a라는 변수에 'hello world'라는 문자열이 바인딩돼 있다고 했을 때 a의 값을 'hi world'로 변경해 보세요.

a = 'hello world'
print(a, ', a값을 변경합니다.')
a = a[0] + 'i' + a[5:]
print(a)
