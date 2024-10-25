def banner(text):
    print((len(text)+4) * "*")
    print("* " + text + " *")
    print((len(text) + 4) * "*")

def banner2(text):
    reeksSterren = "****"
    aantalSterren = len(text)
    for i in range(aantalSterren):
        reeksSterren = reeksSterren + "*"

    print(reeksSterren)
    print("* " + text + " *")
    print(reeksSterren)


name = input("Give a name for the banner: ")

banner(name)

banner2(name)