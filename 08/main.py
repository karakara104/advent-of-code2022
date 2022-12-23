# Written by karakara104
import numpy as np

def is_visible(trees_list, index_tree):
    """
    Tests if a tree if visible in the given line
    """
    visibility = True
    visibility_reversed = True
    tree_size = trees_list[index_tree]
    for tree in trees_list[:index_tree]:
        if int(tree) >= tree_size:
            visibility = False

    for tree in trees_list[::-1][:len(trees_list) - 1 - index_tree]:
        if int(tree) >= tree_size:
            visibility_reversed = False
    return visibility or visibility_reversed 


def nb_trees_visible(trees_list, height_tree):
    """
    Calculates the number of trees visible in tree_list while on a tree at tree_height
    A tree is visible if its height is < height_tree
    All the trees behind a tree >= height_tree are not visible
    The last visible tree is either on the edge (last item of the list)
    or >= heigth_tree
    Returns an int : number of visible trees
    """
    nb_vis_trees = 0
    for tree in trees_list:
        if int(tree) >= height_tree:
            nb_vis_trees += 1
            break
        elif int(tree) < height_tree:
            nb_vis_trees += 1
    return nb_vis_trees


def calc_scenic_score(my_forest, x_tree, y_tree):
    """
    Calculates the scenic score of a given tree
    my_forest is a numpy array
    x_tree is the x coordinate of the tree
    y_tree is the y coordinate of the tree
    returns an int
    """
    sc = 1
    # Look right
    sc *= nb_trees_visible(my_forest[x_tree][y_tree + 1:], int(my_forest[x_tree,y_tree]))
    # Look left
    sc *= nb_trees_visible(my_forest[x_tree][:y_tree][::-1], int(my_forest[x_tree,y_tree]))
    # Look down
    sc *= nb_trees_visible(my_forest[:,y_tree][x_tree + 1:], int(my_forest[x_tree,y_tree]))
    # Look up
    sc *= nb_trees_visible(my_forest[:,y_tree][:x_tree][::-1], int(my_forest[x_tree,y_tree]))
    return sc


forest = []

with open('input', 'r') as f:
    for trees in f:
        trees = trees.strip()
        forest.append([int(tree) for tree in trees])

# Convert to numpy array
forest = np.array(forest, dtype=int)
visible_trees = np.full(forest.shape, -1, dtype=int)
scenic_score = np.full(forest.shape, 0, dtype=int)


# Outer trees are visible
for i in [0, -1]:
    visible_trees[i] = np.full(len(visible_trees[i]), True, dtype=bool)
    visible_trees[:,i] = np.full(len(visible_trees[:,i]), True, dtype=bool)


with np.nditer(forest, flags=['multi_index']) as it:
    for tree in it:
        x, y = it.multi_index
        if visible_trees[x,y] != -1: # no need to calculate on edge trees
            continue
        visible_trees[x,y] = is_visible(forest[x], y) or is_visible(forest[:,y], x)

print('Step 1 : n of trees visible : ', visible_trees.sum())

# Step 2 : calculate scenic score for each tree
with np.nditer(forest, flags=['multi_index']) as it:
    for tree in it:
        x, y = it.multi_index
        scenic_score[x,y] = calc_scenic_score(forest, x, y) 

print('Step 2 : max scenic score : ', scenic_score.max())
