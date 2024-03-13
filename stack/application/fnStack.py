
## 함수 선언 ##
#스택 꽉 차있는지 확인 함수
def isStackFull(): 
    # from preUrl import SIZE, stack, top
    global SIZE, stack, top
    if(top >= SIZE-1):
        return True
    else:
        return False
    
#스택 비어있는지 확인 함수
def isStackEmpty(): 
    #from preUrl import SIZE, stack, top
    global SIZE, stack, top
    if(top == -1):
        return True
    else:
        return False
    
#스택 삽입 함수
def push(data): 
    # from preUrl import SIZE, stack, top
    global SIZE, stack, top
    if(isStackFull()):
        print('(push) 스택이 꽉 찼습니다.')
        return 
    top += 1
    stack[top] = data
    
#스택 추출 함수    
def pop(): 
    # from preUrl import SIZE, stack, top
    global SIZE, stack, top
    if(isStackEmpty()): #스택이 비어있는지 먼저 확인
        print('(pop) 스택이 비어있습니다.')
        return 
    data = stack[top] #스택의 마지막 요소 부터 추출
    stack[top] = None #추출 후 None 반환
    top -= 1 
    return data

#스택 확인 함수
def peak(): 
    # from preUrl import SIZE, stack, top
    global SIZE, stack, top
    if(isStackEmpty()):
        print('(peak) 스택이 비어있습니다.')
        return None
    return stack[top]