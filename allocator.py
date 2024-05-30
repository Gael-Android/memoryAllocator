from arena.arenaManager import ArenaManager
from freeSpace.freeSpaceManager import FreeSpaceManager
from memory_visualizer import MemoryVisualizer


class Allocator:
    def __init__(self):
        # self.chunk_size = 4096
        self.chunk_size = 80000
        self.freeSpaceManager = FreeSpaceManager(self.chunk_size)
        self.arena = ArenaManager()

    def print_stats(self):
        self.freeSpaceManager.to_list()
        print("Arena: XX MB")
        print("In-use: XX MB")
        print("Utilization: 0.XX")

    def malloc(self, id, size):
        block = self.freeSpaceManager.allocate(id, size)
        if block is not None:
            print("malloc block: ", block)
            self.arena.insert(block)
        else:
            return None

    def free(self, id):
        block = self.arena.free(id)
        if block is not None:
            print("free block: ", block)
            self.freeSpaceManager.insert(block)

    def new_chunk(self, chunk_size):
        self.freeSpaceManager.new_chunk(chunk_size)

    def return_call_data(self):
        return self.freeSpaceManager.to_list() + self.arena.to_list()


if __name__ == "__main__":
    allocator = Allocator()
    a_counter = 0
    f_counter = 0
    naive_total_memory_alloc = 0
    memory_visualizer = MemoryVisualizer()
    memory_visualizer.visualize(allocator.return_call_data())

    with open("./input.txt", "r") as file:
        n = 0
        for line in file:
            print("EPOCH : ", n)
            # print(line)
            req = line.split()
            if req[0] == 'a':
                a_counter += 1
                naive_total_memory_alloc += int(req[2])
                if allocator.malloc(int(req[1]), int(req[2])) is None:
                    print("Memory allocation failed")
            elif req[0] == 'f':
                f_counter += 1
                allocator.free(int(req[1]))

            if n == 50:
                break

            memory_visualizer.visualize(allocator.return_call_data())
            n += 1

    print("a_counter: ", a_counter)
    print("f_counter: ", f_counter)
    print("total_memory_alloc: ", naive_total_memory_alloc)
    print("average_memory_wanted: ", naive_total_memory_alloc / a_counter)

    print("total call : ", a_counter + f_counter)
    allocator.print_stats()
    memory_visualizer.make_gif()
