import matplotlib.pyplot as plt
from celluloid import Camera


class MemoryVisualizer:

    def __init__(self):
        self.fig = plt.figure(figsize=(12, 6))
        self.camera = Camera(self.fig)

    def make_gif(self):
        animation = self.camera.animate(interval=1000)
        animation.save('anime.gif', fps=5)

    def visualize(self, data):
        blocks = []
        for i in data:
            blocks.append([i.value.id, i.value.start_address, i.value.end_address, i.value.size])
        print(blocks)

        # Extract data for plotting
        ids = [block[0] for block in blocks]
        starts = [block[1] for block in blocks]
        sizes = [block[3] for block in blocks]

        # Create color list
        colors = ['gray' if id == -1 else 'skyblue' for id in ids]

        # Horizontal bars (block ranges)
        plt.barh(ids, sizes, left=starts, align='center', height=0.8, color=colors, edgecolor='black')

        # Add text labels with sizes (optional)
        for i, size in enumerate(sizes):
            plt.text(starts[i] + size / 2, ids[i], str(size),
                     ha='center', va='center', color='black')  # Adjust label color if needed

        # Customize the plot
        plt.xlabel('Position')
        plt.ylabel('Block ID')
        plt.title('Block Visualization')
        plt.grid(axis='x')

        # plt.show()
        self.camera.snap()
