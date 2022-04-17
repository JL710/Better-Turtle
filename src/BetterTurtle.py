import tkinter
import tkinter.ttk as ttk
import turtle
import threading


class BetterTurtle(tkinter.Tk):
    def __init__(self, title: str="BetterTurtle", geometry: str="500x500"):
        super().__init__()
        self.title(title)
        self.geometry(geometry)

        self.columnconfigure(7, weight=1)
        self.rowconfigure(1, weight=1)

        # create widgets
        self.turtle_canvas = tkinter.Canvas(self)
        self.larger_button = ttk.Button(self, width=2, text="+", command=lambda: self.turtle_canvas.scale("all", 0, 0, 1.1, 1.1))
        self.smaller_button = ttk.Button(self, width=2, text="-", command=lambda: self.turtle_canvas.scale("all", 0, 0, 0.9, 0.9))
        self.left_button = ttk.Button(self, width=2, text="←", command=lambda: self.turtle_canvas.move("all", -10, 0)) #←↑→↓
        self.up_button = ttk.Button(self, width=2, text="↑", command=lambda: self.turtle_canvas.move("all", 0, -10))
        self.right_button = ttk.Button(self, width=2, text="→", command=lambda: self.turtle_canvas.move("all", 10, 0))
        self.down_button = ttk.Button(self, width=2, text="↓", command=lambda: self.turtle_canvas.move("all", 0, 10))
        self.spacing_label = ttk.Label(self, text="")

        # grid widgets
        self.larger_button.grid(column=0, row=0)
        self.smaller_button.grid(column=1, row=0)
        self.left_button.grid(column=2, row=0)
        self.up_button.grid(column=3, row=0)
        self.right_button.grid(column=4, row=0)
        self.down_button.grid(column=5, row=0)
        self.spacing_label.grid(column=6, row=0)
        self.turtle_canvas.grid(column=0, row=1, columnspan=8, sticky="nsew")

        self.turtle = turtle.RawTurtle(self.turtle_canvas)

        thread = threading.Thread(target=lambda: self.mainloop)
        thread.start()

    def get_turtle(self):
        return self.turtle

    def not_exit(self):
        self.turtle.getscreen().update()
        self.mainloop()

    def tracer(self, number: int, *args):
        self.turtle._tracer(number)
