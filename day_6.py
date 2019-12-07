# Anytree suggested by a talented collegue https://github.com/xtream1101
from anytree import Node, RenderTree, AsciiStyle, PreOrderIter, Walker

with open('input_day_6.txt', 'r') as f:
    input = f.read().split('\n')

# input = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L""".split("\n")

# input = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN""".split("\n")

orbit_pairs = []
nodes = {}

for orbit_pair in input:
    if not orbit_pair:
        break
    pairs = orbit_pair.split(')')
    parent = pairs[0]
    child = pairs[1]

    orbit_pairs.append((parent, child))
    if parent not in nodes:
        nodes[parent] = Node(parent)

    if child not in nodes:
        nodes[child] = Node(child)

for parent, child in orbit_pairs:
    nodes[child].parent = nodes[parent]

for node in nodes.values():
    if node.is_root:
        print(node)
#
print(RenderTree(nodes['COM'], style=AsciiStyle()))

##
# Part 1
##
direct = 0
indirect = 0
for node in PreOrderIter(nodes['COM']):
    ancestors = len(node.ancestors)
    if ancestors == 0:
        continue

    direct += 1
    indirect += ancestors - 1

print(direct + indirect)

##
# Part 2
##
san_parent = nodes['SAN'].parent
print(san_parent.name)
w = Walker()

walk = w.walk(nodes['YOU'].parent.parent, nodes['SAN'].parent)
print(walk)
full_path = (*walk[0], walk[1], *walk[2])
print(len(full_path))
