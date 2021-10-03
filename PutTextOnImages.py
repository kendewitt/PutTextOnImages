from PIL import Image, ImageDraw, ImageFont
import os
import pyperclip
import re

input_file = re.sub(',', '\n', pyperclip.paste()).splitlines()

english_title = re.sub('<br>|</center>|[!@#$]', '', input_file[0])
japanese_title = re.sub('<sup>|</sup>|[!@#$]', '', input_file[1])
if len(japanese_title) > 26:
    japanese_title_list = japanese_title.split(" / ")
    japanese_title = japanese_title_list[0]
    japanese_title2 = japanese_title_list[1]

source_img = Image.open("<path to image file>.png", 'r').convert("RGBA")
english_font_size = 75
english_font = ImageFont.truetype("/Library/Fonts/Avenir LT 95 Black.ttf", english_font_size)
japanese_font = ImageFont.truetype("/Library/Fonts/ヒラギノ丸ゴ Pro W4.otf", 25)

draw = ImageDraw.Draw(source_img)
W, H = source_img.size
w, h = draw.textsize(english_title, font=english_font)

if w>W:
    english_font_size=int(input("We need to decrease the English font size. What size?"))
    english_font = ImageFont.truetype("/Library/Fonts/Avenir LT 95 Black.ttf", english_font_size)
    w, h = draw.textsize(english_title, font=english_font)

wjp, hjp = draw.textsize(japanese_title, font=japanese_font)
english_horizontal_text_position = ((W-w)/2)
eng_vertical_text_position = ((h))
japanese_horizontal_text_position = ((W-wjp)/2)
japanese_vertical_text_position = eng_vertical_text_position+125
draw.text((english_horizontal_text_position, eng_vertical_text_position), english_title, font=english_font, fill="black")
draw.text((japanese_horizontal_text_position, japanese_vertical_text_position), japanese_title, font=japanese_font, fill="black")
if 'japanese_title2' in globals():
    wjp2, hjp2 = draw.textsize(japanese_title2, font=japanese_font)
    draw.text((((W-wjp2)/2), (H-h)/3+150), japanese_title2, font=japanese_font, fill=(255,255,255,255))

image_name = english_title+", "+(re.sub('/', '', japanese_title))

source_img.save("<path to output image directory>/%s.png" % image_name, "PNG")
