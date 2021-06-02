import random
from PIL import Image
from controller import randomized_image_generate
import glob
import numpy as np


def get_file_paths(path: str):
    files = glob.glob(path + '/*')
    return files


# 28*28サイズの時
def random28():
    size_y = random.uniform(0.7, 1.1)
    size_x = random.uniform(0.7, 1.1)
    move_y = random.randint(-2, 2)
    move_x = random.randint(-2, 2)
    rotate = random.uniform(-np.pi/18, np.pi/18)
    return size_y, size_x, move_y, move_x, rotate


# 200*200サイズの時
def random200():
    size_y = random.uniform(0.7, 1.1)
    size_x = random.uniform(0.7, 1.1)
    move_y = random.randint(-20, 20)
    move_x = random.randint(-20, 20)
    rotate = random.uniform(-np.pi/18, np.pi/18)
    return size_y, size_x, move_y, move_x, rotate


def main():
    paths = get_file_paths('data/origin_images')
    file_count = 5

    for path in paths:
        image = Image.open(path)
        randmized_images = randomized_image_generate(
            image, resize=200, count=file_count, random=random200
        )

        file_name = path.split('\\')[-1].split('.')[0]
        image_category = file_name.split('_')[0]
        file_index = int(file_name.split('_')[1])

        for index, image in enumerate(randmized_images):
            new_index = index + file_index * file_count
            image.save(f'out/train_data1/{image_category}_{new_index}.png')


if __name__ == '__main__':
    main()
