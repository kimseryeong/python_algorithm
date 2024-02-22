t1 = 1234, '안녕!'
print(t1[0])
print(t1)

t2 = t1, (1, 2, 3, 4, 5)
print(t2)

empty_t = ()
print(len(empty_t))

tup1 = '안녕', #또는 ('안녕',)
print(len(tup1))
print(tup1)

tup2 = ('안녕')
print(tup2)

t = 1, 5, 7, 8, 9, 4, 1, 4
tup_cnt = t.count(4)
print(tup_cnt)

t = 1, 5, 7, 8, 9, 4, 1, 4
tup_idx = t.index(4)
print(tup_idx)

#튜플 언패킹
x, *y = (1, 2, 3, 4,5)
print(x)
print(y)
*x, y = (1, 2, 3)
print(x)
print(y)

x, y, *z = (1, 2, 3, 4, 5, 6)
print(x)
print(y)
print(z)

#네임드 튜플
import collections
Person = collections.namedtuple('Person', 'name age gender')
# Person = collections.namedtuple('Person', ['name', 'age', 'gender'])
# Person = collections.namedtuple('Person', ('name', 'age', 'gender'))
p = Person('아스틴', 30, '여자')
print(p)

torf = p.age == 20
print(torf)

p.age = 20