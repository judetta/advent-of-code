with open('2_input.txt') as f:
    input_list = f.readlines()
input_list = [x.strip() for x in input_list]
input_list = [x.replace(':', '') for x in input_list]
input_list = [x.split() for x in input_list]
for x in input_list:
    x[0] = x[0].split('-')

valid_words_part1 = 0
valid_words_part2 = 0

for row in input_list:
    rule_range = row[0]
    minimum = int(rule_range[0])
    maximum = int(rule_range[1])
    rule = row[1]
    word = row[2]
    rule_count = word.count(rule)
    if minimum <= rule_count <= maximum:
        valid_words_part1 += 1
    pos1 = minimum - 1 
    pos2 = maximum - 1
    if word.count(rule) > 0:
        if word[pos1] == rule and word[pos2] != rule:
            valid_words_part2 += 1
        elif word[pos1] != rule and word[pos2] == rule:
            valid_words_part2 += 1

print(f'Count of valid passwords, part 1: {valid_words_part1}')
print(f'Count of valid passwords, part 2: {valid_words_part2}')

"""
for row in input_list:
    rule_range = row[0]
    pos1 = int(rule_range[0]) - 1
    pos2 = int(rule_range[1]) - 1
    rule = row[1]
    word = row[2]
    rule_count = word.count(rule)
    if rule_count > 0:
        if word[pos1] == rule and word[pos2] != rule:
            valid_words2 += 1
        elif word[pos1] != rule and word[pos2] == rule:
            valid_words2 += 1

print(valid_words_part2)
"""