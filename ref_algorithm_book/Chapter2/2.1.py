myList = [1, 2, 3, 4]
newList = myList[:]
newList2 = list(myList)

print(myList)
print(newList)
print(newList2)

#-------------------------------------

people = {"버피", "에인젤", "자일스"}
slayers = people.copy()
slayers.discard("자일스")
print(slayers)
slayers.remove("에인젤")

print(slayers)
print(people)

#-------------------------------------

myDict = {"안녕" : "세상"}
newDict = myDict.copy()
print(myDict)
print(newDict)

#-------------------------------------
#기타 객체의 깊은 복사를 할 때는 copy() 모듈 사용
import copy
myObj = "다른 어떤 객체"
newObj = copy.copy(myObj) #얕은 복사 (shallow copy)
newObj2 = copy.deepcopy(myObj) #깊은 복사 (deep copy)

print(myObj)
print(newObj)
print(newObj2)

#-------------------------------------

#슬라이싱
word = "오늘은 2월 20일 이직준비하자"
print(word[-1])
print(word[-2])
print(word[-2:])
print(word[:-2])
print(word[-0])
