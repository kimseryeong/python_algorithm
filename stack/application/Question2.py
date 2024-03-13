'''

[파일 내용을 완전히 거꾸로 출력하기]
텍스트 파일에서 전체 줄을 거꾸로 하고, 
각 줄의 글자도 거꾸로 출력하는 프로그램을 작성한다.
파일 : Question2_txt.txt

'''

#스택 비어있는지 확인 
def isStackEmpty():
    global stack, SIZE, top
    if top == -1:
        return True
    else:
        return False
    
#스택 가득있는지 확인
def isStackFull():
    global stack, SIZE, top
    if top == SIZE-1:
        return True
    else:
        return False

#스택 삽입
def push(data):
    global stack, SIZE, top
    if (isStackFull()):
        return 
    top += 1
    stack[top] = data

#스택 추출
def pop():
    global stack, SIZE, top
    if isStackEmpty():
        return 
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

SIZE = 100
stack = [None for _ in range(SIZE)]
top = -1


### 메인 ###
if __name__ == '__main__':

    #텍스트 파일 한 줄 씩 읽어오기
    with open('stack/application/Question2_txt.txt', 'r', encoding='UTF-8') as rfp:
        txtLine = rfp.readlines()
        print(txtLine)

    print('원본 >>>>>>>>>>>>>>>>>>>>>>> ')
    for line in txtLine:
        push(line)
        print(line, end=' ')

    print()
    print('거꾸로 >>>>>>>>>>>>>>>>>>>>>>> ')
    while True:
        line = pop()
        if line == None:
            break
        # print(line, end=' ')

        lineStack = [None for _ in range(len(line))]
        lineTop = -1

        for ch in line:
            lineTop += 1
            lineStack[lineTop] = ch

        while True:
            if lineTop == -1:
                break
            ch = lineStack[lineTop]
            lineTop -= 1
            print(ch, end=' ')
            

    