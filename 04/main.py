# Written by karakara104

def is_included(range1: tuple[int, int], range2: tuple[int, int]):
    """
    Checks if range 1 is included in range 2
    range1 and range 2 are : (int, int)
    """
    return range1[0] >= range2[0] and range1[1] <= range2[1]


def is_overlapped(range1: tuple[int, int], range2: tuple[int, int]):
    """
    Checks if range 1 overlaps with range 2
    range1 and range 2 are : (int, int)
    """
    return range2[0] <= range1[0] <= range2[1] or range2[0] <= range1[1] <= range2[1]


number_included = 0
number_overlapped = 0

with open('input', 'r') as f:
    for assignment in f:
        assignment = assignment.strip()
        elf1, elf2 = assignment.split(',')

        elf1 = tuple(map(int, elf1.split('-')))
        elf2 = tuple(map(int, elf2.split('-')))

        number_included += is_included(elf1, elf2) or is_included(elf2, elf1)

        number_overlapped += is_overlapped(elf1, elf2) or is_overlapped(elf2, elf1)

print(f'Step 1: {number_included} included\nStep 2: {number_overlapped} overlapped')