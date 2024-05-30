from arena.arenaManager import ArenaManager
from freeSpace.freeSpaceManager import FreeSpaceManager

from memory_visualizer import MemoryVisualizer


def my_print():
    fm = FreeSpaceManager(4096)
    memory_visualizer = MemoryVisualizer()
    am = ArenaManager()
    id_size_list = [
        (0, 100),
        (1, 73),
        (2, 48),
        (3, 100),
        (4, 42),
        (5, 55),
        (6, 40),
        (7, 58),
        (8, 42),
        (9, 55),
        (10, 40),
        (11, 58),
        (12, 42),
    ]
    for id, size in id_size_list:
        block = fm.allocate(id, size)
        memory_visualizer.visualize(fm.to_list() + am.to_list())
        if block is not None:
            am.insert(block)
            memory_visualizer.visualize(fm.to_list() + am.to_list())

    fm.insert(am.free(0))
    memory_visualizer.visualize(fm.to_list() + am.to_list())

    memory_visualizer.make_gif()


if __name__ == "__main__":
    my_print()
