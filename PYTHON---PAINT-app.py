import tkinter as tk

def on_click(event):
    global prev_x, prev_y
    prev_x, prev_y = event.x, event.y

def on_drag(event):
    global prev_x, prev_y
    canvas.create_line(prev_x, prev_y, event.x, event.y, fill=color, width=brush_size)
    prev_x, prev_y = event.x, event.y

def change_color(new_color):
    global color
    color = new_color

def change_brush_size(new_size):
    global brush_size
    brush_size = new_size

# Initialize variables
color = 'black'
brush_size = 2

# Create main window
root = tk.Tk()
root.title("Paint App")

# Create canvas to draw
canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack()

# Bind events for drawing
canvas.bind('<Button-1>', on_click)
canvas.bind('<B1-Motion>', on_drag)

# Create color options
colors_frame = tk.Frame(root)
colors_frame.pack(pady=10)

tk.Label(colors_frame, text="Colors: ").pack(side=tk.LEFT)

colors = ['black', 'red', 'green', 'blue', 'yellow', 'orange', 'purple']
for c in colors:
    color_button = tk.Button(colors_frame, bg=c, width=2, command=lambda col=c: change_color(col))
    color_button.pack(side=tk.LEFT, padx=2)

# Create brush size options
sizes_frame = tk.Frame(root)
sizes_frame.pack(pady=5)

tk.Label(sizes_frame, text="Brush size: ").pack(side=tk.LEFT)

sizes = [1, 2, 3, 4, 5]
for s in sizes:
    size_button = tk.Button(sizes_frame, text=str(s), width=2, command=lambda size=s: change_brush_size(size))
    size_button.pack(side=tk.LEFT, padx=2)

# Run the application
root.mainloop()
