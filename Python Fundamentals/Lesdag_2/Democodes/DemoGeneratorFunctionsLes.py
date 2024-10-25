# Deze code is uit de volgende YouTube-film: https://youtu.be/bD05uGo_sVI

def square_numbersList(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

def square_numbersYield(nums):
    for i in nums:
        yield (i*i)

my_numsList = square_numbersList([1,2,3,4,5])

print(my_numsList)

my_numsYield = square_numbersYield([1,2,3,4,5])
print(my_numsYield)
for num in my_numsYield:
    print(num)

