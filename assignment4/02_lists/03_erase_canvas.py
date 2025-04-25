import tkinter as tk
import time

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser."""
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()

    # Define the eraser's bounding box
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE

    # Get all objects that the eraser is overlapping
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)

    # Change their color to white (erase effect)
    for obj in overlapping_objects:
        canvas.itemconfig(obj, fill='white')

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE

    # Create a grid of blue rectangles (cells)
    cells = []
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')
            cells.append(cell)

    # Wait for the user to click before placing the eraser
    canvas.bind("<Button-1>", lambda event: create_eraser(event, canvas))

    root.mainloop()

def create_eraser(event, canvas):
    # Create the pink eraser at the click position
    last_click_x = event.x
    last_click_y = event.y
    eraser = canvas.create_rectangle(
        last_click_x,
        last_click_y,
        last_click_x + ERASER_SIZE,
        last_click_y + ERASER_SIZE,
        fill='pink'
    )

    while True:
        erase_objects(canvas, eraser)
        time.sleep(0.05)

if __name__ == '__main__':
    main()
