#1 - Countdown
# def countdown(startNum):
#     counted=[]
#     for i in range(startNum,-1,-1):
#         counted.append(i)
#     return counted
# countVal = input("Enter a positive value from which to count down: ")
# print(countdown(int(countVal)))

#2 - Print and return
# def printReturn(arr):
#     print(arr[0])
#     return arr[1]
# arr2 = []
# arr2.append(int(input("Please input value 1: "))) 
# arr2.append(int(input("Please input value 2: ")))
# print(printReturn(arr2))

#3 - First Plus Length
import numpy as np
def firstPlusLen(arr):
    return arr[0] + len(arr)
arrScale = (int(input("Size of array?(1-15): ")))
ronArrTest = [None]*arrScale
for i in range(len(ronArrTest)):
    ronArrTest[i] = np.random.randint(-10,200)
print(ronArrTest)
print(firstPlusLen(ronArrTest))