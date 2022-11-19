array = [11, 4, 7, 5, 10, 9, 13, 1]
print("array used:" , array)
print("\n")

def bubble(array):
	x = len(array)
	for i in range(x-1):
		for j in range(0, x-i-1):
			if array[j] > array[j + 1]:		
				array[j], array[j + 1] = array[j + 1], array[j]		
bubble(array)
print("Bubble")
print("BS array :" ,array)
print("\n")

#///////////////////

def selec(arr, x):
	for ninja in range(x):
		m = ninja
		for i in range(ninja + 1,x):
			if arr[i] < arr[m]:
				m = i
		(array[ninja], array[m]) = (array[m], array[ninja])
x = len(array)
selec( array ,x)
print('Selec')
print("SS :",array)
print("\n")

#/////////////

def insert(ninja):
    for x in range(1, len(ninja)):
        key = ninja[x]
        i = x - 1      
        while i >= 0 and key < ninja[i]:
            ninja[i + 1] = ninja[i]
            i = i - 1
        ninja[i + 1] = key	
insert(array)
print('insert')
print("ls :",array)
