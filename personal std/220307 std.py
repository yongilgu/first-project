#---------------------------4-3 파일 읽고 쓰기---------------------

f = open("C:/Users/ksol180204/Desktop/Python_19/새파일2.txt",'w') #open 함수이다. r = 읽기, w= 쓰기, a= 추가
for i in range(1,11):
    data = "%d번쨰 줄입니다.\n" %i #줄바꿈을 뜻하는 \n을 잘 봐야한다. 이건 역슬레시가 필요하다.
    f.write(data)
f.close #파일객체를 닫아주는 역활을 한다.

#이제 프로그램 외부 파일을 읽어 들여 프로그램에서 사용할수 있는 여러가지 방법을 알아보자.

#readline 함수 이용

f = open("C:/Users/ksol180204/Desktop/Python_19/새파일2.txt",'r')
line = f.readline() #첫번쨰 줄을 읽어들이라는 명령어이다.
print(line)
f.close

#만약 모든줄을 읽어서 화면에 출력하고 싶다면?

f = open("C:/Users/ksol180204/Desktop/Python_19/새파일2.txt",'r')
while True: #무한 루프 안에서
    line = f.readline() #한줄씩 라인을 읽는다.
    if not line: break #만약 더 읽을 라인이 없다면 break 를 수행한다.
    print(line)
f.close

# readline 함수 사용하기

f = open("C:/Users/ksol180204/Desktop/Python_19/새파일3.txt",'w')
for i in range (1,11):
    data = "%d번쨰 줄. \n" %i
    f.write(data)
f.close

f = open("C:/Users/ksol180204/Desktop/Python_19/새파일3.txt",'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close

#줄바꿈 \n 제거 하기

f = open("C:/Users/ksol180204/Desktop/Python_19/새파일3.txt",'r')
lines = f.readlines()
for line in lines:
    line = line.strip() #줄바꿈을 제거하는 식이다.
    print(line)
f.close

#read  함수 사용하기
f = open("C:/Users/ksol180204/Desktop/Python_19/새파일4.txt",'w')
for i in range(1,10):
    data ="%d번이다.\n" %i
    print(data)
    f.write(data)
f.close


#이제 파일에 새로운 내용을 추가해보자. 추가모드 a이다.

f = open("C:/Users/ksol180204/Desktop/Python_19/새파일4.txt",'a')
for i in range(11,20):
    data ="%d번.\n" %i
    print(data) #이렇게는 파일에 써질수 없다. 데이터만 불러온것이다.
    f.write(data)
f.close


f = open("C:/Users/ksol180204/Desktop/Python_19/새파일4.txt",'r')
data = f.read()
print(data)
f.close()
#전체를 읽으라는 간단한 수식이다.


#with 문과 함께 써보기