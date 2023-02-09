theSum = 0.0
numcount = 0
while True:
    number = input("Enter a number or press Enter to quit: ")
    if number == "":
        break
    theSum += float(number)
    numcount += 1
print("The sum is", theSum)
if numcount > 0:
    print("The average is", theSum / numcount)
