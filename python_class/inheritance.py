'''
### 1. Class Inheritance (상속)
  - **추상화(abstraction)**: 여러 클래스에 중복되는 속성 혹은 메서드를 하나의 기본 클래스로 작성하는 작업
  - **상속(inheritance)**: 기본 클래스의 공통 기능을 물려받고, 다른 부분만 추가 또는 변경하는 것
    + 이 때 기본 클래스는 부모 클래스(또는 상위 클래스), Parent, Super, Base class 라고 부름
    + 기본 클래스 기능을 물려받는 클래스는 자식 클래스(또는 하위 클래스), Child, Sub, Derived class 라고 부름
  

### 예: 사각형, 삼각형, 원 클래스
* 공통점과 차이점 찾아보기
  + 사각형: **사각형 이름, 사각형 색**, 사각형 너비/높이, 사각형 넓이
  + 삼각형: **삼각형 이름, 삼각형 색**, 삼각형 한 변 길이, 삼각형 넓이
  + 원: **원 이름, 원 색**, 원 반지름, 원 넓이
  --즉 속성들은 공통적임

  +override==덮어씌우기


#상속하는 방법
* 부모 클래스를 자식 클래스에 인자로 넣으면 상속이 됨!!!!!!!
  - 다음 코드는 __init__(self, name, color) 메서드가 상속되고,
  - self.name과 self.color 도 __init__ 실행시 생성됨
'''

class Figure:
    def __init__(self,name,color):
        self.name=name
        self.color=color


class Quadrangle(Figure):
    def set_area(self,width,height):
        self.width=width
        self.height=height

    def get_info(self):
        print(self.name,self.color,self.width*self.height)



square=Quadrangle('dave','blue') #Quandrangle이 부모 클래스의 생성자(__init__)을 그대로 상속하고 있으므로
#그냥 처음부터 Quadrangle에 __init__이 있었던 것처럼 선언하면 됨
square.set_area(5,5)
square.get_info()




#* 상속 관계인 클래스 확인하기 - 내장함수 issubclass(자식 클래스, 부모 클래스) 사용하기
# Quadrangle 클래스가 Figure 클래스의 자식 클래스인지 확인
print(issubclass(Quadrangle, Figure)) #True


#* 클래스와 객체간의 관계 확인하기 - 내장함수 isinstance(객체, 클래스) 사용하기
figure1 = Figure('figure1', 'black')
square = Quadrangle('square', 'red')

print(isinstance(figure1, Figure)) #true
print(isinstance(square, Figure)) #true
print(isinstance(figure1, Quadrangle)) #false
print(isinstance(square, Quadrangle)) #true


### 또 다른 예: 사람과 학생
# 클래스 선언
class Person:
    def __init__(self, name):
        self.name = name
        
class Student(Person):
    def study(self):
        print (self.name + " studies hard")

class Employee(Person):
    def work(self):
        print (self.name + " works hard")


# 객체 생성
student1 = Student("Dave")
employee1 = Employee("David")

# 객체 실행
student1.study()
employee1.work()


'''### 2. Method Override (메서드 재정의) - 즉 그냥 덮어씌우기 기능이라고 생각하기
* 부모 클래스의 method를 자식 클래스에서 재정의(override)
* 자식 클래스에서 **부모 클래스 method를 재정의**함
* 자식 클래스 객체에서는 재정의된 메소드가 호출됨
* 자식 클래스에서 **부모 클래스의 메서드와 이름만 동일하면 메서드 재정의가 가능함**
  - C++/Java언어 등에서는 메서드와 인자도 동일해야 함 '''


# 클래스 선언
class Person:
    def __init__(self, name):
        self.name = name

    def work(self):
        print (self.name + " works hard")        

class Student(Person):
    def work(self): #오버라이딩
        print (self.name + " studies hard")
    
    def go_to_school(self): #그냥 일반 메서드
        print('Go to school')




'''### 3. 자식 클래스에서 부모 클래스 메서드 호출 (super 와 self)
### super()
 - 자식 클래스에서 부모 클래스의 method를 호출할 때 사용(오버라이딩이 되었어도 부모 클래스에서의 메서드를 호출함)
   - super().부모 클래스의 method명'''

