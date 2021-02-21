with open('4_input.txt') as f:
    puzzle_input = f.read()

# split passport data into list by blank lines in input
batch = puzzle_input.split('\n\n')

# clear newlines from each passport data chunk
batch = [passport.replace('\n', ' ') for passport in batch]
batch = [passport.split() for passport in batch]

required_fields = [
    "byr", # (Birth Year) - four digits; at least 1920 and at most 2002.
    "iyr", # (Issue Year) - four digits; at least 2010 and at most 2020.
    "eyr", # (Expiration Year) - four digits; at least 2020 and at most 2030.
    "hgt", # (Height) - a number followed by either cm or in:
            # If cm, the number must be at least 150 and at most 193.
            # If in, the number must be at least 59 and at most 76.
    "hcl", # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    "ecl", # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    "pid", # (Passport ID) - a nine-digit number, including leading zeroes.
    # "cid" # (Country ID) - ignored, missing or not.
]

# Part 1

valid_passports_count1 = 0
for_further_validation = [] # list of passports with required fields for part 2

for passport in batch:
    passport_fields = dict((x, y) for x, y in (field.split(':') 
                                                for field in passport))
    required_fields_count = 0
    for field in required_fields:
        if field in passport_fields:
            required_fields_count += 1
    if required_fields_count == 7:
        valid_passports_count1 += 1
        for_further_validation.append(passport_fields) # for part 2


print(f'Total number of passports validated: {len(batch)}')
print(f'Number of valid passports (part 1): {valid_passports_count1}')


# Part 2

valid_hcl_chars = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

valid_passports_count2 = 0

for passport in for_further_validation:
    if (1920 <= int(passport.get('byr')) <= 2002 and
         2010 <= int(passport.get('iyr')) <= 2020 and
         2020 <= int(passport.get('eyr')) <= 2030 and
         passport.get('ecl') in valid_ecl and 
         len(passport.get('hcl')) == 7 and 
         passport.get('hcl').startswith('#') and
         len(passport.get('pid')) == 9 and
         passport.get('pid').isdigit()):
        is_valid = True
        for character in passport.get('hcl').strip('#'):
            if character in valid_hcl_chars:
                continue
            is_valid = False
        if is_valid and passport.get('hgt').endswith('cm'):
            if 150 <= int(passport.get('hgt').strip('cm')) <= 193:
                valid_passports_count2 += 1
        elif is_valid and passport.get('hgt').endswith('in'):
            if 59 <= int(passport.get('hgt').strip('in')) <= 76:
                valid_passports_count2 += 1

print(f'Number of valid passports (part 2) {valid_passports_count2}')