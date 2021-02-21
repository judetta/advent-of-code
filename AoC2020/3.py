with open('3_input.txt') as f:
    input_list = f.readlines()
input_list = [x.strip() for x in input_list]

# Slope 1: Right 1, down 1

number_of_trees_slope1 = 0
pos_slope1 = 0

for row in input_list:
    while pos_slope1 >= len(row):
        pos_slope1 -= len(row)
    if row[pos_slope1] == '#':
        number_of_trees_slope1 += 1
    pos_slope1 += 1

print('Number of trees slope 1:', number_of_trees_slope1)

# Slope 2: Right 3, down 1

number_of_trees_slope2 = 0
pos_slope2 = 0

for row in input_list:
    while pos_slope2 >= len(row):
        pos_slope2 -= len(row)
    if row[pos_slope2] == '#':
        number_of_trees_slope2 += 1
    pos_slope2 += 3

print('Number of trees slope 2:', number_of_trees_slope2)

# Slope 3: Right 5, down 1.

number_of_trees_slope3 = 0
pos_slope3 = 0

for row in input_list:
    while pos_slope3 >= len(row):
        pos_slope3 -= len(row)
    if row[pos_slope3] == '#':
        number_of_trees_slope3 += 1
    pos_slope3 += 5

print('Number of trees slope 3:', number_of_trees_slope3)

# Slope 4: Right 7, down 1.

number_of_trees_slope4 = 0
pos_slope4 = 0

for row in input_list:
    while pos_slope4 >= len(row):
        pos_slope4 -= len(row)
    if row[pos_slope4] == '#':
        number_of_trees_slope4 += 1
    pos_slope4 += 7

print('Number of trees slope 4:', number_of_trees_slope4)

# Slope 5: Right 1, down 2.

number_of_trees_slope5 = 0
pos_slope5 = 0

for i, row in enumerate(input_list):
    if i % 2 == 0:
        while pos_slope5 >= len(row):
            pos_slope5 -= len(row)
        if row[pos_slope5] == '#':
            number_of_trees_slope5 += 1
        pos_slope5 += 1

print('Number of trees slope 5:', number_of_trees_slope5)

# What do you get if you multiply together the number of trees 
# encountered on each of the listed slopes?

multiplied_trees = (number_of_trees_slope1 
                    * number_of_trees_slope2 
                    * number_of_trees_slope3 
                    * number_of_trees_slope4 
                    * number_of_trees_slope5)

print('Numbers multiplied:', multiplied_trees)
