import random

def testing_random():
    """ random 모듈 테스트 """
    values = [1, 2, 3, 4]
    #values 에서 랜덤으로 1개 뽑아서 출력
    print(random.choice(values))
    print(random.choice(values))
    print(random.choice(values))
    #values 에서 랜덤으로 2개 뽑아서 배열로 생성
    print(random.simple(values, 2)) 
    #values 에서 랜덤으로 3개 뽑아서 배열로 생성
    print(random.simple(values, 3))

    """ values 리스트를 섞는다 """
    random.shuffle(values)
    print(values)

    """ 0-10 임의의 정수를 생성한다 """
    print(random.randint(0, 10))
    print(random.randint(0, 10))