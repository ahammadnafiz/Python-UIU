"""
Module: whiteboard

Description: This module contains the code for a simple whiteboard application.

Functions:

WhiteboardApp(root) - Creates a new instance of the WhiteboardApp class.
create_ui() - Creates the user interface for the whiteboard application.
start_drawing(event) - Starts drawing when the user clicks the mouse.
draw(event) - Draws a line when the user moves the mouse.
stop_drawing(event) - Stops drawing when the user releases the mouse button.
change_pen_color() - Opens a color selection dialog to allow the user to choose a new pen color.
change_line_width(value) - Changes the line width of the pen.
clear_canvas() - Clears the canvas.
toggle_eraser(event=None) - Toggles between pen and eraser mode.
toggle_pen(event=None) - Toggles between pen and eraser mode.

Classes:

WhiteboardApp - A class that represents the whiteboard application.

"""

import customtkinter as ctk
from tkinter.colorchooser import askcolor


class WhiteboardApp:
    """
    Class: WhiteboardApp

    Description: This class represents a simple whiteboard application.

    Functions:

    __init__(self, root) - Initializes a new instance of the WhiteboardApp class.
    create_ui() - Creates the user interface for the whiteboard application.
    start_drawing(event) - Starts drawing when the user clicks the mouse.
    draw(event) - Draws a line when the user moves the mouse.
    stop_drawing(event) - Stops drawing when the user releases the mouse button.
    change_pen_color() - Opens a color selection dialog to allow the user to choose a new pen color.
    change_line_width(value) - Changes the line width of the pen.
    clear_canvas() - Clears the canvas.
    toggle_eraser(event=None) - Toggles between pen and eraser mode.
    toggle_pen(event=None) - Toggles between pen and eraser mode.

    """

    def __init__(self, root):
        """
        Function: __init__

        Description: Initializes a new instance of the WhiteboardApp class.

        Parameters:

        root (tkinter.Tk) - The root window for the whiteboard application.

        """
        self.root = root
        self.root.title("Whiteboard App")
        self.root.geometry("1200x800")

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("green")

        self.canvas = ctk.CTkCanvas(root, bg="white", bd=0, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)
        self.is_drawing = False
        self.eraser_mode = False
        self.drawing_color = "black"
        self.line_width = 2
        self.prev_x = None
        self.prev_y = None
        self.create_ui()

    def create_ui(self):
        """
        Function: create_ui

        Description: Creates the user interface for the whiteboard application.

        """
        controls_frame = ctk.CTkFrame(self.root)
        controls_frame.pack(side="top", fill="x", padx=20, pady=10)

        self.color_button = ctk.CTkButton(controls_frame, text="Change Color", command=self.change_pen_color, width=120, height=40, font=("Arial", 12), corner_radius=8)
        self.clear_button = ctk.CTkButton(controls_frame, text="Clear Canvas", command=self.clear_canvas, width=120, height=40, font=("Arial", 12), corner_radius=8)
        self.pen_button = ctk.CTkButton(controls_frame, text="Pen (P)", command=self.toggle_pen, width=120, height=40, font=("Arial", 12), corner_radius=8)
        self.eraser_button = ctk.CTkButton(controls_frame, text="Eraser (E)", command=self.toggle_eraser, width=120, height=40, font=("Arial", 12), corner_radius=8)

        self.color_button.grid(row=0, column=0, padx=10, pady=10)
        self.clear_button.grid(row=0, column=1, padx=10, pady=10)
        self.pen_button.grid(row=0, column=2, padx=10, pady=10)
        self.eraser_button.grid(row=0, column=3, padx=10, pady=10)

        line_width_label = ctk.CTkLabel(controls_frame, text="Line Width:", font=("Arial", 12))
        line_width_label.grid(row=0, column=4, padx=10, pady=10)

        self.line_width_slider = ctk.CTkSlider(controls_frame, from_=1, to=10, command=self.change_line_width, progress_color="#FF6347")
        self.line_width_slider.set(self.line_width)
        self.line_width_slider.grid(row=0, column=5, padx=10, pady=10)

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)
        self.root.bind("e", self.toggle_eraser)
        self.root.bind("E", self.toggle_eraser)
        self.root.bind("p", self.toggle_pen)
        self.root.bind("P", self.toggle_pen)

    def start_drawing(self, event):
        """
        Function: start_drawing

        Description: Starts drawing when the user clicks the mouse.

        Parameters:

        event (tkinter.Event) - The event that triggered the drawing.

        """
        self.is_drawing = True
        self.prev_x, self.prev_y = event.x, event.y

    def draw(self, event):
        """
        Function: draw

        Description: Draws a line when the user moves the mouse.

        Parameters:

        event (tkinter.Event) - The event that triggered the drawing.

        """
        if self.is_drawing:
            current_x, current_y = event.x, event.y
            if self.eraser_mode:
                self.canvas.create_line(self.prev_x, self.prev_y, current_x, current_y, fill="white", width=self.line_width, capstyle=ctk.ROUND, smooth=True)
            else:
                self.canvas.create_line(self.prev_x, self.prev_y, current_x, current_y, fill=self.drawing_color, width=self.line_width, capstyle=ctk.ROUND, smooth=True)
            self.prev_x, self.prev_y = current_x, current_y

    def stop_drawing(self, event):
        """
        Function: stop_drawing

        Description: Stops drawing when the user releases the mouse button.

        Parameters:

        event (tkinter.Event) - The event that triggered the drawing.

        """
        self.is_drawing = False

    def change_pen_color(self):
        """
        Function: change_pen_color

        Description: Opens a color selection dialog to allow the user to choose a new pen color.

        """
        color = askcolor()[1]
        if color:
            self.drawing_color = color

    def change_line_width(self, value):
        """
        Function: change_line_width

        Description: Changes the line width of the pen.

        Parameters:

        value (int) - The new line width.

        """
        self.line_width = int(value)

    def clear_canvas(self):
        """
        Function: clear_canvas

        Description: Clears the canvas.

        """
        self.canvas.delete("all")

    def toggle_eraser(self, event=None):
        """
        Function: 
        toggle_eraser
        
        Description: Toggles between pen and eraser mode.

        Parameters:
        ----------
        event (tkinter.Event, optional) - The event that triggered the toggling. Defaults to None.

        """
        self.eraser_mode = not self.eraser_mode
        
    def toggle_pen(self, event=None):
        """
    Toggle between pen and eraser mode.

    Parameters
    ----------
    event : Event, optional
        The event that triggered the function call.
        This parameter is only used to determine the key that was pressed.
        By default, this parameter is set to None.

    Returns
    -------
    None

    """
        self.eraser_mode = not self.eraser_mode


if __name__ == "__main__":
    """
    Main function of the program. Creates the main window and starts the main loop.
    """
    root = ctk.CTk()
    app = WhiteboardApp(root)
    root.geometry("1000x700")
    root.mainloop()
