#오 파이썬 3.10 버전으로 업그레이드가 됬다. 한번 테스트 해보자.
#formatting 테스트 진행 (02-2문자열 자료형)
print('i like {0} yunah'.format(3)) #포맷팅의 기본폼이다.
number=5
print('i like {0} yunah'.format(number))
state='beauty'
print('i like {0} yunah'.format(state))
#2개 이상의 값을 넣기
print('i like {0} {1} yunah'.format(number,state))
print('i like {0} yunah {why}'.format(state,why=3)) #문자열로 대체 가능하다.
name='용일구'
print('이 보고서는 {name1}에 의하여 {date}에 만들어 졌다.'.format(name1=name,date='22.2.4'))
#자이제 f열 포매팅을 시도해보자. (3.6 버전부터 가능하다.)
name='용일구'
age=37
print(f'나의 이름은 {name}입니다.나이는{age}입니다.')
#대박 작동한다. 이거라면 하나의 지문에 여러가지 인물을 나열하여 출력가능할거 같다.
print(f'나의 이름은 {name}입니다.나이는{age+12}입니다.')

#02-3 리스트 자료형
number_1= [1,3,5,7,9]
name_1=['일구','윤애','소율']
print(name_1)
print(name_1[0]) #일구만 인덱싱 했다.
print(name_1[2]) #소율만 인덱싱 진행. 
print(number_1[0]+number_1[1]) 
print(name_1[0]+name_1[1]) 
#리스트에서 값 수정하기, 결측치를 대체하는데 사용될 것이다.
a=[1,2,3]
a[2]=4
print(a)
#요소를 제거하는 것도 테스트 해보자.del 함수를 사용해 리스트 요소 삭제하기
del a[0]
print(a)
b=[1,3,2,4,6,5,]
del b[:2]
print(b)
#리스트 정렬 함수 (순서대로 정렬한다.)
b.sort()
print(b)
#리스트에 포함된 요소 x의 개수 세기(count)
c=[1,2,2,2,3,4,5,6]
print(c.count(2))

#02-4 튜플 자료형,이게 더 편할수도?
a1=(1,2,3,4,5)
b1=('a','b','c','d','e')
print(a1+b1)
print((a1+b1)[:2])

#02-5 딕셔너리 자료형
a={'name':'pey','phone':'0119993323','birth':'1118'}
print(a.keys())
print(a['name'])
print('name' in a)
print('email' in a)

#02-6 집합 자료형, 교집합, 합집합,차집합 구하기 가능
s1=set([1,2,3,5,6])
s2=set([0,9,8,7,6,5,4])
print(s1&s2) #교집합 구하는게 가능하다.
print(s1-s2) #차집합
print(s1|s2) #합집합
s1.add(4)
s1.remove(5)
s1.update([11,12,13])
print(s1)

#20-7불 자료형 이건 if로 대체 가능할거 같은각임
bool([1,2,3])
print(bool(1))
print(bool())

#20-8 자료형의 값을 저장하는 공간, 변수
a=[1,2,3]
print(id(a)) #리스트의 주소 값을 나타낸다.고유
b=a
print(a is b) #참 거짓을 확인 한다.

#연습문제
#Q1
국어=80
영어=75
수학=55
print(국어+영어+수학/3)
