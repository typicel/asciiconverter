from PIL import Image, ImageDraw, GifImagePlugin
from numpy import interp
import os
import keyboard
import time
import sys

def resize(image, nsize):
    new_image = image.copy()
    width, height = new_image.size
    aspect_ratio = height/width #Calculate aspect ratio to evently resize image

    size = (nsize, nsize*aspect_ratio)
    new_image.thumbnail(size)
    return new_image

def parseGifFrames(input_gif):
    new_gif = input_gif.copy()
    for frame in range(0, input_gif.n_frames):
        time.sleep(0.01)
        os.system("cls")

        input_gif.seek(frame)
        new_gif = resize(input_gif, 50)
        convertImageToASCII(new_gif)


def convertImageToASCII(image):
    density = " .:-=+*#%@"
    width, height = image.size
    px = image.load()

    image = image.convert('RGB')

    for i in range(height):
        for j in range(width):
            # Calcualtes average of all three RGB values
            r, g, b = image.getpixel((j,i))
            avg = (r+g+b)/3
            idx = interp(avg, [0, 255], [9,0]) #maps the range 0-255 to 9-0 (for density string)
            print(2*density[int(idx)], end="")
        print("")


def main():
    print("1. Still Image\n2. GIF")
    formatInput = int(input("Enter choice for image format > "))

    if(formatInput == 1):
        os.system("cls")
        imagefile = input("Enter image name > ")

        old_image = Image.open(imagefile)
        new_image = resize(old_image, 64)

        os.system("cls")
        convertImageToASCII(new_image)

    if(formatInput == 2):
        keyboard.on_press_key("q", quit)
        os.system("cls")
        imagefile = input("Enter gif name > ")

        os.system("cls")
        input("Press Enter to start gif, press Ctrl+C to stop loop")

        imageObject = Image.open(imagefile)
        try:
            while True:
                parseGifFrames(imageObject)
        except KeyboardInterrupt:
            os.system("cls")
            print("Exiting...")
            pass


main()
