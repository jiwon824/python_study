#쇼핑 리스트 선언
shopping_list=['우유', '계란', '치즈', '버터', '크림']
print ("쇼핑 리스트:", shopping_list)

#in 사용
item1= input('무엇을 사시겠습니까?')

if item1 in shopping_list :
    print('쇼핑 리스트에 있습니다.')
else:
    print('쇼핑리스트에 없습니다.')

print("")

#not in 사용
item2=input('무엇을 사시겠습니까?')

if item2 not in shopping_list:
    print("쇼핑 리스트에 없습니다.")
else:
    print("쇼핑 리스트에 있습니다.")
