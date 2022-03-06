import subprocess
import pyautogui
import time
import webbrowser


def log_in():
    # opens the chrome
    subprocess.call(
        ["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"])
    time.sleep(2)

    # log in to the page

    webbrowser.open(
        'https://www.dpssiliguri.org/School/Student/StudentLogin.aspx')
    time.sleep(2)

    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')

    # locate online class button
    time.sleep(5)
    pyautogui.moveTo(1175, 964)
    time.sleep(1)
    pyautogui.click()

    # click the link
    time.sleep(2)
    pyautogui.moveTo(1232, 253)
    pyautogui.click()
    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.moveTo(1063, 270)
    pyautogui.click()


log_in()


def position():
    print("hi")
    time.sleep(5)
    p = (pyautogui.position())
    print(p)

# position()
