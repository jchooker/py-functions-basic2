from typing import Match
import numpy as np

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
# def firstPlusLen(arr):
#     return arr[0] + len(arr)
# arrScale = (int(input("Size of array?(1-15): ")))
# ronArrTest = [None]*arrScale
# for i in range(len(ronArrTest)):
#     ronArrTest[i] = np.random.randint(-10,200)
# print(ronArrTest)
# print(firstPlusLen(ronArrTest))

#4 - Values Greater Than Second
def valsGreaterThan2nd(arr):
    x = len(arr)
    arr2=[]
    if x < 2:
        return False
    elif x == 2:
        if arr[0]>arr[1]:
            arr2.append(arr[0])
    else:
        if arr[0]>arr[1]:
                arr2.append(arr[0])
        for i in range(2,x):
            if arr[i]>arr[1]:
                arr2.append(arr[i]) 
    # match x:
    #     case 0:
    #         return False
    #     case 1:
    #         return False
    #     case 2:
    #         if arr[0]>arr[1]:
    #             arr2.append(arr[0])
    #     case _:
    #         if arr[0]>arr[1]:
    #             arr2.append(arr[0])
    #         for i in range(2,x):
    #             if arr[i]>arr[1]:
    #                 arr2.append(arr[i]) 
    print(len(arr2))
    return arr2
arrScale = (int(input("Size of array?(0 or larger - but the fun starts at 2): ")))
newArr = [None]*arrScale
for i in range(len(newArr)):
    newArr[i] = np.random.randint(-200,200)
print(newArr)
print(valsGreaterThan2nd(newArr))