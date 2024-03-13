#stack의 일반 구현
#-----------------------------------------------------------------

##### 스택 초기화 ###### 

stack = [None, None, None, None, None]# -> 사이즈가 큰 스택의 경우 타이핑 반복하기 어려움

#사이즈를 미리 설정하고 빈 스택 생성
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1 #스택이 비어있다는 의미



##### 스택이 꽉 찼는지 확인하는 함수 ###### 
def isStackFull():
    global SIZE, stack, top
    if(top >= SIZE-1):
        return True
    else:
        return False
    
SIZE = 5
stack = ["커피", "녹차", "꿀물", "콜라", "환타"]
top = 4
print("스택이 꽉찼는지 확인 >> ", isStackFull())



##### 스택에 데이터 삽입하는 함수 ###### 
def push(data):
    global SIZE, stack, top
    if(isStackFull()):
        print('스택이 꽉 찼습니다.')
        return 
    top += 1
    stack[top] = data

SIZE = 5
stack = ["커피", '녹차', '환타', '콜라', None]
top = 3

print(stack)
push('꿀물')
print(stack)
push('게토레이')



##### 스택이 비어있는지 확인하는 함수 ###### 
def isStackEmpty():
    global SIZE, stack, top
    if(top == -1):
        return True
    else:
        return False

SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1
print("스택이 비어있는지 확인 >> ", isStackEmpty())



##### 스택에서 데이터 추출하는 함수 ###### 
def pop():
    global SIZE, stack, top
    if(isStackEmpty()): #스택이 비어있는지 먼저 확인
        print('스택이 비어있습니다.')
        return 
    data = stack[top] #스택의 마지막 요소 부터 추출
    stack[top] = None #추출 후 None 반환
    top -= 1 
    return data

SIZE = 5
stack = ["커피", None, None, None, None]
top = 0

print(stack)
retData = pop() #스택 추출하면서 추출값 변수에 삽입
print('추출한 데이터 : ', retData)
print(stack)
retData = pop()



##### 스택 데이터 확인 함수 ###### 
# pop() : 데이터를 스택에서 추출해서 삭제하고 top 위치는 한 칸 내려감
#         데이터를 뽑아내는 효과
# peak() : top 위치의 데이터를 확인만 하고 스택에 그대로 두기
def peak():
    global SIZE, stack, top
    if(isStackEmpty()):
        print('스택이 비어있습니다.')
        return None
    return stack[top]

SIZE = 5
stack = ["커피", "녹차", None, None, None]
top = 1

print(stack)
retData = peak()
print('top의 데이터 확인 : ', retData)
print(stack)
pop()
pop()
retData = peak()
print('top의 데이터 확인 : ', retData)


###### 스택 크기 입력받고 삽입, 추출, 확인을 선택하여 작동하는 코드 ###### 
SIZE = int(input('스택 크기를 입력하세요 >> '))
stack = [None for _ in range(SIZE)]
top = -1

## 메인 코드 실행 ##
if __name__ == "__main__":
    select = input('삽입(I) / 추출(E) / 확인(v) / 종료(X) 중 하나 선택 >> ')

    while (select != 'X' and select != 'x'):
        if select == 'I' or select == 'i':
            data = input("입력할 데이터 -> ")
            push(data)
            print('스택 상태 : ', stack)
        elif select == 'E' or select == 'e':
            data = pop()
            print("추출된 데이터 -> ", data)
            print('스택 상태 : ', stack)
        elif select == 'v' or select == 'V':
            data = peak()
            print("확인된 데이터 -> ", data)
            print('스택 상태 : ', stack)
        else:
            print('입력이 잘못됨')

        select = input('삽입(I) / 추출(E) / 확인(v) / 종료(X) 중 하나 선택 >> ')
    
    print('프로그램 종료')
        
