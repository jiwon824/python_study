from math import *

class Shape:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def area(self):         #부모클래스의 넓이와 둘레는
        pass
    def perimeter(self):    #구하지 않고 그냥 넘어간다는 의미
        pass


    def setMake(self, make):
        self.make=make
    def getMake(self):
        return self.make
    def getDesc(self):
        return "도형=("+str(self.x)+","+\
                               str(self.y)+")"
                            

class Rectangle(Shape): #Shape 클래스의 자식 Rectangle
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w=w
        self.h=h

    def area(self):
        return self.w*self.h
    def perimeter(self):
        return 2*(self.w+self.h)

    def getDesc(self):
        return "사각형=("+str(self.x)+","+\
                               str(self.y)+","+\
                               str(self.w)+","+\
                               str(self.h)+")"

class Circle(Shape):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r=r

    def area(self):
        return pi*self.r**2

    def perimeter(self):
        return 2*pi*self.r

    def getDesc(self):
        return "원=("+str(self.x)+","+\
                               str(self.y)+","+\
                               str(self.r)+")"

class Triangle(Shape):
    def __init__(self, x, y, a, b, c):
        super().__init__(x, y)
        self.a=a
        self.b=b
        self.c=c
        
        self.s=(self.a+self.b+self.c)/2
        
    def area(self):
        return sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))

    def perimeter(self):
        return self.a+self.b+self.c

    def getDesc(self):
        return "삼각형=("+str(self.x)+","+\
                               str(self.y)+","+\
                               str(self.a)+","+\
                               str(self.b)+","+\
                               str(self.c)+")"

def main():
    #사각형 객체생성
    myRectangle=Rectangle(3, 4, 5, 6)

    myRectangle.setMake(5)
    myRectangle.setMake(6)
    print(myRectangle.getDesc())

    #사각형의 둘레, 넓이
    print("사각형의 넓이는 "+str(myRectangle.area())+"이다.")
    print("사각형의 둘레는 "+str(myRectangle.perimeter())+"이다."+"\n")



    #원 객체 생성
    myCircle=Circle(3, 4, 5)

    myCircle.setMake(5)
    print(myCircle.getDesc())

    #원의 둘레, 넓이
    print("원의 넓이는 "+str(myCircle.area())+"이다.")
    print("원의 둘레는 "+str(myCircle.perimeter())+"이다."+"\n")



    #삼각형 객체생성
    myTriangle=Triangle(3, 4, 1, 1, 1)

    myTriangle.setMake(1)
    myTriangle.setMake(1)
    myTriangle.setMake(1)
    print(myTriangle.getDesc())

    #삼각형의 둘레, 넓이
    print("삼각형의 넓이는 "+str(myTriangle.area())+"이다.")
    print("삼각형의 둘레는 "+str(myTriangle.perimeter())+"이다."+"\n")

    

main()



