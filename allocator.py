from arena.arenaManager import ArenaManager
from freeSpace.freeSpaceManager import FreeSpaceManager


class Allocator:
    def __init__(self):
        self.chunk_size = 4096
        self.freeSpaceManager = FreeSpaceManager(self.chunk_size)
        self.arena = ArenaManager()

    def print_stats(self):
        self.freeSpaceManager.visualize()
        print("Arena: XX MB")
        print("In-use: XX MB")
        print("Utilization: 0.XX")

    def malloc(self, id, size):
        self.freeSpaceManager.allocate(id, size)

    def free(self, id):
        pass


if __name__ == "__main__":
    allocator = Allocator()
    a_counter = 0
    f_counter = 0
    naive_total_memory_alloc = 0

    with open("./input.txt", "r") as file:
        n = 0
        for line in file:
            # print(line)
            req = line.split()
            if req[0] == 'a':
                a_counter += 1
                naive_total_memory_alloc += int(req[2])
                allocator.malloc(int(req[1]), int(req[2]))
            elif req[0] == 'f':
                f_counter += 1
                # allocator.free(int(req[1]))

            # if n%100 == 0:
            #     print(n, "...")

            n += 1

    print("a_counter: ", a_counter)
    print("f_counter: ", f_counter)
    print("average_memory_wanted: ", naive_total_memory_alloc / a_counter)

    print("total: ", a_counter + f_counter)
    allocator.print_stats()
