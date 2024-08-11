# Randomize and Move Images

This script randomly selects a specified number of images from a source directory and moves them to a destination directory.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/randomize-and-move-images.git
    ```

2. Navigate to the project directory:
    ```bash
    cd randomize-and-move-images
    ```

3. Modify the `source_dir` and `destination_dir` variables in `randomize_images.py` to point to your directories.

4. Run the script:
    ```bash
    python randomize_images.py
    ```

## Parameters

- `source_dir`: Path to the source directory containing images.
- `destination_dir`: Path to the destination directory.
- `num_images`: Number of images to move (default is 100).

## Example

```python
source_dir = r'path/to/source/folder'
destination_dir = r'path/to/destination/folder'
randomize_and_move_images(source_dir, destination_dir)
