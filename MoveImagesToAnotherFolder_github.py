import os
import random
import shutil

def randomize_and_move_images(source_dir, destination_dir, num_images=100):
    """
    Randomly select a specified number of images from the source directory
    and move them to the destination directory.

    Parameters:
    source_dir (str): Path to the source directory containing images.
    destination_dir (str): Path to the destination directory.
    num_images (int): Number of images to move. Default is 100.
    """
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Get a list of all files in the source directory
    all_files = os.listdir(source_dir)

    # Filter the list to include only image files (e.g., .jpg, .png)
    image_files = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

    # Check if there are enough images in the source directory
    if len(image_files) < num_images:
        raise ValueError(f"Not enough images in the source directory. Found {len(image_files)}, but need {num_images}.")

    # Randomly select the specified number of images
    selected_images = random.sample(image_files, num_images)

    # Move the selected images to the destination directory
    for image in selected_images:
        shutil.move(os.path.join(source_dir, image), os.path.join(destination_dir, image))

    print(f"Moved {len(selected_images)} images to {destination_dir}")

if __name__ == "__main__":
    # Define the source and destination directories
    source_dir = r'path/to/source/folder'
    destination_dir = r'path/to/destination/folder'

    # Call the function to randomize and move images
    randomize_and_move_images(source_dir, destination_dir)
