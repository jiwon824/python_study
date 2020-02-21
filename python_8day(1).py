'''
문제에서 오류로 주어진 코드
words = 'Connect Foundation'

if 'F' in words :
    words.lower()
    words[7] = '&'

else :
    print(words)
print(words)
'''

#오류가 안 나게 고친 코드

words = 'Connect Foundation'

if 'F' in words :
    words.lower()
    words = words[:7] + '&' + words[8:]

else :
    print(words)
print(words)
