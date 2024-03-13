##### 괄호의 매칭 검사 ##### 

# (), {} [] <>

# 여는 괄호는 무조건 push, 닫는 괄호 만나면 pop 하여 비교
'''
    1. 닫는 괄호를 만났을 때, 스택은 비어있지 않아야 함
    2. 닫는 괄호를 만났을 때, 추출한 괄호는 여는 괄호여야 함
    3. 2를 만족해도 두 괄호의 종류가 같아야 함
    4. 모든 수식의 처리가 끝나면 스택은 비어 있어야 함

if '(', '[', '<', '{' 중 하나라면 :
    push()
elif ')', ']', '>', '}' 중 하나라면 :
    열린괄호 = pop()
    if 두 괄호의 쌍이 맞으면:
        True
    else
        False

if 스택이 비어있다면:
    True
else:
    False

'''

### 함수 선언 ###
def isStackFull():
    global SIZE, stack, top
    if(top >= SIZE-1):
        return True
    else:
        return False
    
def push(data):
    global SIZE, stack, top
    if(isStackFull()):
        print('스택이 꽉 찼습니다.')
        return 
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if(top == -1):
        return True
    else:
        return False
    
def pop():
    global SIZE, stack, top
    if(isStackEmpty()): #스택이 비어있는지 먼저 확인
        return 
    data = stack[top] #스택의 마지막 요소 부터 추출
    stack[top] = None #추출 후 None 반환
    top -= 1 
    return data

def peak():
    global SIZE, stack, top
    if(isStackEmpty()):
        return None
    return stack[top]

#확인용
def checkGwlho(expr):
    for ch in expr:
        if ch in '({[<':
            push(ch)
        elif ch in ')}]>':
            out = pop()
            if ch == ')' and out == '(':
                pass
            elif ch == '}' and out == '{':
                pass
            elif ch == ']' and out == '[': 
                pass
            elif ch == '>' and out == '<':
                pass
            else:
                return False
        else:
            pass

    if isStackEmpty():
        return True
    else:
        return False



### 전역변수 선언 ###
SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1

### 메인 코드 ###
if __name__ == "__main__":
    expreArray = ['(A+B)', ')A+B(', '((A+B)-C', '(A+B]', '(<A+{B-C}/[C*D]>)']

    for expr in expreArray:
        top = -1
        print(expr, '-->', checkGwlho(expr))