#데코레이터는 다양한 언어 전반에서 쓰임
import math

#2.1 중첩함수(nested function) - 함수 안에서 새로운 함수를 선언
'''def outer_func():
    print('call outer_func function')

    def inner_function(): #함수 안에서 또 함수를 "정의"-호출이 아님!
        return 'call inner_func function'

    print(inner_function())'''


'''
outer_func() - 얘를 호출하면
#call outer_func function
#call inner_func function'''

###중첩 함수의 내부 함수는 함수 밖에서는 호출 불가
##단독으로 inner_function() 이렇게는 호출 못 함
#outer_func 함수 안에서만 호출 가능

#그런데 중첩함수를 함수 밖에서도 호출 할 수 있는 방법이 있다
#first-class function,closure

def outer_func(num):

    def inner_func(): #함수 안에서 또 함수를 "정의"-호출이 아님!
        print(num)
        return 'complex'

    return inner_func #중첩함수를 리턴하는 first-class함수

fn=outer_func(10) #outer function #first-class function
#fn이라는 변수에는 outer_func의 리턴값! 즉 inner_func가 들어가 있는 거임!(num=10이 되어있는채로)

print(fn())  #closure 호출 
#이 방법을 통해 중첩함수만 실행(중첩함수만 호출된 거임)
#이렇게 outer변수에다 ()붙이면 중첩함수를 실행시킨 것처럼 할 수 있음
'''
10
complex
'''

#2.2 First-class function
'''#First-class 함수란 -->그냥 일반적인 함수인 듯?
  - 함수 자체를 변수에 저장 가능
     예) 
     def calc_square(digit):
         return digit*digit;
    
    func1=calc_squre
    print(func1(2)) #즉 함수를 다른 변수에 담고 그 변수가 함수명인 것처럼
  
  - 함수의 인자에  다른 함수를 인수로 전달 가능
  - 함수의 반환 값(return 값)으로 함수를 전달 가능'''

#first class함수 활용
def html_creator(tag):
    def text_wrapper(msg):
        print ('<{0}>{1}</{0}>'.format(tag, msg))
    return text_wrapper  #중첩함수를 리턴하는 first class함수

h1_html_creator=html_creator('h1') #이러면 text_wrapper함수(중첩함수)가 담겨지고, tag=h1값이 저장된 상태인 거임
h1_html_creator('h1태그는 타이틀을 표시하는 태그입니다')#따라서 이렇게 되면 중첩함수가 호출되는 거임
#<h1>h1태그는 타이틀을 표시하는 태그입니다</h1>

#연습
#스트링으로 된 문자열 리스트가 주어지면, 정해진 목차 기호로 나열해주는 First-class 함수를 만들어보세요<br>
def list_creator(mark):
    def text_creator(list):
        for item in list:
            print(mark,item)

    return text_creator

list_mark=list_creator('-')
list_mark(['안녕','하세요','화이팅!'])
'''
- 안녕
- 하세요
- 화이팅!

'''


### 2.3. Closure function
#* 함수와 해당 함수가 가지고 있는 **데이터를 함께 복사, 저장해서 별도 함수**로 활용하는 기법으로 First-class 함수와 동일
#* 외부 함수가 소멸되더라도, 외부 함수 안에 있는 로컬 변수 값과 중첩함수(내부함수)를 사용할 수 있는 기법
list_mark=list_creator('-') #--->first-class function
list_mark(['안녕','하세요','화이팅!']) #----> closure 호출 #그냥 이 과정 자체가 closure fucntion이 되는 거임

#연습
#1에서 5까지 1승부터 5승까지 출력하기 
#(위 calc_power() 함수를 사용해서 list_data 리스트 변수에 1승부터 5승까지 계산 클로져 함수를 넣어서 사용)
#문제가 뭔 말인지 모르겠음;; 걍 이해한대로 품
def calc_power(num):
    def list_calc():
        res=list()
        for i in range(1,6):
            res.append(pow(num,i))
        print (res)

    return list_calc #중첩함수 호출

calc=calc_power(2)
calc() #[2, 4, 8, 16, 32]


#2.4 데코레이터
#함수 앞 뒤에서 기능을 추가해서 함수를 활용
#closure function을 활용


'''@decorator_func
def function():
    print ("what is decorator?")
#### 위 코드에서 @decorator_func 부분이 데코레이터임 '''

### 즉 decorator는 outer_function에 해당되고, 그 아래의 함수는 inner_function에 해당되는 거임
### 따라서 decorator를 읽으면(위에서 배운 과정처럼) 내부 함수인 데코레이터 아래에 있는 함수가 실행되는 거임
###(즉 decorator 는 위에서 배운 중첩함수대로 하기 위해 표현을 간략하게 해놓은 것)


###예시 - 파라미터가 있는 함수에 Decorator 적용하기
#예제 코드는 파이썬 코딩 도장 참고

#데코레이터 적용 전의 코드(그냥 중첩 함수로 표현)
def trace(func):                             # 호출할 함수를 매개변수로 받음!!!!
    def wrapper():                           # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
 
def hello():
    print('hello')
 
def world():
    print('world')
 
trace_hello = trace(hello)    # 데코레이터에 호출할 함수를 넣음
trace_hello()                 # 반환된 함수를 호출
'''hello 함수 시작
hello
hello 함수 끝'''
trace_world = trace(world)    # 데코레이터에 호출할 함수를 넣음
trace_world()                 # 반환된 함수를 호출
'''world 함수 시작
world
world 함수 끝'''


##데코레이터 적용 후(위의 코드에서)!!!
def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
 
