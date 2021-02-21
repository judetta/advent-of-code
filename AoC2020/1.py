with open('1_input.txt') as f:
    input_list = f.readlines()
input_list = [x.strip() for x in input_list]
input_list = [int(x) for x in input_list]

#print(input_list)
#print(len(input_list))

for number in input_list:
    number1 = number
    input_list.remove(number)
    for number in input_list:
        number2 = number
        for number in input_list:
            number3 = number
            if number1 + number2 + number3 == 2020:
                product = number1 * number2 * number3
                print(product)
            else:
                continue
