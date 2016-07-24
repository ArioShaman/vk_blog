# -*- coding: utf-8 -*-
import ImageFont
import Image
import ImageDraw
text = "Руский текст"
font = ImageFont.truetype("Fonts/journalism.ttf", 95)
image = Image.open('Images/frog.jpg','r')
draw = ImageDraw.Draw(image)
draw.text((400,500), text.encode('utf-8'),font=font, fill=(255,243,243))
image.save("Images/format.png")