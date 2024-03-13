#리스트 타입 -> 셋 타입으로 변환
def remove_dup(l1):
    '''리스트의 중복 요소 제거 후 반환'''
    return list(set(l1))

def intersaction(l1, l2):
    '''교집합 결과 반환'''
    return list(set(l1) & set(l2))

def union(l1, l2):
    '''합집합 결과 반환'''
    return list(set(l1) | set(l2))

l1 = [1, 2, 3, 4, 5, 5, 9, 11, 11, 15]
l2 = [4, 5, 6, 7, 8]
l3 = []

print(remove_dup(l1))
print(intersaction(l1, l2))
print(union(l1, l2))
print(intersaction(l3, l2))
print(union(l3, l2))