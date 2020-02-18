#TV Class


class TV:
    #CLASS 변수
    TOTAL = 0                   #int
    
    #생성자
    def __init__(self):
        #instance 변수 -> private
        self.channel = 0      #int
        self.volume = 0       #int
        self.state = False    #bool

        TV.TOTAL += 1

    #메소드(함수) 선언
    def showInfo(self):
        print("channel    : ", self.channel)
        print("volume     : ", self.volume)
        print("TV is ON?  : ", self.state)

        #Setter/Getter
    def setChannel(self, channel):
        self.channel = channel
        if (self.state == False):
            print ("setChannel 실패")
            self.channel = 0
        if (channel<0 or channel>999):
            print ("setChannel 실패")
            self.channel = 0

    def setVolume(self, volume):
        self.volume = volume
        if (self.state == False):
            print ("setVolume 실패")
            self.volume=0
        if (self.volume<0 or self.volume>100):
            print ("setVolume 실패")
            self.volume=0

    def getChannel(self):
        return self.__channel

    def getVolume(self):
        return self.volume

    def turnOff(self):
        self.state = False

    def turnOn(self):
        self.state = True
        
    def getState(self):
        return self.state
    
    def channelUp(self):
        self.channel+=1
        if self.channel>999:
            self.channel=0
        
    def channelDown(self):
        self.channel-=1
        if self.channel<0:
            self.channel=999

    def volumeUp(self):
        self.volume+=1
        if self.volume>100:
            self.volume=0

    def volumeDown(self):
        self.volume-=1
        if self.volume<0:
            self.volume=100
        
    #소멸자
    def __del__(self):
        TV.TOTAL -= 1




#main()문

def main():
    tv1 = TV()

    print("TV1's init state")
    tv1.showInfo()
    print()

    tv1.setChannel(100)    #TV 안 켜져있으니까 실패나옴
    tv1.setVolume(100)     #출력 0
    print()
 
    tv1.turnOn()          #TV on
    print("TV1 ON")
    tv1.showInfo()
    print("")


    tv1.setChannel(1001)   #999초과니까 실패
    tv1.setVolume(101)     #100초과니까 실패


    tv1.setChannel(999)   
    tv1.setVolume(50)
    print()

    print("TV1's update state")
    tv1.showInfo()
    print("")

 
    tv1.channelUp()
    tv1.volumeUp()
    
    print("TV1's update state")
    tv1.showInfo()
    print()


    tv1.setChannel(0)
    tv1.setVolume(1)

    print("TV1's update state")
    tv1.showInfo()
    print()


    tv1.channelDown()
    tv1.volumeDown()

    print("TV1's update state")
    tv1.showInfo()
    print()

    tv1.turnOff() 
    print("TV1 OFF")
    tv1.showInfo()

    del tv1


    
main()

        

    
    
	
