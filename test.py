import pydirectinput

# pydirectinput.moveTo(100, 150) # Move the mouse to the x, y coordinates 100, 150.
# pydirectinput.click() # Click the mouse at its current location.
# pydirectinput.click(2560, 1080) # Click the mouse at the x, y coordinates 200, 220.
# pydirectinput.move(None, 10)  # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
# pydirectinput.doubleClick() # Double click the mouse at the
# pydirectinput.press('esc') # Simulate pressing the Escape key.
# pydirectinput.keyDown('shift')
# pydirectinput.keyUp('shift')

print("Press Ctrl-C to quit.")
try:
    while True:
        
        x, y = pydirectinput.position()
        positionStr = "X: " + str(x).rjust(4) + " Y: " + str(y).rjust(4)
        print(positionStr, end="")
        print("\b" * len(positionStr), end="", flush=True)
except KeyboardInterrupt:
    print("\n")

#  w a s d lc pc alt
# [0,0,0,0,0, 0, 0] <- keyboard oh
# [x,y]          <- mouse position
