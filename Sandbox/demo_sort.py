
zin = 'dat waren dan bijna twee dagen vol met python'

woorden = zin.split()

def aantal_e(word):
    return word.count('e')

lambda word: word.count('e')


def aantal_klinkers(word):
    return sum([word.count(v) for v in 'aeiou'])

lambda word: sum([word.count(v) for v in 'aeiou'])


def sort_key(word):
    return len(word), word



for woord in sorted(woorden, key = lambda word: sum([word.count(v) for v in 'aeiou'])):
    print(woord)
