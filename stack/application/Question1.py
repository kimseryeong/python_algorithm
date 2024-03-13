'''

헨젤과 그레텔이 돌을 떨어뜨리면서 숲으로 들어간다. 
과자집에서 집으로 돌아갈 때는 떨어뜨린 순서와 반대로 돌을 주워야 한다.
스택을 이용해서 집으로 무사히 돌아오는 로직을 만들어보자.

'''
import random

SIZE = 6
stack = [None for _ in range(SIZE)]
top = -1

#스택 비어있는지 확인
def isStackEmpty():
    global SIZE, stack, top
    if top == -1:
        return True
    else:
        return False

#스택 가득 차있는지 확인   
def isStackFull():
    global SIZE, stack, top
    if top == SIZE-1:
        return True
    else:
        return False
    
#스택 삽입
def push(data):
    global SIZE, stack, top
    if(isStackFull()):
        print('스택이 가득')
        return False
    top += 1
    stack[top] = data

#스택 추출
def pop():
    global SIZE, stack, top
    if(isStackEmpty()):
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data




if __name__ == '__main__':
    
    # 색상이 각각 다른 돌을 준비하고 랜덤으로 섞는다
    stones = ['빨강', '초록', '핑크', '파랑', '보라']
    random.shuffle(stones)

    #우리집 -> 과자집 가는 방향으로 돌 떨어뜨리기
    print('우리집 -> 과자집')
    for stone in stones:
        push(stone)
        print(stone, '-->', end=' ')

    print()
    print()

    #과자집 -> 우리집 가는 방향의 돌 줍기
    print('과자집 -> 우리집')
    while True:
        if isStackEmpty():
            break;
        print(pop(), '-->', end=' ')
    

    