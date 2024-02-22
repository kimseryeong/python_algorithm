#[항목 for 항목 in 반복 가능한 객체]
#[표현식 for 항목 in 반복 가능한 객체]
#[표현식 for 항목 in 반복 가능한 객체 if 조건문]

a = [y for y in range(1900, 1940) if y%4 == 0]
print(a)

b = [2**i for i in range(13)]
print(b)

c = [x for x in a if x%2 == 0]
print(c)

d = [str(round(355/113.0, i)) for i in range(1, 6)]
print(d)

words = 'Buffy is awesome and a vampire slayer'.split()
e = [[w.upper(), w.lower(), len(w)] for w in words]
print(e)
for i in e:
    print(i)
