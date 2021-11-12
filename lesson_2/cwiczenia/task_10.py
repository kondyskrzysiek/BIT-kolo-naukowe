from PIL import Image


def load_image(filename):
    image = Image.open(filename)
    width, height = image.size
    pixels = list(image.getdata())
    image = [pixels[i:i + width] for i in range(0, len(pixels), width)]
    return image


def save_image(filename, image):
    flat_image = [item for sublist in image for item in sublist]
    height, width = len(image), len(image[0])
    image_out = Image.new("L", (width, height))
    image_out.putdata(flat_image)
    image_out.save(filename)


def color_to_grey(image, average=False):
    height, width = len(image), len(image[0])

    new_image = []
    for i in range(height):
        new_row = [0 for _ in range(width)]
        for j in range(width):
            r, g, b = image[i][j]
            if average:
                new_row[j] = (r + g + b) // 3
            else:
                new_row[j] = int(0.3 * r + 0.59 * g + 0.11 * b)
        new_image.append(new_row)

    return new_image


if __name__ == "__main__":
    in_file = "wiewiorka.jpg"  # fill in your image file name
    out_file = "wie_grey.jpg"  # fill in file name of grayscale image
    image = load_image(in_file)
    image = color_to_grey(image)
    save_image(out_file, image)
