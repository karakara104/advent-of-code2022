# Written by karakara104

def find_marker(txt, n):
    """
    Finds the n letters maker
    Returns the position of the beginning of the packet
    """
    pos = 0
    # read chars 4 by for
    for i in range(len(txt) - n):
        if len(set(txt[i:i+n])) == n:
            pos = i + n
            break
    return pos

with open('input', 'r') as f:
    # only one line in the file
    message = f.readline().strip()
    print("Step 1 marker : ", find_marker(message, 4))
    print("Step 2 marker : ", find_marker(message, 14))
    

