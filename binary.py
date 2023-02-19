from PIL import Image
from utils import out_file, binary_file

def binary(grayscaled):
    w, h = grayscaled.size
    img = Image.new("RGB", (w, h))
    limiar = 128

    for x in range(w):
        for y in range(h):
            pxl = grayscaled.getpixel((x, y))
            if pxl[0] > limiar:
                lum = 255
            else:
                lum = 0
            img.putpixel((x, y), (lum, lum, lum))
    return img


if __name__ == "__main__":
    img = Image.open(out_file("grayscaled-image.jpg"))
    binary(img).save(binary_file("binary-image.jpg"))