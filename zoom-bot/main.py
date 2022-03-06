import subprocess
import pyautogui
import time
import pandas as pd
from datetime import datetime


def sign_in(meetingid, pswd):
    # opens the zoom app
    subprocess.call(["C:\\Users\\sid86\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"])

    time.sleep(5)

    # click the join button
    pyautogui.moveTo(777, 435)
    pyautogui.click()
    time.sleep(2)

    # enter meeting id
    pyautogui.write(meetingid)
    time.sleep(2)

    # click on join meeting
    pyautogui.moveTo(988, 679)
    pyautogui.click()
    # enter password
    time.sleep(2)
    pyautogui.write(pswd)

    # join meeting
    time.sleep(2)
    pyautogui.moveTo(963, 676)
    pyautogui.click()


sign_in('997 7463 3348', 'z7fM6c')
# def position():
#     print("hi")
#     time.sleep(5)
#     p = (pyautogui.position())
#     print(p)
#
#
# position()


# df = pd.read_csv('info.csv')
# while True:
#     # check the current time exists in our csv file
#     now = datetime.now().strftime("%H:%M")
#     if now in str(df['timings']):
#         row = df.loc[df['timings'] == now]
#         m_id = str(row.iloc[0, 1])
#         m_pswd = str(row.iloc[0, 2])
#
#         sign_in(m_id, m_pswd)
#         time.sleep(40)
#         print("signed in successful")
