#원주율, 제곱근을 사용하기 위해 math module import
from math import *

#super_class
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getArea(self):
        pass

    def getPerimeter(self):
        pass


#sub_class_1 사각형 클래스 
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def getArea(self):
        return self.width*self.height

    def getPerimeter(self):
        return 2*(self.width + self.height)


#sub_class_2 원 클래스 
class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def getArea(self):
        return round( pi * (self.radius**2) , 4 )

    def getPerimeter(self):
        return round( 2 * pi * self.radius , 4 )


#sub_class_3 삼각형 클래스
class Triangle(Shape):
    def __init__(self, x, y, sideA, sideB, sideC):
        super().__init__(x, y)
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    def getArea(self):
        s = (self.sideA + self.sideB + self.sideC) / 2
        area = sqrt( s * (s - self.sideA) * (s - self.sideB) * (s - self.sideC) )
        return round( area, 4 )
        
    def getPerimeter(self):
        return self.sideA + self.sideB + self.sideC



#main 함수
def main():
    #사용할 file open 
    f_r = open("data.txt", "r")
    f_w = open("result.txt", "w")


    #모든 라인을 lines list에 저장
    lines = f_r.readlines() 


    #for문 : 한 라인씩 모든 라인을 처리 하기 위해 사용
    for line in lines:
        
        #line string 끝에 포함되는 "\n" 제거
        line = line.rstrip()
        
        #" "으로 분리하여 data list에 저장
        data = line.split(" ")
        

        #if-elif-else문 : 각 각의 도형에 따라 넓이, 둘레를 계산하기 위해 사용
        if data[0] == "rectangle" :
            r = Rectangle(0, 0, int(data[1]), int(data[2]))
            f_w.write("가로 세로 %d %d 인 사각형의 " %(int(data[1]), int(data[2])) )
            f_w.write("면적: " + str(r.getArea()) + ", 둘레: " + str(r.getPerimeter()) )
            f_w.write("\n\n")
        
        elif data[0] == "circle" :
            c = Circle(0, 0, int(data[1]))
            f_w.write("반지름 %d 인 원의 " %int(data[1]))
            f_w.write("면적: "+str(c.getArea()) + ", 둘레: " + str(c.getPerimeter()) )
            f_w.write("\n\n")
            
        elif data[0] == "triangle" :
            t = Triangle(0, 0, int(data[1]), int(data[2]), int(data[3]))
            f_w.write("세 변 %d %d %d인 삼각형의 " %(int(data[1]), int(data[2]), int(data[3])))
            f_w.write("면적: "+ str(t.getArea()) + ", 둘레: " + str(t.getPerimeter()) )
            f_w.write("\n\n")

        else:
            pass


    #open한 file 모두 close
    f_r.close()
    f_w.close()



#main함수 실행
main()
