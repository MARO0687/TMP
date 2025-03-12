from wand.color import Color
from wand.image import Image
from wand.drawing import Drawing
from wand.compat import nested
from math import cos, pi, sin

with nested(Color('lightblue'),
            Color('transparent'),
            Drawing()) as (bg, fg, draw):
    draw.stroke_width = 3
    draw.fill_color = fg
    for degree in range(0, 360, 15):
        draw.push()  # Grow stack
        draw.stroke_color = Color('hsl({0}%, 100%, 50%)'.format(degree * 100 / 360))
        t = degree / 180.0 * pi
        x = 35 * cos(t) + 50
        y = 35 * sin(t) + 50
        draw.line((50, 50), (x, y))
        draw.pop()  # Restore stack
    with Image(width=100, height=100, background=Color('lightblue')) as img:
        draw(img)

#Save the image
    with Image(width=100,
               height=100,
               background=Color('yellow')) as image:
        draw(image)
        image.format = 'jpeg'                   
        image.save(filename='curvas_lineas.jpg')