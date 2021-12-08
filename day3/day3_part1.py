with open("day1/data.txt", "r") as data_file:
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
    
def get_common(column):
    count_1 = 0
    count_0 = 0
    for value in values:
        if int(value[column]) == 1:
            count_1 += 1
        elif int(value[column]) == 0:
            count_0 += 1
    if count_1 < count_0:
        return '0'
    else:
        return '1'

def get_uncommon(column):
    count_1 = 0
    count_0 = 0
    for value in values:
        if int(value[column]) == 1:
            count_1 += 1
        elif int(value[column]) == 0:
            count_0 += 1
    if count_1 < count_0:
        return '1'
    else:
        return '0'

gamma_bin = ''
epsilon_bin = ''

for i in range(0, 12):
    gamma_bin = gamma_bin + get_common(i)
    epsilon_bin = epsilon_bin + get_uncommon(i)

gamma = binaryToDecimal(int(gamma_bin))
epsilon = binaryToDecimal(int(epsilon_bin))

power_consumption = gamma * epsilon

print('Power Consumption: ' + str(power_consumption)) # solution: 2595824