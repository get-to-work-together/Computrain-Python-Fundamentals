name = 'Guido'
place = 'Amsterdam'
age = 62


print(name + ' is ' + str(age) + ' jaar.')
print('%s is %d jaar en woont in %s' % (name, age, place))
print('{} is {} jaar en woont in {}'.format(name, age, place))

leeftijdString = "100"
print(leeftijdString.isnumeric())


print(name.upper())
print(name.lower())
print(name.isnumeric())
print(name.split("i"))
print(name.count('i'))

testString = "{} {} {}"
print(testString.format(3,5,5))

print(name.endswith("i"))


