import keyboard
from time import sleep
import threading
import pyautogui

def main():
    counter = 0
    while pause.wait():
        path1 = 'BUTTONS/img1.jpg'
        path2 = 'BUTTONS/img2.jpg'
        button1 = pyautogui.locateOnScreen(path1, confidence=0.8, region=(1765, 900, 150, 140))
        button2 = pyautogui.locateOnScreen(path2, confidence=0.8)
        if button1:
            pyautogui.click(x=1872, y=957)
            counter += 1
            print("Counter = " + str(counter))
            input("Press Enter to continue...(Do not press pause)")
        elif button2:
            pyautogui.doubleClick(button2)
            counter += 1
            print("\nCounter = " + str(counter))
            input("Press Enter to continue...(Do not press pause)")
        sleep(1)

def off():
    print("===========\nAutoClicker\n===========")
    print ('Press "Ctrl + 1" to start')
    print ('Press "Ctrl + 2" to pause')
    while True:
        if keyboard.wait('Ctrl + 1') is None: # активация цикла на Ctrl + 1
            pause.set()
            print('\nAcl is work')
        if keyboard.wait('Ctrl + 2') is None: # остановка цикла на Ctrl + 2
            pause.clear()
            print('\nAcl is pause')

pause = threading.Event()
thread1 = threading.Thread(target=main)
thread2 = threading.Thread(target=off)

thread1.start()
thread2.start()

thread1.join()
thread2.join()