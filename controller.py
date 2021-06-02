from tools.move import move_image
from tools.noise import noise_image
from tools.stretch import stretch_image
from tools.binary_converter import binary_convert


def randomized_image_generate(image, resize, count, random):
    image_binary = binary_convert(
        image,
        resize=resize,
        threshold=128
    )

    images = []
    for _ in range(count):
        size_y, size_x, move_y, move_x = random()
        image_randomized = noise_image(image_binary)
        image_stretched = stretch_image(image_randomized, size_y, size_x)
        image_moved = move_image(image_stretched, move_y, move_x)
        images.append(image_moved)
    return images
