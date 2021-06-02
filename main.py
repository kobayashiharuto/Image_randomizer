import random
from PIL import Image
from controller import randomized_image_generate
import glob


def get_file_paths(path: str):
    files = glob.glob(path + '/*')
    return files


# 28*28サイズの時
def random28():
    size_y = random.uniform(0.7, 1.1)
    size_x = random.uniform(0.7, 1.1)
    move_y = random.randint(-2, 2)
    move_x = random.randint(-2, 2)
    return size_y, size_x, move_y, move_x


# 200*200サイズの時
def random200():
    size_y = random.uniform(0.7, 1.1)
    size_x = random.uniform(0.7, 1.1)
    move_y = random.randint(-20, 20)
    move_x = random.randint(-20, 20)
    return size_y, size_x, move_y, move_x


def main():
    paths = get_file_paths('data/origin_images')

    for path in paths:
        image = Image.open(path)
        randmized_images = randomized_image_generate(
            image, resize=200, count=5, random=random200()
        )

        name = path.split('\\')[-1].split('.')[0]
        for index, image in enumerate(randmized_images):
            image.save(f'out/train_data1/{name}_{index}.png')


if __name__ == '__main__':
    main()
