#다른 진법을 10진수로 변환하는 함수
def convert_to_10jinbeob(num, base):
    multiplier, result = 1, 0
    while num > 0:
        result += num % 10 * multiplier
        multiplier *= base 
        num = num // 10
    return result

#다른 진법을 10진수로 바꾸는 함수 테스트
def test_convert_from_jinbeob():
    num, base = 9, 2
    assert(convert_to_10jinbeob(num, base) == 1001)
    print('10진법 -> 다른 진법 테스트 통과')

if __name__ == "__main__":
    test_convert_from_jinbeob()
#------------------------------------------------------

#10진수를 다른 진법의 숫자로 변환하는 함수
def convert_to_jinbeob(num, base):
    multi, res = 1, 0
    while num > 0:
        res += num % base * multi
        multi *= 10
        num = num // base
    return res

#10진수를 다른 진법의 숫자로 변환하는 함수 테스트
def test_convert_from_10jinbeob():
    num, base = 9, 2
    assert(convert_to_jinbeob(num, base) == 1001)
    print('다른 진법 -> 10진법 테스트 통과')
#------------------------------------------------------
    
#base가 10보다 큰 경우, 
#10 이상의 숫자를 나타내기 위해 문자를 사용
#A=10, B=11, C=12 ...

#10진법 숫자를 20이하의 진법으로 변환
def convert_from_decimal_larger_bases(num, base):
    strings = '0123456789ABCDEFGHIJ' #0-19까지 (20개)
    res = ""
    while num > 0:
        digit = num % base
        res = strings[digit] + res
        num = num // base
    return res
#------------------------------------------------------

#재귀함수를 사용한 진법 변환
#재귀 알고리즘 (8.2 참고)
def convert_dec_to_any_base_rec(num, base):
    convertString = "0123456789ABCDEF"
    if num < base:
        return convertString[num]
    else:
        return convert_dec_to_any_base_rec(num // base, base) + convertString[num % base]
