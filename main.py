import time
import pyautogui
from PIL import ImageGrab

def get_pixel_color(x, y):
    screen = ImageGrab.grab(bbox=(x, y, x + 1, y + 1))
    color = screen.getpixel((0, 0))
    return color

def main():
    # Get the initial color at the cursor position
    initial_color = get_pixel_color(*pyautogui.position())
    
    while True:
        # Check if the color at the cursor position has changed
        current_color = get_pixel_color(*pyautogui.position())
        if current_color != initial_color:
            print("Screen color change detected!")
            # Add code here to stop your program or perform other actions
            break
        
        # Optional: Adjust the sleep duration based on your needs
        time.sleep(0.1)

time.sleep(1)
main()
