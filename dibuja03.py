from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
    draw.stroke_color = Color('red')
    draw.stroke_width = 2
    draw.fill_color = Color('yellow')
    draw.ellipse((50, 50), # Origin (center) point
                 (40, 20)) # 80px wide, and 40px tall
    with Image(width=100, height=100, background=Color('lightblue')) as image:
        draw(image)

 #Save the image
    with Image(width=100,
               height=100,
               background=Color('green')) as image:
        draw(image)
        image.format = 'png'                   
        image.save(filename='elipse.png')