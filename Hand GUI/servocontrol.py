import tkinter as tk
from gpiozero import AngularServo 

# Initialize servo motor objects 
# Although our servo motors are 90 degrees, the max_angle must be set to 360 to get the full 90 degrees of rotations
thumb_servo = AngularServo(18, min_angle=0, max_angle=360) # Dark Green M/F 
index_servo = AngularServo(23, min_angle=0, max_angle=360) # Yellow M/F 
middle_servo = AngularServo(25, min_angle=0, max_angle=360) # Purple M/F
ring_servo = AngularServo(4, min_angle=0, max_angle=360) # White M/F
pinky_servo = AngularServo(2, min_angle=0, max_angle=360) # Black M/F

# Set the root of the GUI
root = tk.Tk()

# Tkinter screen dimensions 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

text_font = "Raleway"

# Create the canvas
canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
canvas.grid(columnspan=5, rowspan=6)


# Button related code 
def createButton(root, btn_text, btn_font, colPos, rowPos, callback):
    """
    Args:
        param1: root of the tkineter GUI
        param2: text for the button 
        param3: font for the button's text 
        param4: column position of the button within the tkinter grid 
        param5: row position of the button within the tkinter grid  
    """
    text = tk.StringVar()
    btn = tk.Button(root, textvariable=text, font=btn_font, command=callback)
    text.set(btn_text)
    btn.grid(column=colPos, row=rowPos)


# Two callback functions that are executed when the buttons are clickeds
def open_btn_callback():
    thumb_slider.set(0)
    ring_slider.set(0)
    middle_slider.set(0)
    index_slider.set(0)
    pinky_slider.set(0)
    
    thumb_servo.angle(0)
    index_servo.angle(0)
    middle_servo.angle(0)
    ring_servo.angle(0)
    pinky_servo.angle(0)

def close_btn_callback():
    thumb_slider.set(360)
    ring_slider.set(360)
    middle_slider.set(360)
    index_slider.set(360)
    pinky_slider.set(360)

    thumb_servo.angle(360)
    index_servo.angle(360)
    middle_servo.angle(360)
    ring_servo.angle(360)
    pinky_servo.angle(360)

# This needs to be tested
def middleFinger_btn_callback():
    thumb_slider.set(360)
    ring_slider.set(360)
    middle_slider.set(0)
    index_slider.set(360)
    pinky_slider.set(360)
    
    thumb_servo.angle(360)
    index_servo.angle(360)
    middle_servo.angle(0)
    ring_servo.angle(360)
    pinky_servo.angle(360)
    


# Open button
open_button = createButton(root, "Open", text_font, 1, 0, open_btn_callback)

# Close button 
close_button = createButton(root, "Close", text_font, 3, 0, close_btn_callback)

# Middle Finger Button
middleFinger_button = createButton(root, "Middle Finger", text_font, 2, 1, middleFinger_btn_callback)



# Slider related Code below


# Define variables for sliders 
start_val = 0
end_val = 360
initial_val = 0 


def createSlider(root, slider_text, start, sVal, eVal, orientation, function, colPos, rowPos, col_txt, row_txt):
    """
    Args: 
        param1: root of the tkinter GUI
        param2: text for the slider 
        param3: inital value of the slider 
        param4: smallest value of the slider 
        param5: largest value of the slider 
        param6: orientation of the slider (Horizontal or Vertical)
        param7: callback or event function (used to get values of the slider)
        param8: column position of the slider 
        param9: row position of the slider 
        param10: column for the text for the slider 
        param11: row for the text for the slider 
    
    Returns: 
        the slider object that was created
    """
    slider = tk.Scale(root, from_=sVal, to=eVal, orient=orientation, command=function)
    slider.set(start)
    slider.grid(column = colPos, row=rowPos)
    slider_label = tk.Label(root, text=slider_text)
    slider_label.grid(column=col_txt, row=row_txt)
    return slider


# These are callback functions that are executed when values of sliders change
def index_val(event):
    index_servo.angle = index_slider.get()
    
def middle_val(event):
    middle_servo.angle = middle_slider.get()

def ring_val(event):
    ring_servo.angle = ring_slider.get()

def thumb_val(event):
    thumb_servo.angle = thumb_slider.get()

def pinky_val(event):
    pinky_servo.angle = pinky_slider.get()


# Thumb Slider 
thumb_slider = createSlider(root, "Thumb", initial_val, end_val, start_val, tk.VERTICAL, thumb_val, 0, 2, 0, 3)

# Index Slider 
index_slider = createSlider(root, "Index", initial_val, end_val, start_val, tk.VERTICAL, index_val, 1, 2, 1, 3)

# Middle Slider 
middle_slider = createSlider(root, "Middle", initial_val, end_val, start_val, tk.VERTICAL, middle_val, 2, 2, 2, 3)

# Ring slider 
ring_slider = createSlider(root, "Ring", initial_val, end_val, start_val, tk.VERTICAL, ring_val, 3, 2, 3, 3)

# Pinky Slider 
pinky_slider = createSlider(root, "Pinky", initial_val, end_val, start_val, tk.VERTICAL, pinky_val, 4, 2, 4, 3)

root.mainloop()
