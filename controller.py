from PIL import Image
from tools.move import move_image
from tools.noise import noise_image
from tools.stretch import stretch_image
from tools.binary_converter import binary_convert


def randomized_image_generate(image):
    image_binary = binary_convert(
        image,
        resize=28,
        threshold=128
    )

    images = []
    for i in range(10):
        image_randomized = noise_image(image_binary)
        image_stretched = stretch_image(image_randomized, 0.7, 0.9)
        image_moved = move_image(image_stretched, 3, 3)
        images.append(image_moved)
    return images
