from block import Block
from rb.rbtree import RedBlackTree, Node


class FreeSpaceManager:
    def __init__(self, chunk_size: int):
        self.current_chunk_size = chunk_size
        self.rbtree = RedBlackTree()
        self.rbtree.insert(chunk_size, Block(-1, 0, chunk_size - 1, chunk_size))

    def insert(self, block: Block):
        print(f"FreeSpace :: inserting block : {block}")
        self.rbtree.insert(block.size, block)

    def new_chunk(self, chunk_size: int):
        self.rbtree.insert(chunk_size,
                           Block(-1, self.current_chunk_size, self.current_chunk_size + chunk_size - 1, chunk_size))
        self.current_chunk_size += chunk_size

    def allocate(self, id: int, size: int):
        # 가장 딱 맞는 노드를 찾는다
        most_suited_block = self.rbtree.find_closest_greater(size)
        if most_suited_block is None:  # 메모리 없으면 할당 불가
            print("No memory available")
            return None

        # 가장 딱 맞는 노드를 찾았다면 쪼개서 할당
        fit_block = self.split(most_suited_block, size, id)
        return fit_block

    # 블럭을 딱 맞는 크기로 나누고 나머지를 다시 트리에 넣는다
    # 할당하고자 하는 블럭을 return
    def split(self, original_block: Node, wanted_size, id):
        print(f"original block size : {original_block.value.size} wanted size : {wanted_size}")
        # 블럭이 딱 맞는 경우 -> 그냥 할당
        if original_block.get_key() == wanted_size:
            print("Allocated perfect!")
            new_block = self.rbtree.delete(original_block.get_key())
            return new_block
        else:
            # 블럭을 나누고 나머지를 다시 트리에 넣는다. -> 원하는 크기를 가진 블럭을 return
            print("splitting!")
            new_block = Block(id, original_block.value.start_address,
                              original_block.value.start_address + wanted_size - 1,
                              wanted_size)
            rest_block = Block(-1, original_block.value.start_address + wanted_size,
                               original_block.value.end_address,
                               original_block.value.size - wanted_size)
            print(f"new used block : {new_block}")
            print(f"rest free block : {rest_block}")
            self.rbtree.delete(original_block.get_key())
            self.rbtree.insert(rest_block.size, rest_block)
            return new_block

    def to_list(self):
        return self.rbtree.inorder()
