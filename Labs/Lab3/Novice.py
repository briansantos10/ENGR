from microbit import *

def full_image(brightness):
    # Image() expects input to be in the form of "row1:row2:row3:row4:row5"
    # Num represents brightness
    row = str(brightness) * 5
    arr = [row] * 5

    # Creates a string with : between each new row
    image_str = ":".join(arr)
    return Image(image_str)

while True:
    for _ in range(2):
        display.show(full_image(9))
        sleep(250)
        display.clear()
        sleep(250)

    sleep(500)

    # Fade in 
    for lvl in range(10):
        display.show(full_image(lvl))
        sleep(75)

    # Fade out from brightness 9 to 0
    for lvl in range(9, -1, -1):
        display.show(full_image(lvl))
        sleep(75)

    sleep(500)
