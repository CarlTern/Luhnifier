import sys

# Obtains all numbers from file. 
def getNumbers(filePath):
    numbers = []
    try:
        file = open(filePath, "r")
        numbers = file.read().splitlines()
        file.close()
        return numbers
    except:
        print("No file found with name:", filePath)
        exit()

# card number in string format.
def luhnify(number):
    number = number[::-1]
    sumOfNumbers = 0
    xHasEvenIndex = False
    result = 0
    for index in range(len(number)):
        digit = number[index]
        # If true => we have X. 
        if (digit.isdigit() is False):
            x = digit
            if (index % 2 is not 0):
                xHasEvenIndex = True
            continue
        digit = int(digit)
        if (index % 2 is not 0):
            digit = int(digit) * 2
        if (digit > 9):
            for individualDigit in str(digit):
                result += int(individualDigit)
            digit = result
            result = 0
        sumOfNumbers += digit
    if(sumOfNumbers % 10 is not 0):
        x = 10 - sumOfNumbers % 10
    else:
        return 0    
    if (xHasEvenIndex):
        if(x % 2 is 0):
            return  int(x / 2)
        else:
            product = "1" + str( x - 1)
            return int(int(product) / 2)
    return x

# Main method.   
if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except:
        print ("Please specify a file path")
        exit()
    result = []
    numbers = getNumbers(path)
    for number in numbers:
        result.append(str(luhnify(number)))
    print(''.join(result))