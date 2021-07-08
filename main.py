from cairosvg import svg2png
import os
import glob
from PIL import Image


def add_margin(pil_img, top, right, bottom, left, color):
    width, height = pil_img.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(pil_img.mode, (new_width, new_height), color)
    result.paste(pil_img, (left, top))
    return result


files = glob.glob(
    'C:/Users/owner/Desktop/DATA_for_ML/fontawesome-pro-5.15.3-desktop/svgs/light' + '/*')

for filename in files:
    with open(filename, 'r') as f:
        filename_without_ext = os.path.splitext(os.path.basename(filename))[0]
        image_path = f'images/{filename_without_ext}.png'
        svg2png(bytestring=f.read(),
                write_to=image_path, output_height=500, output_width=500)
        image = Image.open(image_path).convert('RGBA')
        image_new = Image.new('RGBA', image.size, 'WHITE')
        image_new.paste(image, (0, 0), image)
        image_new = image_new.convert('RGB')
        image_new = add_margin(image_new, 50, 50, 50, 50, (255, 255, 255))
        image_new.save(image_path, quality=95)
