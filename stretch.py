from PIL import Image
import numpy as np


np.set_printoptions(threshold=1000000)


def stretch(image, y_zoom, x_zoom):
    origin_size, _ = image.size
    y_position = origin_size * (1.0 - y_zoom)
    x_position = origin_size * (1.0 - x_zoom)
    stretch_array = np.array([[y_zoom, 0, 0], [0, x_zoom, 0], [0, 0, 1]])
    position_array = np.array(
        [[1, 0, y_position], [0, 1, x_position], [0, 0, 1]])
    affin_array = np.matmul(stretch_array, position_array)
    affine_data = tuple(np.linalg.inv(affin_array).flatten())
    image_stretched = image.transform(
        image.size, Image.AFFINE, affine_data, fill=1, fillcolor=255)
    return image_stretched


def main():
    image = Image.open('data/binary.png')
    image_stretched = stretch(image, 0.9, 0.9)
    image_stretched.save('out/transform.png')


if __name__ == '__main__':
    main()
