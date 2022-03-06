import PIL.Image
import os

ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']


# resize image according to new width
def resize_image(image, new_width=100):
    width, height = image.size 
    ratio = height / width
    new_height = int(new_width+ratio)
    resize_image = image.resize(new_width, new_height)
    return resize_image

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.conver("L") 
    return grayscale_image

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join(([ASCII_CHARS[pixels//25] for pixel in pixels]))
    return characters

def main(new_width=100):
    path = f'{os.getcwd()}/test.jpg'
    try:
        image = PIL.Image.open(path)
    except:
        print('Invalid Image')

    # convert image to ascii
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # format
    pixels_count = len(new_image_data)
    ascii_image = '\n'.join(new_image_data[i:(i+new_width)] for i in range(0, pixels_count, new_width))

    print(ascii_image)

    # save the ascii image
    with open('ascii_image.txt', 'w') as f:
        f.write(ascii_image)


main()