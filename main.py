import random
from PIL import Image
from controller import randomized_binary_image_generate
from controller import randomized_gray_image_generate
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
    rotate = random.uniform(-np.pi/36, np.pi/36)
    strength = 1
    move = 2
    return size_y, size_x, move_y, move_x, rotate, strength, move


# 200*200サイズの時
def random200():
    size_y = random.uniform(0.5, 1.1)
    size_x = random.uniform(0.5, 1.1)
    move_y = random.randint(-20, 20)
    move_x = random.randint(-20, 20)
    rotate = random.uniform(-np.pi/36, np.pi/36)
    strength = 5
    move = 30
    return size_y, size_x, move_y, move_x, rotate, strength, move


# 100*100サイズの時
def random100():
    size_y = random.uniform(0.6, 1.1)
    size_x = random.uniform(0.6, 1.1)
    move_y = random.randint(-10, 10)
    move_x = random.randint(-10, 10)
    rotate = random.uniform(-np.pi/36, np.pi/36)
    strength = 6
    move = 7
    return size_y, size_x, move_y, move_x, rotate, strength, move


def image_randomize(multi, alpha):
    paths = get_file_paths('data/icons')
    file_count = 500

    for path in paths:
        image = Image.open(path)
        if alpha:
            image = image.convert('RGBA')
            new_image = Image.new('RGBA', image.size, 'WHITE')
            new_image.paste(image, (0, 0), image)
            new_image = new_image.convert('RGB')
            image = new_image
        randmized_images = randomized_gray_image_generate(
            image, resize=50, count=file_count, random=random100
        )

        file_name = path.split('\\')[-1].split('.')[0]
        image_category = file_name.split('_')[0]

        for index, image in enumerate(randmized_images):
            if multi:
                index = index + int(file_name.split('_')[1]) * file_count
            image.save(f'out/train_datav6/{image_category}_{index}.png')


if __name__ == '__main__':
    image_randomize(multi=False, alpha=True)
