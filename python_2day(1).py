#실습1 간단한 명함 제작 프로그램

#input을 이용해 사용자에게 이름과 번호를 입력받음
full_name = input("영문 이름을 입력하세요 :")
phone_number = input("전화번호를 입력하세요 :")

#입력된 이름을 대문자로 저장
FULL_NAME=(full_name.upper())

#슬라이싱을 이용해 성과 이름을 분리, 휴대폰 번호 사이에 '-' 넣기
print("+"*35)
print("Last Name :" ,FULL_NAME[-4:])
print("First Name :" ,FULL_NAME[0:-4])
print("Phone Number :", phone_number[0:3]+"-"+phone_number[3:7]+"-"+phone_number[7:])
print("+"*35)
