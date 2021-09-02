#class 선언하기
#객체 생성 전에 미리 class를 선언해야 함
'''
* class 도 변수/함수와 마찬가지로 유일한 이름을 지어줘야 함
* class 에 attribute/method를 아직 안넣은 상태이므로, 클래스에 내용이 없기에 임의로 pass 를 넣어 클래스 선언이 끝났음을 알려줌
  - pass는 아무것도 수행하지 않는 문법, 임시 코드 작성시 주로 사용
* 클래스명은 !!!!!!!1각 단어의 첫 문자를 대문자로 하는 CapWords!!!!!!!!! 방식을 사용


class Quadrangle:
    pass

class SingleWord:
    pass
'''

class Quadrangle:
    #attribute 넣어보기(만들고자 하는 "속성" 생각해보기)
    #일반적으로 속성은 init이라는 함수 안에 넣는 경우가 많음
    #클래스 내에서 속성값을 이용할 때도 반드시! self. 을 붙여줘야 한다!
    def __init__ (self,width,height,color):
        self.width=width
        self.height=height
        self.color=color

    #method 추가하기
    #따로 파라미터가 없어도! self는 인자로서 반드시! 써줘야 한다!
    def get_area(self): #넓이를 리턴하는 메서드
        return self.width*self.height

    def set_area(self,data1,data2): #너비와 높이 속성만 새로 정하는 메서드
        self.width=data1
        self.height=data2


#객체 디폴트로 생성하기
#square=Quadrangle()

#속성으로 생성하기
square1=Quadrangle(12,12,'red')
square2=Quadrangle(10,10,'blue')

#객체에서 속성 값에 접근하기
square1.color #red
square2.color='red' #이렇게 속성 값을 바꿀 수도 있음
print(square2.color) #red