ui = input('Geef tekst: ')

print(repr(ui))

aantal_a = ui.count('a')
aantal_e = ui.count('e')
aantal_i = ui.count('i')
aantal_o = ui.count('o')
aantal_u = ui.count('u')

print(f'De a komt {aantal_a} keer voor.')
print(f'De e komt {aantal_e} keer voor.')
print(f'De i komt {aantal_i} keer voor.')
print(f'De o komt {aantal_o} keer voor.')
print(f'De u komt {aantal_u} keer voor.')

aantal_klinkers = aantal_a + aantal_e + aantal_i + aantal_o + aantal_u

print(f'Er zijn dus {aantal_klinkers} klinkers.')



totaal = 0
for letter in 'aeiou':
    aantal = ui.count(letter)
    totaal += aantal
    print(f'De {letter} komt {aantal} keer voor.')
print(f'Er zijn dus {totaal} klinkers.')



print(f'De tekst was {len(ui)} karakters lang.')
