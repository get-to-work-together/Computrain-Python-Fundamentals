values = [23,67,34,89,34,56,56,86,67]
value_to_look_for = 56

first_index = values.index(value_to_look_for)

all_indeces = []
p = -1
while True:
    try:
        p = values.index(value_to_look_for, p + 1)
        all_indeces.append(p)
    except:
        break

# or

# all_indeces = []
# for i, value in enumerate(values):
#     if value == value_to_look_for:
#         all_indeces.append(i)

# or

# all_indeces = [i for i, value in enumerate(values) if value == value_to_look_for]

print(first_index)

print(all_indeces)