from block import Block
from rb.rbtree import RedBlackTree


class ArenaManager:
    def __init__(self):
        self.rbtree = RedBlackTree()

    def insert(self, block: Block):
        self.rbtree.insert(block.id, block)

    def free(self, id: int):
        last_in_use_block_end_address = 0
        free_block = self.rbtree.delete(id)
        if free_block is None:
            # quit()
            return None
        for node in self.rbtree.inorder():
            if node.value.start_address > free_block.start_address:
                node.value.start_address -= free_block.size
                node.value.end_address -= free_block.size
                last_in_use_block_end_address = node.value.end_address
        return Block(-1, last_in_use_block_end_address, last_in_use_block_end_address + free_block.size - 1,
                     free_block.size)

    def to_list(self):
        return self.rbtree.inorder()
