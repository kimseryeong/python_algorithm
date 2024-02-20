import math

#1. 재귀함수를 호출하는 방법
#   -> 시간복잡도 : O(2^n)
def find_fibonacci_seq_iter(n):
    if n < 2: return n
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

#2. 반복문을 사용하는 방법
#   -> 시간복잡도 : O(n)
def find_fibonacci_seq_rec(n):
    if n < 2: return n
    return find_fibonacci_seq_rec(n-1) + find_fibonacci_seq_rec(n-2)

#3. 수식을 사용하는 방법
#   -> 시간복잡도 : O(1) 
#      (단, 70번째 이상의 결과는 정확하지 않음)
def find_fibonacci_seq_form(n):
    sq5 = math.sqrt(5) #math.sqrt(x) : x의 제곱근 반환
    phi = (1 + sq5) / 2
    return int(math.floor(phi ** n / sq5)) #math.floor(x) : 실수 x를 내림하여 정수 반환
