blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
print(the_bytes)

the_bytearray = bytearray(blist)
print(the_bytearray)

the_bytearray[1] = 127
print(the_bytearray)

#the_bytes[1] = 127
#print(the_bytes)

#-----------------------------------------------

x = 4 #100(2)
print(1 << x) #1을 왼쪽으로 x번 만큼 왼쪽으로 이동 

x = 8
print(x & (x-1))

x = 6
print(x & (x-1))