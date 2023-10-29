# The Most Awesome Lotto Comparator In The World
import random

staticNumbers=[4,6,12,19,22,27,31]

def rndNums(size, min_value, max_value):
    array=[]
    while len(array)<size:
        new_element=random.randint(min_value,max_value)
        if new_element not in array:
            array.append(new_element)
    array.sort()
    return array

def areArraysIdentical(array1,array2):
    if len(array1)!=len(array2):
        return False

    for i in range(len(array1)):
        if array1[i]!=array2[i]:
            return False

    return True

x=0
y=0

for i in range(1000000):
    lottoNumbersDraw=rndNums(7,1,32)
    lottoNumbersPlay=rndNums(7,1,32)

    rndResult = areArraysIdentical(lottoNumbersDraw,lottoNumbersPlay)
    if rndResult:
        x += 1
        print(lottoNumbersDraw)

    staticResult=areArraysIdentical(staticNumbers,lottoNumbersDraw)
    if staticResult:
        y+=1
        print(lottoNumbersDraw)

print("Total numers of wins for random play", x)
print("Total number of wins for static play", y)