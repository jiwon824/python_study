score=int(input("성적을 입력하시오:"))

#90점 이상

if score>= 90:
    print("학점A")
    
#80점 이상 90점 미만
elif score>=80:
    print("학점B")
    
#70점 이상 80점 미만
elif score>=70:
    print("학점C")
    
#60점 이상 70점 미만
elif score>=60:
    print("학점D")
    
#60점 미만
else :
    print("학점F")
