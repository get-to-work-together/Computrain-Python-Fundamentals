filename = "data.txt"

with open(filename) as f:
    for row in f:
        line = row.strip()
        print(line)
        if "ID" in line:
            print(line)