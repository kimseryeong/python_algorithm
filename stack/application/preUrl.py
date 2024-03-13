##### 웹 서핑에서 이전 페이지 돌아가기 ##### 

#웹 브라우저를 통해 여러 웹 사이트를 방문하면, 방문한 url을 스택에 push
#이전 페이지 버튼 클릭 -> pop(), url을 역순으로 재방문

import webbrowser 
import time

#webbrowser.open('https://www.hanbit.co.kr') #파이썬 제공 패키지 사용하여 open


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



## 전역 변수 선언 ##
SIZE = 100 #url은 최대 100개까지 방문
stack = [None for _ in range(SIZE)]
top = -1


##메인 코드 ##
if __name__ == "__main__":
    urls = ['naver.com', 'daum.net', 'google.com'] #방문할 url을 미리 저장

    for url in urls:
        push(url)
        webbrowser.open('https://' + url)
        print(url, end='-->')
        time.sleep(1) #1초 멈추기
    print('urls 방문 종료')
    time.sleep(5) #(모든 url 방문이 끝나면) 5초 멈추기
    # print('urls 방문 후 stack >> ', stack)

    
    while True:
        url = pop()
        if url == None:
            break
        webbrowser.open('https://' + url) #방문했던 url 역순으로 추출 후 방문
        print(url, end='-->')
        time.sleep(1) #1초 멈추기
    print('방문 종료')  