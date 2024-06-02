from memory_visualizer import MemoryVisualizer


def binary_search(target, data):
    start = 0  # 맨 처음 위치
    end = len(data) - 1  # 맨 마지막 위치

    while start <= end:
        mid = (start + end) // 2  # 중간값

        if data[mid].id == target:
            return mid  # target 위치 반환

        elif data[mid].id > target:  # target이 작으면 왼쪽을 더 탐색
            end = mid - 1
        else:  # target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return



class FreeBlock:
    def __init__(self, size):
        self.id = -1
        self.start = 0
        self.end = size
        self.size = size


class UsedBlock:
    def __init__(self, id, start, end, size):
        self.id = id
        self.start = start
        self.end = end
        self.size = size


class Allocator:
    def __init__(self):
        self.chunk_size = 4096 * 4
        self.freeBlock = FreeBlock(self.chunk_size)
        self.usedBlockList = []
        self.chunk_load_count = 0

    def print_stats(self):
        in_use = 0
        for i in self.usedBlockList:
            in_use += i.size
        free_space = self.freeBlock.size
        print("In use:", in_use, "Free space:", free_space)
        print("Chunk load count:", self.chunk_load_count)

    def malloc(self, id, size):
        if size > self.freeBlock.size:
            # print("Too big")
            self.freeBlock.size += self.chunk_size
            self.freeBlock.end += self.chunk_size
            self.chunk_load_count += 1
            self.malloc(id, size)
            return

        # split
        used_block = UsedBlock(id, self.freeBlock.start + 1, self.freeBlock.start + size, size)
        self.usedBlockList.append(used_block)

        self.freeBlock.size -= size
        self.freeBlock.start += size

    def free(self, id):
        idx = binary_search(id, self.usedBlockList)
        if idx is None:
            print("No such block")
            return

        for i in range(idx, len(self.usedBlockList)):
            self.usedBlockList[i].start -= self.usedBlockList[idx].size
            self.usedBlockList[i].end -= self.usedBlockList[idx].size

        self.freeBlock.size += self.usedBlockList[idx].size
        self.freeBlock.start -= self.usedBlockList[idx].size
        self.usedBlockList.pop(idx)


if __name__ == "__main__":
    allocator = Allocator()
    memory_visualizer = MemoryVisualizer()

    import time

    start_time = time.time()

    with open("./input.txt", "r") as file:
        n = 0
        for line in file:
            print("epoch ", n)
            req = line.split()
            if req[0] == 'a':
                allocator.malloc(int(req[1]), int(req[2]))
            elif req[0] == 'f':
                allocator.free(int(req[1]))
            n += 1

    end_time = time.time()

    execution_time = end_time - start_time
    print("프로그램 실행 시간:", execution_time, "초")
    allocator.print_stats()
