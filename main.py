from voice_recognise import recogniseText

import pyautogui as pg

query = recogniseText()

if query == "next":
    print('next video!')
    # pg.typewrite('next')
    pg.scroll(10)
elif query=="like":
    print('like video')
    # pg.typewrite('like')
    pg.click(clicks=2)

