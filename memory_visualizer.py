import matplotlib.pyplot as plt
import os
import subprocess
import shutil  # For removing directories and their contents


def clear_temp_images(image_dir="./temp_images"):
    """Clears (or creates) the temporary image directory."""
    if os.path.exists(image_dir):
        shutil.rmtree(image_dir)  # Remove the entire directory
    os.makedirs(image_dir)  # Create a fresh, empty directory


def create_video_from_images(image_dir="./temp_images", output_filename="./animation/output.mp4", framerate=5):
    """Creates an MP4 video from a sequence of images using ffmpeg."""

    ffmpeg_cmd = [
        "ffmpeg",
        "-framerate", str(framerate),
        "-i", os.path.join(image_dir, "frame_%d.jpg"),  # Use os.path.join for cross-platform paths
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        output_filename
    ]

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print(f"Video created successfully: {output_filename}")
        clear_temp_images()
    except subprocess.CalledProcessError as e:
        print(f"Error creating video: {e}")


class MemoryVisualizer:

    def __init__(self):
        self.img_idx = 0
        self.fig = plt.figure(figsize=(15, 8))

    def make_mp4(self):
        create_video_from_images()

    def visualize(self, data):
        blocks = []
        for i in data:
            blocks.append([i.value.id, i.value.start_address, i.value.end_address, i.value.size])

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

        plt.savefig(f"./temp_images/frame_{self.img_idx}.jpg")  # Save each frame (plt.show() 보다 먼저 써야함)
        # plt.show()
        self.img_idx += 1
        plt.clf()
