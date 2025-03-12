from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
    draw.stroke_width = 2
    draw.stroke_color = Color('black')
    draw.fill_color = Color('white')
    points = [(25, 25), (75, 50), (25, 75)]
    draw.polygon(points)
    with Image(width=100, height=100, background=Color('lightblue')) as image:
        draw(image)

#Save the image
    with Image(width=100,
               height=100,
               background=Color('yellow')) as image:
        draw(image)
        image.format = 'pdf'                   
        image.save(filename='play.pdf')