import os
import random
from PIL import Image
from controller import randomized_binary_image_generate
from controller import randomized_gray_image_generate_mnist
import glob
import numpy as np
import PIL.ImageOps as imgops


def get_file_paths(path: str):
    files = glob.glob(path + '/*')
    return files


# 28*28サイズの時
def random28():
    size_y = random.uniform(0.5, 1.2)
    size_x = random.uniform(0.5, 1.2)
    move_y = random.randint(-5, 5)
    move_x = random.randint(-5, 5)
    rotate = random.uniform(-np.pi/9, np.pi/9)
    strength = 2
    move = 5
    return size_y, size_x, move_y, move_x, rotate, strength, move


def main():
    paths = get_file_paths(
        r'C:\Users\owner\Desktop\Image_tool\image_randomizer\target')
    file_count = 1000

    save_dir = 'out/mnist_data4'

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    for path in paths:
        image = Image.open(path)
        randmized_images = randomized_gray_image_generate_mnist(
            image, resize=28, count=file_count, random=random28, invert=True
        )

        file_name = path.split('\\')[-1].split('.')[0]
        image_category = file_name.split('_')[0]
        file_index = int(file_name.split('_')[1])

        for index, image in enumerate(randmized_images):
            image = imgops.invert(image)
            new_index = index + file_index * file_count
            image.save(f'{save_dir}/{image_category}_{new_index}.png')


if __name__ == '__main__':
    main()
