import pytest

from freeSpace.freeSpaceManager import FreeSpaceManager


def test_print() -> None:
    fm = FreeSpaceManager(4096)
    fm.allocate(3, 100)
    fm.allocate(1, 73)
    print(fm.rbtree.get_root())
    fm.allocate(2, 48)
    fm.allocate(3, 100)
    fm.allocate(4, 42)
    fm.allocate(5, 55)
    fm.allocate(6, 40)
    fm.allocate(7, 58)
    fm.allocate(8, 42)
    fm.allocate(9, 55)
    fm.allocate(10, 40)
    fm.allocate(11, 58)
    fm.allocate(12, 42)

    fm.rbtree.print_tree()
