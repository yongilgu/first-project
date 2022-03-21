#프로그램을 만들려면 입력과 출력을 생각하라.

#구구단 프로그램중 2단을 만든다면? 2를 입력값을로 주었을떄 어떻게 출력될 것인가?

# 함수이름은 GuGu
# 입력받는 값은? 2
# 출력하는 값은? 2단 (2,4,6,8,~)
# 결과는 어떤 형태로 저장하지? 연속된 자료형이니까 리스트!



def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n*i)
        i = i + 1
    # result.append(n*1)
    # result.append(n*2)
    # result.append(n*3)
    # result.append(n*4)
    # result.append(n*5)
    # result.append(n*6)
    # result.append(n*7)
    # result.append(n*8)
    # result.append(n*9)
    return result
print(GuGu(2))


#과연 append 함수는 어떻게 익숙해 져야 하는것인가?함수를 천천히 다 보자.
#프로그램밍을 할땐 매우 구체적으로 접근해야 머리가 덜 아프다는 것을 기억하자.