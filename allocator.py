
class Allocator:
    def __init__(self):
        self.chunk_size = 4096

    def print_stats(self):
        print("Arena: XX MB")
        print("In-use: XX MB")
        print("Utilization: 0.XX")

    def malloc(self, id, size):
        pass

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
                # allocator.malloc(int(req[1]), int(req[2]))
                a_counter += 1
                naive_total_memory_alloc += int(req[2])
            elif req[0] == 'f':
                # allocator.free(int(req[1]))
                f_counter += 1

            # if n%100 == 0:
            #     print(n, "...")

            n += 1

    print("a_counter: ", a_counter)
    print("f_counter: ", f_counter)
    print("average_memory_wanted: ", naive_total_memory_alloc / a_counter)

    print("total: ", a_counter + f_counter)
    allocator.print_stats()
