slayer = ["버피", "엔", "아스틴"]
print(" ".join(slayer)) #'버피 엔 아스틴'

print("-<>-".join(slayer)) #'버피-<>-엔-<>-아스틴'

print("".join(slayer)) #'버피엔아스틴'

#reversed() 메서드 사용
print("".join(reversed(slayer))) #아스틴엔버피

#---------------------------------------
name = "스칼렛"
print(name.ljust(10, '-')) #스칼렛-------
print(name.rjust(10, '-')) #-------스칼렛

#---------------------------------------

form1 = "{0} {1}".format("안녕", "파이썬!")
print(form1)

form2 = "이름 : {who}, 나이 : {age}".format(who="제임스", age=17)
print(form2)

form3 = "이름 : {who}, 나이 : {0}".format(12, who="에이미")
print(form3)

#필드 이름 혹은 인덱스 생략 가능 자동으로 순서대로 번호 매김 
form4 = "{} {} {}".format("python", "자료구조", "알고리즘")
print(form4)

#+연산자 사용하여 문자열 더 간결하게 결합
#s:문자열 형식, r:표현 형식, a:아스키 코드 
import decimal
form5 = "{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("99.9"))
print(form5)

#---------------------------------------

hero = "버피"
number = 999
locals_form = "{number}: {hero}".format(**locals())
print(locals_form)

#---------------------------------------

slayers = "로미오\n줄리엣"
splt = slayers.splitlines()
print(splt)

#---------------------------------------

slayers = "버피+크리스-메리+16"
fields = slayers.split("+")
print(fields)
job = fields[1].split('-')
print(job)

#문자열에서 모든 스페이스 제거하는 함수
str1 = '안 녕 나 는 이 직 하 고 싶 어'

def erase_space_from_string(str):
    s1 = str.split(' ')
    res = "".join(s1)
    return res

result = erase_space_from_string(str1)
print(result)

#---------------------------------------

slayers = "로미오 & 줄리엣999"
str = slayers.strip("999")
print(str)

#---------------------------------------

slayers = "Buffy and Faith"
swap = slayers.swapcase()
print(swap)

#---------------------------------------

#문자열 안에서 또 다른 문자열의 인덱스 위치 찾는 메서드 
slayers = "Buffy and Faith"
find1 = slayers.find('y')
print(find1)

find2 = slayers.find('k')
print(find2)

#index1 = slayers.index('k')
#print(index1)

index2 = slayers.index('y')
print(index2)

#---------------------------------------

slayer = "Buffy is Buffy is Buffy"
cnt1 = slayer.count('Buffy', 0, -1)
cnt2 = slayer.count('Buffy')

print(cnt1)
print(cnt2)

#---------------------------------------

rep = slayer.replace("Buffy", "who", 2)
print(rep)

#---------------------------------------

name = "프레드"
f"그의 이름은 {name!r}입니다."
f"그의 이름은 {repr(name)}입니다." #repr() == !r

import decimal
width = 10
precision = 4
value = decimal.Decimal("12.34567")
f"결과: {value:{width}.{precision}}" #중첩 필드 사용 

from datetime import datetime
today = datetime(year=2024, month=2, day=20)
f"{today:%B %d %Y}" #날짜 포맷 지정 지정자(specifier) 사용
num = 1024
f"{num:#0x}" #정수 포맷 지정자 사용 (16진수 표현)


