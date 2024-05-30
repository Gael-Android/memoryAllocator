
from arena.arenaManager import ArenaManager
from freeSpace.freeSpaceManager import FreeSpaceManager


def test_print():
    fm = FreeSpaceManager(4096)
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
        if block is not None:
            am.insert(block)

    fm.rbtree.print_tree()
    am.rbtree.print_tree()

    fm.insert(am.free(0))

    print(fm.to_list())
    print(am.to_list())