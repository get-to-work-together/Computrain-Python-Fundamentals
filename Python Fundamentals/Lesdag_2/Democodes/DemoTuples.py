# Hier worden 2 tuples aangemaakt.
tplVoorbeeld1 = (1,2,3,4,5)
tplVoorbeeld2 = (6,7,8,9,10)

print(tplVoorbeeld1, hex(id(tplVoorbeeld1)))
print(tplVoorbeeld2, hex(id(tplVoorbeeld2)))

tplAlles = tplVoorbeeld1 + tplVoorbeeld2

print(tplAlles, hex(id(tplAlles)))

lstAllesVanTpl = list(tplAlles)

print(lstAllesVanTpl, hex(id(lstAllesVanTpl)))

lstAllesVanTpl.append(100)

tplAlles2 = tuple(lstAllesVanTpl)

print(tplAlles2, hex(id(tplAlles2)))

print(tplAlles2[0], hex(id(tplAlles2[0])))

print(tplAlles2[-1:0:-1])
print(tplAlles2[2:-1:2])



