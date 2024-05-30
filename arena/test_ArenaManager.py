from arena.arenaManager import ArenaManager
from block import Block


def test_print() -> None:
    am = ArenaManager()
    am.insert(Block(10, 0, 100, 100))
    am.insert(Block(1, 100, 173, 73))
    am.insert(Block(2, 173, 221, 48))
    am.insert(Block(3, 221, 321, 100))

    print()
    am.visualize()
