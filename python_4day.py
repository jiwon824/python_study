#실습1 윤년 판단 프로그램

while True :
    year=int(input("연도를 입력하세요:"))
    
    #윤년 조건
    condition= (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    #0을 누르면 프로그램 종료
    if(year==0):
        print("프로그램 종료")
        break

    elif (year>0) and (condition):
        print(year, "은 윤년입니다.")
        
    elif (year>0) and (not condition):
        print(year, "은 윤년이 아닙니다.")
    
    else:
        print("잘못된 년도 입력입니다.")
        
