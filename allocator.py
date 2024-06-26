import multiprocessing

from arena.arenaManager import ArenaManager
import time
from freeSpace.freeSpaceManager import FreeSpaceManager
from memory_visualizer import MemoryVisualizer


class Allocator:
    def __init__(self):
        self.chunk_option = 16
        self.tree_count_option = 1
        self.chunk_size = 1024 * self.chunk_option
        self.freeSpaceManager = FreeSpaceManager(self.chunk_size)
        self.arena = ArenaManager()

    def print_stats(self):
        in_use_memory = 0
        free_memory = 0
        for i in self.freeSpaceManager.to_list():
            free_memory += i.value.size
        for i in self.arena.to_list():
            in_use_memory += i.value.size
        print(f"free: {free_memory} MB")
        print(f"In-use: {in_use_memory} MB")
        print(f"공간활용률(사용공간/전체공간): {in_use_memory / (in_use_memory + free_memory) : .3f}")

    def malloc(self, id, size):
        block = self.freeSpaceManager.allocate(id, size)
        if block is not None:
            # print("malloc block: ", block)
            self.arena.insert(block)
            return True
        else:
            return None

    def free(self, id):
        block = self.arena.free(id)
        if block is not None:
            # print("free block: ", block)
            self.freeSpaceManager.insert(block)
            self.merge()
        else:
            pass
            print("Block not found")

    def new_chunk(self, chunk_size):
        self.freeSpaceManager.new_chunk(chunk_size)
        self.merge()

    def return_call_data(self):
        return self.freeSpaceManager.to_list() + self.arena.to_list()

    def merge(self):
        new_merged_block_size = 0
        new_start_address = self.freeSpaceManager.to_list()[0].value.start_address
        for i in self.freeSpaceManager.to_list():
            new_merged_block_size += i.value.size
        self.freeSpaceManager.clear(new_start_address, new_merged_block_size)


if __name__ == "__main__":
    allocator = Allocator()
    a_counter = 0
    f_counter = 0
    naive_total_memory_alloc = 0
    chunk_load_counter = 0
    memory_visualizer = MemoryVisualizer()
    memory_visualizer.visualize(allocator.return_call_data())

    start_time = time.time()  # 시작 시간 기록
    with open("./input.txt", "r") as file:
        n = 0
        for line in file:
            print("EPOCH : ", n)
            req = line.split()
            if req[0] == 'a':
                # print("malloc request: ", req[1], req[2])
                a_counter += 1
                naive_total_memory_alloc += int(req[2])
                if allocator.malloc(int(req[1]), int(req[2])) is None:
                    allocator.new_chunk(allocator.chunk_size)
                    chunk_load_counter += 1
                    # print("retrying malloc...")
                    allocator.malloc(int(req[1]), int(req[2]))
            elif req[0] == 'f':
                # print("free request: ", req[1])
                f_counter += 1
                allocator.free(int(req[1]))
            # allocator.freeSpaceManager.rbtree.print_tree()
            # allocator.arena.rbtree.print_tree()

            # if n == 30:
            #     break

            # memory_visualizer.visualize(allocator.return_call_data())
            n += 1

    end_time = time.time()  # 종료 시간 기록
    elapsed_time = end_time - start_time  # 경과 시간 계산

    print(f"Elapsed time: {elapsed_time : .3f} seconds")

    print("a_counter: ", a_counter)
    print("f_counter: ", f_counter)
    print("total_memory_alloc: ", naive_total_memory_alloc)
    print(f"average_memory_wanted: {naive_total_memory_alloc / a_counter : .2f}")

    print("total call : ", a_counter + f_counter)
    print("chunk load counter: ", chunk_load_counter)
    allocator.print_stats()

    # memory_visualizer.make_mp4()
