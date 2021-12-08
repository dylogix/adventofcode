with open("day3/data.txt", "r") as data_file:
    values = data_file.readlines()

def binaryToDecimal(binary):
     
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal   

def compare_and_filter_common(list, column):
    filtered_values = []

    count_1 = 0
    count_0 = 0
    for value in list:
        if int(value[column].strip()) == 1:
            count_1 += 1
        elif int(value[column].strip()) == 0:
            count_0 += 1

    if count_1 < count_0:
        common = 0
    else:
        common = 1

    for value in list:
        if int(value[column].strip()) == common:
            filtered_values.append(value)

    return filtered_values

def compare_and_filter_uncommon(list, column):
    filtered_values = []

    count_1 = 0
    count_0 = 0
    for value in list:
        if int(value[column].strip()) == 1:
            count_1 += 1
        elif int(value[column].strip()) == 0:
            count_0 += 1

    if count_1 < count_0:
        common = 1
    else:
        common = 0
    
    for value in list:
        if int(value[column].strip()) == common:
            filtered_values.append(value)

    return filtered_values

tmp = values
tmp2 = values
for i in range(len(values[0])):
    if len(tmp) > 1:
        tmp = compare_and_filter_common(tmp, i)
    
    if len(tmp2) > 1:
        tmp2 = compare_and_filter_uncommon(tmp2, i)


oxygen_generator_rating = binaryToDecimal(int(tmp[0]))
co2_scrubber_rating = binaryToDecimal(int(tmp2[0]))

life_support_rating = oxygen_generator_rating * co2_scrubber_rating

print('Life support rating: ' + str(life_support_rating)) # solution: 2135254