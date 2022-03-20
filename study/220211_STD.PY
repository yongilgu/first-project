#------------------------------자 3장의 시작이다.-------------------------
#if 문의 시작이다.

from ast import Add
from audioop import add


money = True
if money:
    print("가즈아!")
else:
    print("가지말자!")

#기본구조이다. if문없이 else는 독립적으로 사용이 불가하다.

money = 2000
if money >=3000:
    print("가즈아!")
else:
    print("가지말자!")

# 비교연산자 설명
# x < y   	x가 y보다 작다
# x > y	    x가 y보다 크다
# x == y	x와 y가 같다
# x != y	x와 y가 같지 않다
# x >= y	x가 y보다 크거나 같다
# x <= y	x가 y보다 작거나 같다

money = 2000
card = True
if money >=3000 or card:
    print("가즈아!")
else:
    print("가지말자!")

# 연산자	설명
# x or y	x와 y 둘중에 하나만 참이어도 참이다
# x and y	x와 y 모두 참이어야 참이다
# not x	x가 거짓이면 참이다


주머니 = ['현금','카드','대출']
if '현금' in 주머니:
    print("택시타자")
else:
    print("걸어가라")

# in	not in
# x in 리스트	x not in 리스트 []
# x in 튜플	x not in 튜플 ()
# x in 문자열	x not in 문자열

#아무런 명령어를 수행하지 않으려면

주머니 = ['현금','카드','대출']
if '없어' in 주머니:
    pass
else:
    print("걸어가라")

score =65
if score >= 60:
    message = "success"
else:
    message = "failure"

    #메세지를 띄울수 있는 기능으로 추정된다.



윤애 = ['이쁘다','사랑스럽다','슈슈하다']
if '이쁘다' in 윤애:
    print('굿')
else:
    print('ㅠㅠ')

윤애 = 90
소율 = 60

if 소율 >= 윤애:
    print("소율은 무겁다")
else:
    print("윤애가 무겁다")

#while 문의 기본구조(반복해서 문장을 수행할 경우 쓴다.)
treeHit = 0
while treeHit < 10:
    treeHit = treeHit +1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다.")


#for문(가장 직관적인 문장이다.)
# for 변수 in 리스트(또는 튜플, 문자열):
#     수행할 문장1
#     수행할 문장2

marks =[90,88,72,62,30]
number =0

for mark in marks:
    number = number +1
    if mark >=60:
        print("%d번 합격" %number)
    else:
        print("%d번 불합격" %number)


#for문과 continue
marks =[90,88,72,55,30]
number =0

for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 합격" %number)
    
    #해당이 걸릴떄까지 진행시킨다 즉, 60점 이하는 메세지를 못받는다.

    #range는 어렵네 ㅋㅋㅋ 이건 나중에

    #예제
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

#elif는 이게 ~아니면 다음거 같은 의미구나

c=" 집에 사랑 가득"
if "일구" in c: print("일구 없네")
elif "윤애" in c or "일구" in c: print("윤애랑 소율이가 있어")
elif "=윤애" not in c and "일구" not in c and "소율" in c :print("소율이 혼자 있어") 
else: print("뭐야 아무도 없어")
