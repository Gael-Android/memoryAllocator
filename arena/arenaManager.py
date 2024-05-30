from block import Block
from rb.rbtree import RedBlackTree


class ArenaManager:
    def __init__(self):
        self.rbtree = RedBlackTree()

    def insert(self, block: Block):
        print(f"Arena :: inserting block : {block}")
        self.rbtree.insert(block.id, block)

    def free(self, id: int):
        print(f"Arena :: freeing block id : {id}")
        free_block = self.rbtree.delete(id)
        print(f"Arena :: free block : {free_block}")
        return free_block

    def to_list(self):
        return self.rbtree.inorder()
