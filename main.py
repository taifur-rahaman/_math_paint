from classes import Canvas

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
rgb = ["red", "green", "blue"]
color_canvas = []
for i in rgb:
    if i == "red":
        color_red = int(input("Enter the range of Red (0-255): "))
        color_canvas.append(color_red)
    elif i == "green":
        color_green = int(input("Enter the range of Green (0-255): "))
        color_canvas.append(color_green)
    elif i == "blue":
        color_blue = int(input("Enter the range of Blue (0-255): "))
        color_canvas.append(color_blue)

canvas = Canvas(height_canvas, width_canvas, color_canvas)
canvas.make("resources/img/canvas.png")
