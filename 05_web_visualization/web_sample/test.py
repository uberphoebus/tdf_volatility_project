a=5
print(a)
if a>3 :
	print('aA'*3)
elif a>4:
	print('bB')
else :
	print('cC')

# for i=1; i<5; i++
for i in range(1,5):
	print(i, end='')

a=0
while(True):
	print(i, end='')
	a+=1
	if a>5:
		break

# int add(int num1, int num2) {
# 	return num1 + num2;
# }

'''  /* ..  */
int add(int num1, int num2) {
	return num1 + num2;	
}'''
print()
def add(p1, p2):
	return p1,p2

r1, r2=add('a',4)
print(r1,"과", r2)

# list tuple dict
list = (1,2,'a', ['AA','BB'])   #[1,2,'a', ['AA','BB']]
for i in list:
	print(i, end='')
print()
print(list[3][1])  #['AA','BB']

# list.append("ccc")
# print(list)

# [i]  (4*5)  {k:v}
dict = {"id":"kim", "pw":"111"}
print(dict["pw"])
dict["tel"] = "1-2-3"
dict["pw"] = "333"
print(dict)

list = [[1,2],[3,4],[5,6]]
print(list[1][0])  #3

import numpy as np
arr = np.array(list)
print(arr[1][0])
print(type(arr), type(list))

a = "12"
b = int(a)  #(int)a
print(type(b))


