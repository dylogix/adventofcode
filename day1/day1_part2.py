with open("day1/data.txt", "r") as data_file:
    values = data_file.readlines()

counter = -1
previous = 0
pos = 0

for value in values:
    if pos + 1 > len(values) -1:
        v_sum = int(value)
    elif pos + 2 > len(values) -1:
        v_sum = int(value) + int(values[pos + 1])
    else:
        v_sum = int(value) + int(values[pos + 1]) + int(values[pos + 2])
    print(v_sum)

    if v_sum > previous:
        counter += 1

    pos += 1
    previous = int(value)
    print(counter)

print("Final Count: " + str(counter)) # solution: 1748