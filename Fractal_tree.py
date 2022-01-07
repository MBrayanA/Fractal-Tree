import tkinter as tk
import math

class FractalTree:
    def __init__(self):
        """ Initialize the fractal object. """

        self.SIZE = 400
        # Create window 
        self.window = tk.Tk()
        self.window.title("Fractal Tree")
        self.canvas = tk.Canvas(self.window, width = self.SIZE, height = self.SIZE, 
                        borderwidth = 1, relief = 'solid')
        self.canvas.grid(row = 1, column = 1)
        #Frame:
        self.control_frame = tk.Frame(self.window, width = self.SIZE, height = 50)
        self.control_frame.grid(row = 2, column = 1)
        self.control_frame.grid_propagate(False)
        #Buttons:
        self.advance_button = tk.Button(self.control_frame, text="Advance", command = self.advance)
        self.advance_button.grid(row=1, column=1)
        self.reset_button = tk.Button(self.control_frame, text="Reset", command = self.reset)
        self.reset_button.grid(row=1, column=2)
        self.quit_button = tk.Button(self.control_frame, text="Quit", command = self.quit)
        self.quit_button.grid(row=1, column=3)
        
        self.control_frame.grid_rowconfigure(1, weight = 1)
        self.control_frame.grid_columnconfigure(1, weight = 1)
        self.control_frame.grid_columnconfigure(2, weight = 1)
        self.control_frame.grid_columnconfigure(3, weight = 1)

        #Defines and initiates and sets levels of recursion, angle factor, and size factor as instance variables
        self.current_levels_of_recursion = 0
        self.angleFactor = math.pi/5 
        self.sizeFactor = 0.58
        #Calls on draw_tree function to intially create middle branch when program opens  
        self.draw_tree(self.SIZE//2, self.SIZE, self.SIZE//3, math.pi/2,  self.current_levels_of_recursion)
        tk.mainloop()

    def advance(self):
        """ Everytime 'Advance' function/button is called on it increments one level of recursion """
        self.current_levels_of_recursion += 1
        self.draw_tree(self.SIZE//2, self.SIZE, self.SIZE//3, math.pi/2,  self.current_levels_of_recursion)

    def reset(self):
        """ Resets program to 0 levels of recursion """
        #deletes every branch, resets to single middle branch/stem, and calls draw_tree function
        self.canvas.delete("all") 
        self.current_levels_of_recursion = 0 
        self.draw_tree(self.SIZE//2, self.SIZE, self.SIZE//3, math.pi/2,  self.current_levels_of_recursion)

    def quit(self):
        """ Quit the program """
        self.window.destroy()

    def draw_tree(self, x1, y1, size, angle, levels_of_recursion):
        """ Draw fractal with levels_of_recursion in square whose upper level corner is
            (upper_left_x, upper_left_y), whose size is size and whose height is size. 
        """
        x2 = x1 + int(math.cos(angle) * size) #Defines x2 using x1, angle, and size
        y2 = y1 - int(math.sin(angle) * size) #Defines y2 using y1, angle, and size
        
        #If statement is the base case 
        if levels_of_recursion == 0:    
            self.canvas.create_line(x1,y1, x2, y2, tags = 'line')

        #Else statement is the recursive case   
        else: 
            #Calls on draw_tree function to draw the left branche
            self.draw_tree(x2, y2, size * self.sizeFactor, angle + self.angleFactor, levels_of_recursion - 1)
            #Calls on draw_tree function to draw the right branche
            self.draw_tree(x2, y2, size * self.sizeFactor, angle - self.angleFactor, levels_of_recursion - 1)

if __name__ == "__main__":
    FractalTree()