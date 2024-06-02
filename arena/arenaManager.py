from concurrent.futures import ThreadPoolExecutor
from block import Block
from rb.rbtree import RedBlackTree
import os


def insert_worker(tree, block_id, block):
    tree.insert(block_id, block)


def free_worker(tree, block_id):
    return tree.delete(block_id)


class ArenaManager:
    def __init__(self, tree_count=1):
        max_workers = os.cpu_count()  # Default to the number of CPU cores
        self.multi_rbtree = [RedBlackTree() for _ in range(tree_count)]
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def insert(self, block: Block):
        tree_index = block.id % len(self.multi_rbtree)
        tree = self.multi_rbtree[tree_index]
        future = self.executor.submit(insert_worker, tree, block.id, block)
        future.result()  # Wait for the result to ensure the operation is complete

    def free(self, id: int):
        tree_index = id % len(self.multi_rbtree)
        tree = self.multi_rbtree[tree_index]
        future = self.executor.submit(free_worker, tree, id)
        return future.result()  # Get the result once the operation is complete

    def to_list(self):
        result = []
        for tree in self.multi_rbtree:
            result += tree.inorder()
        return result

    def shutdown(self):
        self.executor.shutdown(wait=True)
