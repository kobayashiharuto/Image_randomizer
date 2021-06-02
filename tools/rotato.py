from PIL import Image
import numpy as np


def rotate_image(image, rotate):
    size, _ = image.size
    center_move_array = np.array(
        [[1, 0, -size * 0.5], [0, 1, -size * 0.5], [0, 0, 1]])
    rotate_array = np.array(
        [[np.cos(rotate), -np.sin(rotate), 0], [np.sin(rotate), np.cos(rotate), 0], [0, 0, 1]])
    center_return_array = np.array(
        [[1, 0, size * 0.5], [0, 1, size * 0.5], [0, 0, 1]])
    affin_array = np.matmul(
        center_return_array,
        np.matmul(rotate_array, center_move_array))
    affine_data = tuple(np.linalg.inv(affin_array).flatten())
    image_stretched = image.transform(
        image.size, Image.AFFINE, affine_data, fill=1, fillcolor=255)
    return image_stretched


def main():
    image = Image.open('data/9_0.png')
    image_rotate = rotate_image(image, -np.pi/18)
    image_rotate.save('out/rotate.png')


if __name__ == '__main__':
    main()