# 클래스 선언
class Person:
    def work(self):
        print('work hard')

class Student(Person):
    def work(self):
        print('Study hard')
        
    def parttime(self):
        super().work() #부모 클래스의 메서드가 호출됨

    def general(self):
        self.work() #self는 c++에서의 this. 즉 자기 자신을 가르킨다
        # 즉 이거는 현재 자기자신(student-자식)의 work 메서드가 호출된다


'''
## 3. 클래스 속성과 메서드
-- 속성(변수)은 클래스 속성과 객체(인스턴스) 속성으로 나눌 수 있음

### 1. 클래스 변수와 인스턴스 변수 (attribute를 한 단계 더 구분해보자)
* 클래스 변수: 클래스 정의에서 메서드 밖에 존재하는 변수
  - !!!!!11해당 클래스를 사용하는 모두에게 공용으로 사용되는 변수!!!!!!
  - 클래스 변수는 클래스 **내외부**에서 "클래스명.변수명" 으로 엑세스 가능

* 인스턴스 변수: 클래스 정의에서 메서드 안에서 사용되면서 "self.변수명"처럼 사용되는 변수
  - 각 객체별로 서로 다른 값을 가짐
  - 클래스 내부에서는 self.인스턴스변수명 을 사용하여 엑세스, 클래스 밖에서는 객체명.인스턴스변수명 으로 엑세스

  즉 클래스 변수는 클래스 내에서의 전역?변수 느낌, 객체 변수는 클래스 내에서의 지역 변수 차이(현재 지금의 객체에만 해당됨)
'''

class Figure:
    count = 0  # 클래스 변수 - 클래스의 전역변수이므로 모든 객체들이 해당됨
 
    # 생성자(initializer)
    def __init__(self, width, height):
        # self.* : 인스턴스변수
        self.width = width
        self.height = height
        # 클래스 안에서 클래스 변수 접근 예 -> 클래스명.변수명
        Figure.count += 1
        #생성자에서 클래스 변수에 +1씩 더함. 즉 객체가 만들어질 때마다 count++됨

    
    def __del__(self): #소멸자. 객체 소멸
        Figure.count -= 1
    
    # 메서드
    def calc_area(self):
        return self.width * self.height #클래스 안에서 객체 변수 접근 예 *self(해당 객체를 가르킴).변수명



#클래스 밖에서 클래스 변수 호출: 그냥 클래스명.클래스 변수명
figure1 = Figure(2, 3)
Figure.count 
figure2 = Figure(2, 3)
Figure.count


print(Figure.count) #0
figure1 = Figure(2, 3) 
print(Figure.count)  #1
figure2 = Figure(4, 5)  
print(Figure.count)  #2
print(figure1.width)  #2
print(figure2.width)#4
del figure1
print(Figure.count) #1
del figure2
print(Figure.count) #0


''' 메서드도 속성과 달리 클래스 메서드, 객체 메서드,정적 메서드로 나눌 수 있음

### 2. instance method, static method, class method
### **instance method**: 해당 객체 안에서 호출 (지금까지 다룬 self.메서드명을 의미함)
 - 해당 메서드를 호출한 객체에만 영향을 미침
 - **객체 속성에 접근 가능**

### **static method**: 객체와 독립적이지만, 로직상 클래스내에 포함되는 메서드
 - self 파라미터를 갖고 있지 않음
 - **객체 속성에 접근 불가**
 - 정적 메서드는 메서드 앞에 @staticmethod 라는 Decorator를 넣어야 함
 - 클래스명.정적메서드명 또는 객체명.정적메서드명 둘 다 호출 가능
 
 !즉! 굳이 객체를 만들지 않고 바로 함수만 쓰고 싶으면 staticmethod로 선언해주면 됨!

 '''

