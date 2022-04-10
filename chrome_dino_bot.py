import pyautogui as pygui

pixel_is_grey = lambda x_cor: pygui.pixelMatchesColor(x_cor, 438, expectedRGBColor=(83, 83, 83))


while True:
    if pixel_is_grey(490) or pixel_is_grey(480):
        pygui.press("up")

        # if it's a small spike, just press the down key
        if not (
            pixel_is_grey(500)
        ):
            pygui.keyUp("down")
