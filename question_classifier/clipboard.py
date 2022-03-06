import win32clipboard
import time

# clean clipboard data file

open('clip_history_data.txt', 'w').close()

print('Clipboard Started . . .')

old = ""

# loop for saving ctrl + c data

while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    if old != data:
        new = ''
        for i in data:
            if i != '\n':
                new += i
        with open('clip_history_data.txt', 'a+', encoding='utf8') as f:
            f.write('>>>'+new)
        old = data

    time.sleep(0.5)
