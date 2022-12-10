# Written by karakara104
from copy import deepcopy


def move_boxes(n_moves: int, src: list[str], dst: list[str]) -> int:
    """
    Moves n_moves boxed from src to dst, one after the other
    Returns number of moved boxes
    """
    n_moved = 0
    for _ in range(n_moves):
        if len(src) > 0:
            dst.append(src.pop())
            n_moved += 1
    return n_moved


def move_n_boxes(n_boxes: int, src: list[str], dst: list[str]) -> int:
    """
    Moves n_moves boxed from src to dst, all at a time
    Returns number of moved boxes
    """
    dst.extend(src[-n_boxes:])
    del src[-n_boxes:]
    return 0


piles = []
piles2 = []

with open('input', 'r') as f:
    for containers in f:
        containers = containers.strip('\n') + ' '

        if containers[1].isdigit():
            f.readline()
            break

        if len(piles) == 0:
            n_piles = len(containers) // 4
            piles = [[] for _ in range(n_piles)]

        containers = [containers[i:i+4] for i in range(0, len(containers), 4)]

        for crate, pile in zip(containers, piles):
            if len(crate.strip()) > 0:
                pile.insert(0, crate[1])

    piles2 = deepcopy(piles)
    for move in f:
        move = move.strip()
        _, n, _1, src, _2, dst = move.split(' ')
        move_boxes(int(n), piles[int(src) - 1], piles[int(dst) - 1])
        move_n_boxes(int(n), piles2[int(src) - 1], piles2[int(dst) - 1])

print("Step 1 : Top crates : ", ''.join([piles[i][-1] for i in range(len(piles))]))
print("Step 2 Top crates : ", ''.join([piles2[i][-1] for i in range(len(piles2))]))
