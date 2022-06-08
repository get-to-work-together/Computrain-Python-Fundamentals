

boodschappenlijstje = []

boodschappenlijstje.append('boter')
boodschappenlijstje.append('eieren')
boodschappenlijstje.append('appels')
boodschappenlijstje.append('kaas')

boodschappenlijstje.extend(['prei','sla'])

print(boodschappenlijstje)

print( f'Er staan {len(boodschappenlijstje)} items op jouw lijstje')

print(sorted(boodschappenlijstje))
