### 선형 리스트 함수


##### 선형 리스트 생성 #####
array = []
def add_data(data):
    array.append(None) #배열 끝에 빈공간 생성
    arrLen = len(array)
    array[arrLen-1] = data #배열 끝에 데이터 삽입



##### 선형 리스트 삽입 #####
array2 = ['딸기', '포도', '사과', '레몬', '자몽']
def insert_data(position, data):
    if position < 0 or position > len(array2):
        print('데이터 삽입할 범위를 벗어남')
        return 
    
    #배열 끝에 빈공간 생성
    array2.append(None)

    #배열 뒤에서부터 순회하면서 
    #position에 None값 삽입 & 값 한칸씩 뒤로 미루기
    for i in range(len(array2)-1, position, -1):
        array2[i] = array2[i-1]
        array2[i-1] = None
    
    #지정한 위치에 데이터 추가
    array2[position] = data
        

##### 선형 리스트 데이터 삭제 #####
def del_data(position):
    if position < 0 or position > len(array2):
        print('데이터 삭제할 범위를 벗어남')
        return 
    
    array2[position] = None

    for i in range(position+1, len(array2)):
        array2[i-1] = array2[i]
        array2[i] = None
    
    del(array2[len(array2)-1])