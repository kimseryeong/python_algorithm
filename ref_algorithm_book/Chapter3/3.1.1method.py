#add()
people = {'버피', '토끼', '사자'}
people.add('호랑이')
print(people)

print('-------------------------')
#------------------------------------------------
#update(), |=
fruits = {'딸기', '포도', '망고'}
fruits.update({'자몽', '토마토', '딸기'})
print(fruits)

fruits |= {'수박', '사과'}
print(fruits)

print('-------------------------')
#------------------------------------------------
#union(), |
food = {"샌드위치", "샐러드"}
food_union = food.union({"파스타", "초밥"})
print(food)
print(food_union)

food_union2 = food | {'연어회'}
print(food)
print(food_union2)

print('-------------------------')
#------------------------------------------------
#intersection(), &
milk = {'초코', '딸기', '바나나'}
fav_milk = {'초코'}
intsc = milk.intersection(fav_milk)
print(intsc)

and_ = milk & fav_milk
print(and_)

print('-------------------------')
#------------------------------------------------
#difference(), -
fish = {'고등어', '갈치', '광어', '연어'}
fav_fish = {'연어', '고등어'}
diff = fish.difference(fav_fish)
print(diff)
minus = fish - fav_fish
print(minus)

print('-------------------------')
#------------------------------------------------
#clear()
stuff = {'칫솔', '치약'}
stuff.clear()
print(stuff)

print('-------------------------')
#------------------------------------------------
#discard(), remove(), pop()
contries = {'프랑스', '이탈리아', '싱가포르'}
contries.discard('한국')
print(contries)
contries.discard('이탈리아')
print(contries)

#contries.remove('이탈리아')
print(contries)
#contries.remove('일본')

contries.pop()
print(contries)
contries.pop()
print(contries)
contries.pop()
print(contries)
