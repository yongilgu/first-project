#-------------------------#4장 함수 1--------------------------------------
#간단하게 입력된 정보를 믹스(함수)하여 출력하는 것

#def 함수명(매개변수):
    #<수행할 문장1>
    #<수행할 문장2>

from platform import win32_edition
from unittest import result


def add(a,b): #def는 함수를 지칭하고, add는 함수이름이고 입력으로 2개값을 받는다. a,b= 매개변수(parameter)
    return a+b #출력값은 a,b를 더한 것이다. 
print(add(3,4)) #함수에 인수를 넣어서 출력하라. 3,4=인수(arguments)

#함수의 4가지 유형(입력,결과값 유무에 따라서 발생)
#1. 일반적인 함수

def add(a,b):
    result =a+b
    return result

a=add(5,5)
print(a)

#2. 입력값이 없는 함수

def say(): #입력값이 없는 함수의 경우 ()에 아무것도 넣어서는 안된다.
    return "hi"

a=say() #함수는 지정되어있다. 
print(a)

#3. 결과 값이 없는함수

# def add(a,b):
#     print("%d,%d의 합은 %d입니다." %(a,b,a+b)))

# add(3,4)
#오직 리텅이 발생해야 만 결과값이 산출된다.

#4. 입력, 결과값이 없는 함수

def say():
    print("hi")

#매개변수 지정하여 호출하기

def add(a,b):
    return a+b

result =add(a=3,b=7)
print(result)

#일반적으로는 아래와같다.

def add(a,b):
    return a-b

print(add(3,1))

#하지만 결과에 저렇게 적용이 가능해서 각각의 변수를 지정가능하다.

#입력값이 몇개가 되지 모를떄는 어떻게 해야하는가?

# def 함수이름(*매개변수): 
#     <수행할 문장>
#     ...

def add_many(*ilgu): #*args= 임읠 정한 변수이름, *python 처럼 아무거나 써된다. args는 인수를 뜻하는 영어 단어 arguments의 약자이며 관례적으로 자주 사용한다.
    result = 0
    for i in ilgu:
        result = result + i
    return result

result = add_many(1,2,3)
print(result)


def add_mul(choice,*args):
    if choice == "add": # ==이거 두개의 의미가 뭐였더라? # x == y	x와 y가 같다
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul": #곱하기를 뜻한다.
        result = 1
        for i in args:
            result = result * i
    return result #리턴값을 지정해 주어야 한다! 꼮꼭

result = add_mul("mul", 1,2,3,4,5)
print(result)

#수식을 쌓으니까 재밋네.. 그럼 더 복잡한 수식도 가능하다는 이야기인데...
#하지만 지금은 함수가 뭔지 모르겠다. add, mul 등의 함수를 익혀야 한다는 뜻인데



#  ---------------------------4장 함수2----------------------

#키워드 파라미터 kwargs, 딕셔어리로 만들어져서 출력괸다.
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(name='soyul', age=0)

#딕셔너리의 이름은 바꿀수 있다.
def print_kwargs(**ilgu):
    print(ilgu)

print_kwargs(name='soyul',age=1)


#함수의 결과 값은 언제나 하나이다.

def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result)

def add_and_mul(a,b):
    return a+b, a*b
result1, result2 = add_and_mul(3,4)
print(result1)
print(result2)

def add_and_mul(a,b):
    return a+b #이경우에는 a+b만 가져간다.
    return a*b
result = add_and_mul(3,4)
print(result)

#return 의 또다른 쓰임새


def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." %nick)

say_nick("야호")
say_nick("바보") #이걸 입력받으면 바로 함수를 빠져나온다는 if 설정이다.
#어떤 특정 상황에서 함수를 적용하지 않는 것으로 사용가능할거 같다.


def say_my(name,old,man=True):
    print("나의 이름은 %s입니다." %name)
    print("나의 나이는 %d입니다" %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
    
say_my("용일구",37,True)
say_my("용일구",37,False)


#lambda는 함수를 줄일때 사용된다.

add= lambda a,b: a+b
result=add(3,4)
print(result)

def add(c,d):
    return(c+d)
result=add(3,5)
print(result)


#---------------------------4-2 사용자 입력과 출력---------------------
#사용자가 입력한 값을 어떤 변수에 대입하고 싶을떄는 어떻게 해야할까?

a = input('숫자를 입력하세요')

#이건 자세히 모르겠다 알아보자.

#print 자세히 알기

for i in range(10):
    print(i,end='')


