import pyautogui
import time
import webbrowser


def delete_emails(n):
    print("Starting program..")
    emails = 0
    for i in range(n):
        time.sleep(5)
        pyautogui.moveTo(x=352, y=191)
        time.sleep(1)
        pyautogui.click()
        time.sleep(2)

        # click delete button
        # pyautogui.moveTo(x=535, y=198)
        pyautogui.moveTo(x=479, y=195)
        pyautogui.click()
        time.sleep(5)
        emails+=50
        print(f"{emails} emails deleted")

def position():
    print("hi")
    time.sleep(5)
    p = (pyautogui.position())
    print(p)

delete_emails(80)
# position()
