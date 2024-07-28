import tkinter as tk
from tkinter import colorchooser, filedialog
from PIL import Image, ImageDraw, ImageTk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Drawing App")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(self.root, bg='white', cursor='cross')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.image = Image.new("RGB", (800, 600), 'white')
        self.draw = ImageDraw.Draw(self.image)

        self.color = 'black'
        self.brush_size = 5

        self.setup_ui()

        self.canvas.bind("<B1-Motion>", self.paint)

    def setup_ui(self):
        top_frame = tk.Frame(self.root, bg='grey')
        top_frame.pack(side=tk.TOP, fill=tk.X)

        color_button = tk.Button(top_frame, text="Color", command=self.choose_color)
        color_button.pack(side=tk.LEFT, padx=10)

        save_button = tk.Button(top_frame, text="Save", command=self.save_image)
        save_button.pack(side=tk.LEFT, padx=10)

        clear_button = tk.Button(top_frame, text="Clear", command=self.clear_canvas)
        clear_button.pack(side=tk.LEFT, padx=10)

        size_scale = tk.Scale(top_frame, from_=1, to=10, orient=tk.HORIZONTAL, label='Brush Size')
        size_scale.set(self.brush_size)
        size_scale.pack(side=tk.LEFT, padx=10)
        size_scale.bind("<Motion>", self.change_brush_size)

    def choose_color(self):
        self.color = colorchooser.askcolor(color=self.color)[1]

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"),
                                                            ("All files", "*.*")])
        if file_path:
            self.image.save(file_path)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (800, 600), 'white')
        self.draw = ImageDraw.Draw(self.image)

    def change_brush_size(self, event):
        self.brush_size = event.widget.get()

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)
        self.draw.ellipse([x1, y1, x2, y2], fill=self.color, outline=self.color)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
