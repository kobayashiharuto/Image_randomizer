from PIL import Image
from tools.move import move_image
from tools.noise import noise_image
from tools.stretch import stretch_image
from tools.binary_converter import binary_convert
import random


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


def randomized_image_generate(image, resize, count):
    image_binary = binary_convert(
        image,
        resize=resize,
        threshold=128
    )

    images = []
    for _ in range(count):
        size_y, size_x, move_y, move_x = random200()
        image_randomized = noise_image(image_binary)
        image_stretched = stretch_image(image_randomized, size_y, size_x)
        image_moved = move_image(image_stretched, move_y, move_x)
        images.append(image_moved)
    return images
