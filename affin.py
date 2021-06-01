from PIL import Image
import numpy as np


np.set_printoptions(threshold=1000000)


def stretch(image):
    affin_array = np.array([[0.3, 0, 0], [0, 1, 0], [0, 0, 1]])
    affine_data = tuple(np.linalg.inv(affin_array).flatten())
    image_stretched = image.transform(image.size, Image.AFFINE, affine_data)
    return image_stretched


def main():
    image = Image.open('data/binary.png')
    image_stretched = stretch(image)
    image_stretched.save('out/transform.png')


if __name__ == '__main__':
    main()
