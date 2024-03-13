#stack의 일반 구현
#-----------------------------------------------------------------

##### 스택 초기화

stack = [None, None, None, None, None]# -> 사이즈가 큰 스택의 경우 타이핑 반복하기 어려움

#사이즈를 미리 설정하고 빈 스택 생성
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1 #스택이 비어있다는 의미



##### 스택이 꽉 찼는지 확인하는 함수
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



##### 스택에 데이터 삽입하는 함수
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



##### 스택이 비어있는지 확인하는 함수
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



##### 스택에서 데이터 추출하는 함수
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



##### 스택 데이터 확인 함수
# pop() : 데이터를 스택에서 추출해서 삭제하고 top 위치는 한 칸 내려감
#         데이터를 뽑아내는 효과
# peak() : top 위치의 데이터를 확인만 하고 스택에 그대로 두기
def peak():
    global SIZE, stack, top
    if(isStackEmpty()):
        print('스택이 비어있습니다.')
        return None
    data = stack[top]
    return data
    