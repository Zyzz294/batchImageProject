from sys import path_importer_cache
from PIL import Image,ImageDraw, ImageFont
import os
from fileinput import filename

a = b = 0
c = d = 1080

for filename in os.listdir('./Public Pictures'):
    path_to_img = './images/' + str(filename)
    img = Image.open(r'c:/This PC/Local Disk/Users/Public/Public Pictures' + str(filename)).convert("RGBA")
    img = img.crop((0, 0, 1080, 1080))
    txt = Image.new('RGBA', img.size, (255,255,255,0))

    d = ImageDraw.Draw(txt)

    x=650
    y=950

    text = "ProjectProject"
    font = ImageFont.truetype("arial.ttf", 48)

    d.text((x,y), text, fill=(255,255,255, 120), font=font)


    watermarked = Image.alpha_composite(img, txt)
    grayscale = watermarked.convert('L')

    filename = filename.split('.')
    path_to_edited_img = './edited_images/' + filename[0] + '.png'
    os.remove(path_to_edited_img)
    grayscale.save(path_to_edited_img)