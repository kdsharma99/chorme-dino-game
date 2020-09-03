import pyautogui
from PIL import Image
import pyscreenshot as ImageGrab
import time
from numpy import asarray
# def hit(key):
#     pyautogui.keyDown(key)
#     pyautogui.keyUp(key)
def isCollide():
#     # for i in range(170, 100):
#     #     for j in range(330, 429):
#     #         if data[i, j] < 100:
#     #             hit("down")
#     #             return
#     # for i in range(170,190):
#     #     for j in range(460,510):
#     #         if data[i, j] < 100:
#     #             hit("up")
#     #             return
#     # return
    
    box=(170,430,210,500)
    image=ImageGrab.grab(box).convert("L")
    # data=image.load()
    ar=asarray(image)
    image.save("screenshot2.png")
    print(ar.sum())
    # print(ar)
    # print(ar.shape())
    return(ar.sum())
# isCollide()
if __name__ == "__main__":
    print("Starting the bot")
    time.sleep(1)
    # hit('up')
    while True:
       
        if isCollide()!=714000:
            # pyautogui.keyDown("down")
            pyautogui.keyDown("up")
            pyautogui.keyUp("up")
            # pyautogui.keyDown("up")
        else:
            # pyautogui.keyDown("up")
            # pyautogui.keyUp("up")
            pass
            # hit("up")
            

        # for i in range(170,190):
        #     for j in range(460,510):
        #         data[i,j]=0 
    
        # for i in range(170, 190):
        #     for j in range(330, 429):
        #          data[i, j] = 170
                    # hit("down")
                # return

        
        # image.show()
        
