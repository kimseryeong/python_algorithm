'''

선형 리스트 응용 중 가장 많이 이용되는 것 
: 다항식을 저장하고 활용하는 것

p(x) = 7x^3 - 4x^2 + 5
p(x) = 7x^3 - 4x^2 + 0x^1 + 5x^0

각 배열은 최고차항부터 나열한다고 가정하면
px = [7, -4, 0, 5]
차수  3   2  1  0

'''

##### 다항식 선형 리스트 표현과 계산 프로그램 ##### 

#다항식 표현
def printPoly(p_x):
    term = len(p_x) - 1 #최고차항 숫자 (배열 길이 - 1)
    polyStr = "P(x) = "

    for i in range(len(px)):
        coef = p_x[i] #계수

        if coef >= 0:
            polyStr += "+"
        polyStr += str(coef) + 'x^' + str(term) + " "
        term -= 1
    return polyStr

#다항식 계산
def calcPoly(xVal, p_x):
    retVal = 0
    term = len(p_x) - 1 #최고차항 숫자 (배열 길이 - 1)

    for i in range(term):
        coef = p_x[i] #계수
        retVal += coef * xVal ** term
        term -= 1
    return retVal

## 전역변수 선언
px = [7, -4, 0, 5]


### 메인 코드
if __name__ == '__main__':
    pStr = printPoly(px)
    print('다항식 >> ', pStr)

    xVal = int(input('x 값 >> '))

    pxVal = calcPoly(xVal, px)
    print('다항식 결과 >> ', pxVal)

