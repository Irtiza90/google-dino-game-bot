import pyautogui as pygui

def is_pixel_grey(xcor: int):
    return pygui.pixelMatchesColor(x_cor, 438, expectedRGBColor=(83, 83, 83))

while True:
    if is_pixel_grey(490) or is_pixel_grey(480):
        pygui.press("up")

        # if it's a small spike, just press the down key
        if not (
            is_pixel_grey(500)
        ):
            pygui.keyUp("down")
