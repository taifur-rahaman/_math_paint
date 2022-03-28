<h1 align="center">Math Paint</h1>


An app that lets the user provide the start coordinates of geometrical shapes such as squares and rectangles, their
dimensions, and their colors, and the program produces an image file canvas with the geometrical shapes drawn in it.

<h3> Objects </h3>

    Nouns:
        1. App - App object doens't make sense
        2. Square - Object 1
        3. Rectangle - Object 2
        4. Dimensions - Attributes of Object 1, 2 & 3
        5. Coordinates - X & Y axis Attributes for Object 1 & 2
        6. Canvas - Object 3
        7. Colors - Attributes of Object 1, 2 & 3
        8. Draw - Canvas method for object 1 & 2

Object Design

    Square: 
        X  # X = x-axis
        Y  # Y = y-axis
        sides # Dimension of the Square
        color
        draw(canvas)

    Rectangle:
        X  # X = x-axis
        Y  # Y = y-axis
        width
        height
        color
        draw(canvas)

    Canvas:
        width
        height
        color
        