class Figure:
    # 생성자(initializer)
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    #객체 메서드 -> 객체가 호출했을 때만 사용 가능
    def calc_area(self):
        Figure.is_square(2, 3) #객체 메서드 안에서 정적 메서드 호출 방법( 그냥 똑같이 클래스명.정적 메서드 명)
        return self.width * self.height

    # 정적 메서드 (Figure 에 너비와 높이가 같은 도형은 정사각형임을 알려주는 기능)
    #굳이 객체를 만들고 그걸 통해 호출할 필요 없이 바로 클래스 명 그 자체로도 호출 가능!(객체를 통해서도 호출도 가능함!)
    #즉 그냥 부모,자식 모든 클래스와는 별도의 함수인데 걍 결이 맞으니까 클래스 내로 들어와 있다고 생각하면 됨
    # 따라서 정적 메서드는  속성은 접근을 못함
    @staticmethod
    def is_square(rect_width, rect_height):
        #print(self.width) # 속성에 접근을 못하므로 에러남
        if rect_width == rect_height:
            print("정사각형이 될 수 있는 너비/높이입니다.")
        else:
            print("정사각형이 될 수 없는 너비/높이입니다.")


Figure.is_square(4, 5)          # 클래스명.정적메서드명으로 호출 가능 -> 생성한 객체를 통하지 않아도! 그냥 호출이 가능함

figure1 = Figure(2, 3)
figure1.is_square(5, 5)         # 객체명.정적메서드명으로 호출 가능


''' 클래스 메서드
### **class method**: 해당 class 안에서 호출 (해당 클래스로 만들어진 객체에서 호출되지 않고!, 직접 클래스 자체에서 호출)
 - self 파라미터 대신, cls 파라미터를 가짐 !!!
 - **클래스 변수 접근 가능하며 cls.클래스변수명 으로 엑세스 가능** 단, 객체 속성/메서드는 접근 불가
 - 클래스 메서드는 메서드 앞에 @classmethod 라는 Decorator를 넣어야 함
 - 클래스명.클래스메서드명 또는 객체명.클래스메서드명 둘 다 호출 가능

'''

class Figure1:
    count = 0  # 클래스 변수
 
    # 생성자(initializer)
    def __init__(self, width, height):
        # self.* : 인스턴스변수
        self.width = width
        self.height = height
        # 클래스 변수 접근 예
        Figure1.count += 1
    
    # 메서드
    def calc_area(self):
        return self.width * self.height

    # 클래스 메서드- self가 아니라 cls로 해줌
    @classmethod
    def print_count(cls):
        #self.width 이렇게 객체를 통해 해야하는 객체 속성 호출은 불가능함(즉 self 는 쓸 수 없다)
        return cls.count # 클래스 변수를 호출할 때도 클래스명.변수명이 아니라! cls.클래스 변수명으로 해줌!

figure1 = Figure1(2, 3)
figure2 = Figure1(4, 5)
print(Figure1.count)
print(Figure1.print_count()) # 2
print(figure1.print_count()) # 2


### static method 와 class method 차이!!!!!!!!!!!!
# 클래스 함수는!
#클래스의 모든 인스턴스에 적용되는 클래스 상태를 수정할 수 있습니다. !!!
# 예를 들어 해당 클래스의 모든 인스턴스에 적용할 클래스 변수를 수정할 수 있습니다.

#1.클래스 메서드
class Figure:
    @classmethod
    def set_name(cls, name):
        cls.name = name

class Circle(Figure):
   pass
 
Figure.set_name("figure")
print (Figure.name, Circle.name) #figure figure

Circle.set_name("circle")
print (Figure.name, Circle.name) #figure circle #해당 클래스 단위로 적용이 되기 때문에 circle은 바뀜


#2. static 메서드
class Figure:
    @staticmethod
    def set_name(name):
        Figure.name = name

class Circle(Figure):
   pass
 
Figure.set_name("figure")
print (Figure.name, Circle.name) #figure figure

Circle.set_name("circle")
print (Figure.name, Circle.name) #circle circle 
#static은 진짜 클래스와는 아무런 관계가 없는데 걍 결이 비슷해서 클래스 안에 있는 거임
#그래서 그냥 함수를 실행하고/바꾸면 그 함수에 해당되는 모든 게 걍 다시 시작된다고 보면 됨

