import math
import random

#브루트 포스 (무차별 대입 방법)
def finding_prime(num):
    num = abs(num)
    if num < 4: return True
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

#제곱근 이용
def finding_prime_sqrt(num):
    num = abs(num)
    if num < 4: return True
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

#확률론적 테스트와 페르마의 소정리 사용
def finding_prime_fermat(num):
    if num <= 102:
        for a in range(2, num):
            if pow(a, num-1, num) != 1:
                return False
        return True
    else:
        for i in range(100):
            a = random.randint(2, num-1)
            if pow(a, num-2, num) != 1:
                return False
        return True
    


#------------------------------------------------
#random 모듈을 사용하여 n비트 소수를 생성.
    
import math
import random
import sys

def finding_prime_sqrt(num):
    num = abs(num)
    if num < 4: return True
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

def generate_prime(num=3):
    while 1:
        p = random.randint(pow(2, num-2), pow(2, num-1)-1)
        p = 2 * p + 1
        if finding_prime_sqrt(p):
            return p
        