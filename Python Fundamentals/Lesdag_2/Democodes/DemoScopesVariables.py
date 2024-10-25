#klaar = "einde"

def function1():
    a = 1
    b = 2
    print(a,b)

def function2():

    lstGetallen = list(range(1,100))
    for i in lstGetallen:
        if i % 2 == 0:
            klaar = "einde"
            print(i)

print(klaar)


function2()