#List 선언
A=[1, 3, 5, 7, 8, 9]
print("초기 List:", A, "\n")

#List 요소 추가, 삽입
A.append(4)
print("append(4)의 결과:", A, "\n")
A.insert(1, 2)
print("insert(1, 2) 결과:", A, "\n")

#List 확장
A.extend([5, 6])
print("extend[5, 6]의 결과:", A, "\n")

#List 요소 제거
A.remove(5)
print("remover(5) 결과:", A, "\n")
del A[3:5]
print("del A[3:5] 결과:", A, "\n")
A.pop(3)
print("pop(3)결과:", A, "\n")

#List 뒤집기
A.reverse()
print("reverse() 결과:", A, "\n")

#List 정렬
A.sort()
print("sort()결과:", A, "\n")
