# Written by karakara104

def priority(item):
    """
    item is a letter (a-ZA-Z)
    Returns the priority :
    Lowercase item types a through z have priorities 1 through 26.
    Uppercase item types A through Z have priorities 27 through 52.
    Returns an int
    """
    prio = 0
    if item.isupper():
        # item is uppercase
        prio = ord(item.swapcase()) - ord('A') - 5
    else:
        # item is lowercase
        prio = ord(item.swapcase()) - ord('A') + 1
    return prio


priority_sum = 0
priority_part_two = 0

with open('input', 'r') as f:
    for backpack in f:
        backpack = backpack.strip()
        common_letter = set(backpack[0:len(backpack)//2]) & set(backpack[len(backpack)//2:])
        priority_sum += priority(*common_letter)

print("First part : summed priorities : ", priority_sum)


priority_part_two = 0

with open('input', 'r') as f:
    elves_group = []
    for backpack in f:
        backpack = backpack.strip()

        elves_group.append(set(backpack))

        if len(elves_group) == 3:
            common_letter = set.intersection(*elves_group)
            priority_part_two += priority(*common_letter)
            elves_group = []


print("Second part : summed priorities : ", priority_part_two)



