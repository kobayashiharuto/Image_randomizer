from PIL import Image
from tools.move import move_image
from tools.noise import noise_image
from tools.stretch import stretch_image
from tools.binary_converter import binary_convert


def main():
    image = Image.open('data/9_0.png')
    image_binary = binary_convert(
        image,
        resize=28,
        threshold=128
    )

    for i in range(10):
        image_randomized = noise_image(image_binary)
        image_stretched = stretch_image(image_randomized, 0.7, 0.9)
        image_moved = move_image(image_stretched, 3, 3)
        image_moved.save(f'out/{i}.png')


if __name__ == '__main__':
    main()
