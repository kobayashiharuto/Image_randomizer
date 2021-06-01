from PIL import Image
import numpy as np


def move(image, y_position, x_position):
    position_array = np.array(
        [[1, 0, y_position], [0, 1, x_position], [0, 0, 1]])
    affine_data = tuple(np.linalg.inv(position_array).flatten())
    image_moved = image.transform(
        image.size, Image.AFFINE, affine_data, fill=1, fillcolor=255)
    return image_moved


def main():
    image = Image.open('data/binary.png')
    image_moved = move(image, 2, 2)
    image_moved.save('out/transform.png')


if __name__ == '__main__':
    main()
