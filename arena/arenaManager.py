from block import Block
from rb.rbtree import RedBlackTree


class ArenaManager:
    def __init__(self):
        self.rbtree = RedBlackTree()

    def insert(self, block: Block):
        print(f"Arena :: inserting block : {block}")
        self.rbtree.insert(block.id, block)

    def free(self, id: int):
        print(f"Arena :: freeing block : {id}")
        return self.rbtree.delete(id)

    def visualize(self):
        print()
        self.rbtree.print_tree()
