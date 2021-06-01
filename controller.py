from PIL import Image
from tools.move import move_image
from tools.noise import noise_image
from tools.stretch import stretch_image
from tools.binary_converter import binary_convert
import random


def randomized_image_generate(image, count):
    image_binary = binary_convert(
        image,
        resize=28,
        threshold=128
    )

    images = []
    for _ in range(count):
        size_y = random.uniform(0.7, 1.1)
        size_x = random.uniform(0.7, 1.1)
        move_y = random.randint(-2, 2)
        move_x = random.randint(-2, 2)

        image_randomized = noise_image(image_binary)
        image_stretched = stretch_image(image_randomized, size_y, size_x)
        image_moved = move_image(image_stretched, move_y, move_x)
        images.append(image_moved)
    return images
