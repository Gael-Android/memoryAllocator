from arena.arenaManager import ArenaManager
from freeSpace.freeSpaceManager import FreeSpaceManager
import matplotlib.pyplot as plt
from celluloid import Camera


def my_print():
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

    return fm.to_list() + am.to_list()


# def visualize(l):
#     data = l
#
#     blocks = []
#     for i in data:
#         blocks.append([i.value.id, i.value.start_address, i.value.end_address, i.value.size])
#     print(blocks)
#
#     # Extract data for plotting
#     ids = [block[0] for block in blocks]
#     starts = [block[1] for block in blocks]
#     ends = [block[2] for block in blocks]
#     sizes = [block[3] for block in blocks]
#
#     # Create color list
#     colors = ['gray' if id == -1 else 'skyblue' for id in ids]
#
#     # Create the plot
#     fig = plt.figure(figsize=(12, 6))
#     camera = Camera(fig)
#
#     # Horizontal bars (block ranges)
#     plt.barh(ids, sizes, left=starts, align='center', height=0.8, color=colors)
#
#     # Add text labels with sizes (optional)
#     for i, size in enumerate(sizes):
#         plt.text(starts[i] + size / 2, ids[i], str(size),
#                  ha='center', va='center', color='black')  # Adjust label color if needed
#
#     # Customize the plot
#     plt.xlabel('Position')
#     plt.ylabel('Block ID')
#     plt.title('Block Visualization')
#     plt.grid(axis='x')
#
#     plt.show()
#     camera.snap()
#
#     animation = camera.animate(interval=50, blit=True)
#     animation.save('my.gif')


# if __name__ == '__main__':
#     # visualize(my_print())
