filename = 'demo.txt'
file_out = 'out.txt'

try:
    
    with open(filename, 'r') as f:

        with open(file_out, 'w') as f_out:

            for linenr, line in enumerate(f, start = 1):
                line = line.strip()

                if line.startswith('r'):
                    print(linenr, line)
                    f_out.write(f'{linenr}: {line}\n')

except FileNotFoundError:
    
    print(f'Kan file {filename} niet openen')
