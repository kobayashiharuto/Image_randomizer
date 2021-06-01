from PIL import Image
import noise
import stretch
import binary_converter


def main():
    image = Image.open('data/9_0.png')
    image_binary = binary_converter.binary_convert(
        image,
        resize=28,
        threshold=128
    )

    for i in range(10):
        image_randomized = noise.noise_image(image_binary)
        image_stretched = stretch.stretch(image_randomized, 0.7, 0.9)
        image_stretched.save(f'out/{i}.png')


if __name__ == '__main__':
    main()
