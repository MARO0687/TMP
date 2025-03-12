from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

with Drawing() as draw:
    draw.stroke_width = 2
    draw.stroke_color = Color('black')
    draw.fill_color = Color('white')
    draw.path_start()
    # Start middle-left
    draw.path_move(to=(10, 50))
    # Curve across top-left to center
    draw.path_curve(to=(40, 0),
                    controls=[(10, -40), (30,-40)],
                    relative=True)
    # Continue curve across bottom-right
    draw.path_curve(to=(40, 0),
                    controls=(30, 40),
                    smooth=True,
                    relative=True)
    # Line to top-right
    draw.path_vertical_line(10)
    # Diagonal line to bottom-left
    draw.path_line(to=(10, 90))
    # Close first & last points
    draw.path_close()
    draw.path_finish()
    with Image(width=100, height=100, background=Color('lightblue')) as image:
        draw(image)

#Save the image
    with Image(width=100,
               height=100,
               background=Color('red')) as image:
        draw(image)
        image.format = 'gif'                   
        image.save(filename='paths.gif')