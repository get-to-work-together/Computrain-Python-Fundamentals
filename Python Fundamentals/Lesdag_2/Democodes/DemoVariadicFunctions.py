def minimum(*numbers):
    print(numbers, type(numbers))
    lowestNumber = numbers[0]
    for number in numbers:
        if number < lowestNumber:
            lowestNumber = number
    return lowestNumber


print(minimum(5,6,4,65,4,6,6,4,65,9,-10))

#print(minimum([4,2,3,5,2],6,3,-1))