data_file = open("day1/data.txt", "r")
values = data_file.readlines()

counter = -1
previous = 0

for value in values:
    if int(value) > previous:
        counter += 1
    previous = int(value)
    print(counter)

print("Final Count: " + str(counter)) # solution: 1722