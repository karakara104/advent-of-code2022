# Written by karakara104

# List with content of the bags :
# the structure will be : [n_cal_owned_by_first_elf, n_cal_2nd_elf, ...]
calories = []
elf = 0

# read input
with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        if len(calories) <= elf:
            calories.append(0)

        if len(line.strip()) == 0:
            # next elf
            elf += 1
        else:
            calories[elf] += int(line)

# Part 1
print('Max calories carried by an elf : ', max(calories))

# Part 2
top_3 = sum(sorted(calories, reverse=True)[:3])
print('Top 3 elves : ', top_3)

