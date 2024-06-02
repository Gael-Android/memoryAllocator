#include <iostream>
#include <vector>
#include <list>
#include <set>
#include <chrono> // for timing
#include <sstream>
#include <fstream>

using namespace std;
using namespace std::chrono;

struct FreeBlock {
    FreeBlock(size_t size) : id(-1), start(0), end(size), size(size) {}

    int id;
    size_t start;
    size_t end;
    size_t size;
};

struct UsedBlock {
    UsedBlock(int id, size_t start, size_t end, size_t size)
            : id(id), start(start), end(end), size(size) {}

    int id;
    size_t start;
    size_t end;
    size_t size;
};


struct UsedBlockComparator {
    bool operator()(const UsedBlock &a, const UsedBlock &b) const {
        return a.id < b.id;
    }
};

class Allocator {
public:
    Allocator() : chunk_size(4096 * 4), chunk_load_count(0) {
        freeBlocks.push_back(FreeBlock(chunk_size));
    }

    void print_stats() {
        size_t in_use = 0;
        for (const auto &block: usedBlocks) {
            in_use += block.size;
        }
        size_t free_space = freeBlocks.front().size;
        cout << "In use: " << in_use << " Free space: " << free_space << endl;
        cout << "Chunk load count: " << chunk_load_count << endl;
    }

    void malloc(int id, size_t size) {
        if (size > freeBlocks.front().size) {
            freeBlocks.front().size += chunk_size;
            freeBlocks.front().end += chunk_size;
            chunk_load_count++;
            malloc(id, size); // Recursive call after expanding
            return;
        }

        UsedBlock used_block(id, freeBlocks.front().start + 1, freeBlocks.front().start + size, size);
        usedBlocks.insert(used_block);

        freeBlocks.front().size -= size;
        freeBlocks.front().start += size;
    }

    void free(int id) {
        auto it = usedBlocks.find(UsedBlock(id, 0, 0, 0)); // Search for the block
        if (it == usedBlocks.end()) {
            cout << "No such block" << endl;
            return;
        }

        // Add to the free list (implementation omitted for brevity)
        freeBlocks.push_back(FreeBlock(it->size));
        usedBlocks.erase(it);
    }

private:
    size_t chunk_size;
    list<FreeBlock> freeBlocks;
    set<UsedBlock, UsedBlockComparator> usedBlocks;
    int chunk_load_count;
};

int main() {
    Allocator allocator;

    auto start_time = high_resolution_clock::now();

    ifstream inputFile("./input.txt"); // Open the input file
    if (!inputFile.is_open()) {
        cerr << "Error opening input file." << endl;
        return 1;
    }

    int epoch = 0;
    string line;
    while (getline(inputFile, line)) { // Read each line from the file
        stringstream ss(line); // Use stringstream to parse the line
        char action;
        int id;
        size_t size;
        ss >> action >> id >> size;

        if (action == 'a') {
            allocator.malloc(id, size);
        } else if (action == 'f') {
            allocator.free(id);
        }

        cout << "epoch " << epoch << endl;
        epoch++;
    }

    inputFile.close();

    auto end_time = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(end_time - start_time);

    cout << "program run time: " << duration.count() / 1e6 << " sec" << endl; // Convert to seconds
    allocator.print_stats();

    return 0;
}