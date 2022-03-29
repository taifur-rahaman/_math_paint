# Imports
import numpy as np
from PIL import Image


class Canvas:
    """
    Object where call the shapes are going to be drawn
    """

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # dtype = np.uint8 used for arrays that represents the images, with 3 color channels having small integer values (0 to 255)
        self.data[:] = self.color

    def make(self, image_path):
        """
        Converts the current array into an Image file
        """
        img = Image.fromarray(self.data, "RGB")
        img.save(image_path)


class Rectangle:
    """
    A rectangle shape that can be drawn in the Canvas object
    """

    def __init__(self, row, col, height, width, color):
        self.row = row
        self.col = col
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        """
        Draws itself into the Canvas
        """
        canvas.data[self.row: self.row + self.height, self.col: self.col + self.width] = self.color


class Square:
    """
    A square shape that can be drawn in the Canvas object
    """

    def __init__(self, row, col, side, color):
        self.side = side
        self.row = row
        self.col = col
        self.color = color

    def draw(self, canvas):
        """
        Draws itself into the Canvas
        """
        canvas.data[self.row: self.row + self.side, self.col: self.col + self.side] = self.color
