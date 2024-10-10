from math_painting.canvas import Canvas
from math_painting.shapes import Square, Rectangle
from pathlib import Path


base_dir = Path(__file__).resolve().parent

# Get canvas width and height from the user
canvas_width = int(input("Enter the canvas width: "))
canvas_height = int(input("Enter the canvas height: "))

# Make a dictionary of color codes and prompt for color
colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter canvas color (white or black): ")

# create canvas with the user data
canvas = Canvas(height=canvas_height, width=canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw? Enter quit to quit. ")

    if shape_type.casefold() == "rectangle":
        rec_x = int(input(f"Enter x of the {shape_type}: "))
        rec_y = int(input(f"Enter y of the {shape_type}: "))
        rec_width = int(input(f"Enter width of the {shape_type}: "))
        rec_height = int(input(f"Enter height of the {shape_type}: "))
        red = int(input(f"How much red should the {shape_type} have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red, green, blue))
        r1.draw(canvas)

    # Ask for square data and create a square if the choice is "square"
    if shape_type.casefold() == "square":
        sq_x = int(input(f"Enter x of the {shape_type}: "))
        sq_y = int(input(f"Enter y of the {shape_type}: "))
        sq_side = int(input(f"Enter side of the {shape_type}: "))
        red = int(input(f"How much red should the {shape_type} have? "))
        green = int(input("How much green? "))
        blue = int(input("How much blue? "))

        # Create the square
        s1 = Square(x=sq_x, y=sq_y, side=sq_side, color=(red, green, blue))
        s1.draw(canvas)

    if shape_type == "quit":
        break

canvas.make(str(base_dir.joinpath("canvas.png")))

