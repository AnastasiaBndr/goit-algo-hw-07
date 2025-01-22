from src import AVL_tree
from random import randint

tree = AVL_tree()

for i in range(0,15):
    val=randint(1,101)
    tree.insert_value(val)


tree.print2DTree()
print(f"Max values: {tree.max_value_node()}")
print(f"Min values: {tree.min_value_node()}")
print(f"Sum values: {tree.sum_values()}")
