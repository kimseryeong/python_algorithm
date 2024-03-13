#append
people = ['버피', '테스트']
people.append('미미')
print(people)

people[len(people):] = ['젠더']
print(people)

#---------------------------------------------------
#extend
people = ['버피', '테스트']
people.extend('파파')
print(people)

people[len(people):] = '아스틴'
print(people)

people += '월로'
print(people)

people += ['젠더']
print(people)

#---------------------------------------------------
#insert()
people = ['버피', '테스트']
people.insert(1, '젠더')
print(people)

#---------------------------------------------------
#remove()
people = ['버피', '테스트']
people.remove('버피')
print(people)

#people.remove('젠더')

#---------------------------------------------------
#pop()
print('0-----')
people = ['버피', '테스트', '아스틴']
people.pop(1)
print(people)

people.pop()
print(people)

#---------------------------------------------------
#del문
a = [-1, 4,5, 7, 10]
del a[0]
print(a)

del a[2:3]
print(a)

del a #변수 a자체를 삭제
#print(a) #NameError: name 'a' is not defined

#---------------------------------------------------
#index()
people = ['버피', '테스트', '아스틴']
idx = people.index('버피')
print(idx)

#---------------------------------------------------
#count()
people = ['버피', '테스트', '아스틴']
cnt = people.count('버피')
print(cnt)

#---------------------------------------------------
#sort()
people = ['버피', '테스트', '아스틴']
people.sort()
print(people)

people.sort(reverse=True)
print(people)

#sort() 응용 예제 : 날짜 정렬 
import time
timestamp = [
    "2018-12-12 01:17:31"
    ,"2018-12-12 02:17:31"
    ,"2018-12-12 06:17:31"
    ,"2018-11-25 07:17:31"
    ,"2018-11-25 11:17:31"
    ,"2018-11-25 12:17:31"
]
def time_format(t):
    return time.strptime(t, '%Y-%m-%d %H:%M:%S')[0:6]

latest = timestamp.sort(key=time_format, reverse=True)
print(latest)

#---------------------------------------------------
#reverse()
people = ['버피', '테스트', '아스틴']
people.reverse()
print(people)
print(people[::-1])