@trace    # @데코레이터
def hello():
    print('hello')
 
@trace    # @데코레이터
def world():
    print('world')
 
hello()    # 함수를 그대로 호출
world()    # 함수를 그대로 호출
##즉 데코레이터를 쓰면, 중첩함수의 활용에서 내부 함수를 호출할 때,
# 변수에 함수 전달을 하는 과정 없이! 그냥 바로 호출 할 수 있게 됨

'''#연습
type_checker 데코레이터 만들기 (인자 유효성 검사)
digit1, digit2 를 곱한 값을 출력하는 함수 만들기
type_checker 데코레이터로 digit1, digit2 가 정수가 아니면 'only integer support' 출력하고 끝냄
if (type(digit1) != int) or (type(digit2) != int):'''


def type_checker(function):
    def wrapper(digit1,digit2):
        if (type(digit1) != int) or (type(digit2) != int):
            print("only integer support")
            return
        function(digit1,digit2)  #데코레이터로 정의된 함수를 실행해라
    return wrapper

@type_checker
def multiplexer(num1,num2):
    print(num1*num2)

@type_checker
def adder(num1,num2):
    print(num1+num2)

#데코레이터 처리를 해줬으니까 변수에 함수 외부 함수 전달할 필요 없이 바로 내부 함수로 쓰일 거 호출해주면 됨
multiplexer(2,3) #6
adder(2,3) #5

### 파라미터와 관계없이 모든 함수에 적용 가능한 Decorator 만들기
#* 파라미터는 어떤 형태이든 결국 (*args, ***kwargs) 로 표현 가능!!!!!!!!!!!!
#* 데코레이터의 !!!내부!!!함수 파라미터를 (*args, ***kwargs) 로 작성하면 어떤 함수이든 데코레이터 적용 가능
'''
# 데코레이터 작성하기 - 이런 식으로, 이렇게 해주면 아래의 데코레이터를 활용해서 하는 건 동일함
def general_decorator(function):
    def wrapper(*args, **kwargs):
        print('function is decorated')
        return function(*args, **kwargs)
    return wrapper
'''


### 한 함수에 데코레이터 여러 개 지정하기
#* 함수에 여러 개의 데코레이터 지정 가능 (여러 줄로 @데코레이터를 써주면 됨)
#* 데코레이터를 나열한 순서대로 실행됨 - !!모두 실행됨!- 추가 기능할 때 쓰면 좋음
# 여러 데코레이터 작성하기(각 데코레이터 당 기능 한 개- 함수 한 개)
def decorator1(function):
    def wrapper():
        print('decorator1')
        function()
    return wrapper

 
def decorator2(function):
    def wrapper():
        print('decorator2')
        function()
    return wrapper

# 여러 데코레이터를 함수에 한번에 적용하기
@decorator1
@decorator2
def hello():
    print('hello')
'''
decorator1
decorator2
hello
'''

'''<도전 과제>
다음 그림에 있는 HTML 웹페이지 태그를 붙여주는 데코레이터 만들기
해당 데코레이터를 사용해서 안녕하세요 출력해보기
'''
def mark_bold(function):
    def wrapper(content):
        result="<b>"+function(content)+"</b>" 
        return result 
    return wrapper

def mark_italic(function):
    def wrapper(content):
        result="<i>"+function(content)+"</i>"
        return result
    return wrapper


@mark_bold
@mark_italic
def make_html(string):
    return string

print(make_html("안녕하세요!")) #<b><i>안녕하세요!</i></b>


### Method Decorator
#* 클래스의 method에도 데코레이터 적용 가능
#- 클래스 method는 첫 파라미터가 self 이므로! 이 부분을 데코레이터 작성시에 포함시켜야 함
# 데코레이터 작성하기 (for method) -작성 단계부터 self를 넣어줘야! class의 메서드에도 적용이 가능함!
def h1_tag(function):
    def func_wrapper(self, *args, **kwargs):            # <--- self 를 무조건 첫 파라미터로 넣어야 메서드에 적용가능
        return "<h1>{0}</h1>".format(function(self, *args, **kwargs))  # <--- function 함수에도 self 를 넣어야 함
    return func_wrapper

# 클래스 선언시 메서드에 데코레이터 적용하기
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @h1_tag
    def get_name(self):
        return self.first_name + ' ' + self.last_name

# 데코레이터 적용 확인해보기
davelee = Person('Lee', 'Dave')
print(davelee.get_name())

#+)
#### 파라미터가 있는 Decorator 만들기 (심화)
# *decorator에 파라미터를 추가 가능
# 중첩 함수의 하나 더 깊게 두어 생성

#데코레이터 표현 전
def decorator1(num):
    def outer_wrapper(function):
        def innter_wrapper(*args, **kwargs):
            print('decorator1 {}'.format(num))
            return function(*args, **kwargs)
        return innter_wrapper
    return outer_wrapper

def print_hello():
    print ('hello')

print_hello2 = decorator1(1)(print_hello)
print_hello2()


@decorator1(1) # 여기서 인자를 미리 줌
def print_hello():
    print('hello')



### 도전과제 - 이중중첩, 데코레이터(인자 전달)을 활용하기
def mark_html(tag):
    def outer_wrapper(function):
        def inner_wrapper(*args, **kwargs):
            return '<' + tag + '>' + function(*args, **kwargs) + '</' + tag + '>'
        return inner_wrapper
    return outer_wrapper
     

@mark_html('b')
def print_bold(title):
    return title

@mark_html('h1')
def print_title(title):
    return title

print(print_title('안녕안녕!'))

