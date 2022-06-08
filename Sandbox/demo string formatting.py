
naam = 'Peter'
leeftijd = 66

pi = 3.14159

print( 'Peter is 66 jaar oud'  )

print( naam + ' is ' + str(leeftijd) + ' jaar oud')


# format operator %
#
# format symbols: %s, %d, %f
# https://www.tutorialspoint.com/string-formatting-operator-in-python


print( '%s is %d jaar oud' % (naam, leeftijd)   )
print( 'pi is ongeveer %.2f' % pi )

s = '%s is %d jaar oud' % (naam, leeftijd)
print(s)

# f string

print( f'{naam} is {leeftijd} jaar oud'  )
print( f'pi is ongeveer {pi:.2f}' )

s = f'{naam} is {leeftijd} jaar oud'
print(s)
