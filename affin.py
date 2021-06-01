from PIL import Image
import numpy as np


np.set_printoptions(threshold=1000000)


def stretch(image):
    origin_size, _ = image.size
    y_size = 0.9
    x_size = 0.9
    y_position = origin_size * (1.0 - y_size)
    x_position = origin_size * (1.0 - y_size)
    stretch_array = np.array([[y_size, 0, 0], [0, x_size, 0], [0, 0, 1]])
    position_array = np.array(
        [[1, 0, y_position], [0, 1, x_position], [0, 0, 1]])
    affin_array = np.matmul(stretch_array, position_array)
    affine_data = tuple(np.linalg.inv(affin_array).flatten())
    image_stretched = image.transform(
        image.size, Image.AFFINE, affine_data, fill=1, fillcolor=255)
    return image_stretched


def main():
    image = Image.open('data/binary.png')
    image_stretched = stretch(image)
    image_stretched.save('out/transform.png')


if __name__ == '__main__':
    main()
