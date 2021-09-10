#1 - Countdown
def countdown(startNum):
    counted=[]
    for i in range(startNum,-1,-1):
        counted.append(i)
    return counted
countVal = input("Enter a positive value from which to count down: ")
print(countdown(int(countVal)))

