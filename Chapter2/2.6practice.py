#2.6.1 문자열 전체 반전하기
def revert1(s):
    if s:
        s = s[-1] + revert1(s[:-1])
    return s

def revert2(str):
    return str[::-1]

string_ = '안녕 세상아 !*'
print(revert1(string_))
print(revert2(string_))

#--------------------------------------------
#2.6.2 문자열 단어 단위로 반전하기
def word_revert(str, p1=0, p2=None):
    if len(str) < 2:
        return str
    p2 = p2 or len(str)-1
    while p1 < p2:
        str[p1], str[p2] = str[p2], str[p1]
        p1 += 1
        p2 -= 1

def reversing_words(str):
    word_revert(str)
    p = 0
    start = 0
    while p < len(str):
        if str[p] == " ": #u"\u0020":
            #단어 다시 반전
            word_revert(str, start, p-1)
            start = p+1
        p += 1

    #마지막 단어 반전
    word_revert(str, start, p-1)
    return "".join(str)

print(reversing_words(list(string_)))

#-----------------------------------------
#반복문 1번만 사용하기
def reverse_word_brute(str):
    word, sentense = [], []
    for character in str:
        if character != " ":
            word.append(character)
        else:
            #조건문에서 빈 리스트는 False이므로 
            if word:
                sentense.append("".join(word))
            word = []
    if word != "":
        sentense.append("".join(word))
    sentense.reverse()
    return " ".join(sentense)

print(reverse_word_brute(string_))

#-------------------------------------------------------------
#문자열 공백으로 구분 후 리스트 생성, 슬라이싱 활용
def reversing_words_slice(word):
    new_word = []
    words = word.split(" ")
    for word in words[::-1]:
        new_word.append(word)
    return " ".join(new_word)

print(reversing_words_slice(string_))

#-------------------------------------------------------------
#반복문 없이 문자열 메서드만으로 해결
def reversing_words(str):
    words = str.split(" ")
    rev_set = " ".join(reversed(words))
    return rev_set
def reveersing_words2(str):
    words = str.split(" ")
    words.reverse()
    return " ".join(words)


#-------------------------------------------
#2.6.3단순문자열 압축
def str_comprehension(s):
    count, last = 1, ""
    list_aux = []
    for i, c in enumerate(s):
        if last == c:
            count += 1
        else:
            if i != 0:
                list_aux.append(str(count))
            list_aux.append(c)
            count = 1
            last = c
    list_aux.append(str(count))
    return "".join(list_aux)

#-------------------------------------------
#2.6.3문자열 순열
import itertools

def perm(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        for cc in perm(s[:1] + s[i+1:]):
            res.append(c + cc)
    return res

def perm2(s):
    res = itertools.permutations(s)
    return ["".join(i) for i in res]
    
def combinations(s):
    if len(s) < 2:
        return s
    res = []
    for i, c in enumerate(s):
        res.append(c) #추가된부분
        for j in combinations(s[:1] + s[i+1:]):
            res.append(c + j)
    return res