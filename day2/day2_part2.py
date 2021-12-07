data_file = open("day2/data.txt", "r")
values = data_file.readlines()

values_processed = []

for value in values:
    test = value.split()
    values_processed.append(test)

horizontal = 0
depth = 0
aim = 0

for value in values_processed:
    command = value[0]
    amount = int(value[1])
    if command == 'forward':
        horizontal += amount
        depth += aim * amount
    elif command == 'down':
        aim += amount
    elif command == 'up':
        aim -= amount

print('Final Position: ' + str(int(horizontal) * int(depth))) # solution: 1599311480