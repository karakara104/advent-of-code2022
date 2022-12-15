# Written by karakara104
from anytree import Node, RenderTree, find_by_attr

TOTAL_DISK_SPACE = 70000000
SPACE_NEEDED = 30000000

root = Node("/", size=0)

with open('input', 'r') as f:
    parent_folder = ['/']
    for line in f:
        line = line.strip()
        
        if line[0] == '$':
            # a command is executed
            # either ls or cd
            cmd = line[2:]
            if 'cd' in cmd:
                if cmd.split(' ')[1] == '..':
                    # go back one node
                    parent_folder.pop()
                else:
                    # create node
                    folder_name = cmd.split(' ')[1]
                    if folder_name != '/':
                        Node(''.join(parent_folder) + folder_name, parent=find_by_attr(root, ''.join(parent_folder)), size=0)
                        parent_folder.append(folder_name)
        else:
            # not a cmd
            if 'dir' not in line:
                # we found a file !
                node = find_by_attr(root, ''.join(parent_folder))
                node.size = node.size + int(line.split(' ')[0])
                for parent_node in node.ancestors:
                    parent_node.size = parent_node.size + int(line.split(' ')[0])
print(RenderTree(root))

total_size = 0
for child in root.descendants:
    if child.size <= 100000:
        total_size += child.size

print('Step 1 size : ', total_size)

size_available = TOTAL_DISK_SPACE - root.size
size_needed = SPACE_NEEDED - size_available

# Find the smallest folder with a size >= size_needed
min_size = root.size
for child in root.descendants:
    if child.size >= size_needed and child.size < min_size:
        min_size = child.size

print('Step 2 min_size : ', min_size)
