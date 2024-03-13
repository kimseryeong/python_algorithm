
#한 파일에서 사용된 모든 단어를 알파벳순으로 출력하며 각 단어가 등장한 횟수 출력
import string
import sys

def count_unique_word():
    words = {}
    strip = string.whitespace + string.punctuation + string.digits + "\"'"
    for filename in sys.argv[1:]:
        with open(filename) as file:
            for line in file:
                for word in line.lower().split():
                    word = word.strip(strip)
                    if len(word) > 2:
                        words[word] = words.get(word, 0) + 1
    for word in sorted(words):
        print("{}: {}번".format(word, words[word]))                    