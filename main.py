# Imports
from classes import Canvas, Rectangle, Square


# Color function
def color():
    rgb = ["red", "green", "blue"]
    colors = []
    for i in rgb:
        if i == "red":
            color_red = int(input("Enter the range of Red (0-255): "))
            colors.append(color_red)
        elif i == "green":
            color_green = int(input("Enter the range of Green (0-255): "))
            colors.append(color_green)
        elif i == "blue":
            color_blue = int(input("Enter the range of Blue (0-255): "))
            colors.append(color_blue)
    return colors


# Canvas
# Height of the Canvas with validation check
while True:
    try:
        height_canvas = int(input("Enter the height of the Canvas: "))
        break
    except ValueError:
        print("Invalid Input")

# Width of the Canvas with validation check
while True:
    try:
        width_canvas = int(input("Enter the width of the Canvas: "))
        break
    except ValueError:
        print("Invalid Input")

# Color of the Canvas
color_canvas = color()

canvas = Canvas(height_canvas, width_canvas, color_canvas)

# Rectangle
# Starting Row position of the Rectangle
while True:
    try:
        row_rect = int(input("Enter the starting Row position of the Rectangle: "))
        break
    except ValueError:
        print("Invalid Input")

# Starting Col position of the Rectangle
while True:
    try:
        col_rect = int(input("Enter the starting Column position of the Rectangle: "))
        break
    except ValueError:
        print("Invalid Input")

# Height of the Rectangle
while True:
    try:
        height_rect = int(input("Enter the height of the Rectangle: "))
        break
    except ValueError:
        print("Invalid Input")

# Width of the Rectangle
while True:
    try:
        width_rect = int(input("Enter the width of the Rectangle: "))
        break
    except ValueError:
        print("Invalid Input")

# Color of the Rectangle
color_rectangle = color()

rectangle = Rectangle(row_rect, col_rect, height_rect, width_rect, color_rectangle)
rectangle.draw(canvas)

# Square
# Starting Row position of the Square
while True:
    try:
        row_square = int(input("Enter the starting Row position of the Square: "))
        break
    except ValueError:
        print("Invalid Input")

# Starting Col position of the Square
while True:
    try:
        col_square = int(input("Enter the starting Column position of the Square: "))
        break
    except ValueError:
        print("Invalid Input")

# Sides of the Square
while True:
    try:
        side_square = int(input("Enter the sides of the Square: "))
        break
    except ValueError:
        print("Invalid Input")

# Color of the Rectangle
color_square = color()

square = Square(row_square, color_square, side_square, color_square)
square.draw(canvas)
# Canvas Print
canvas.make("resources/img/canvas.png")
