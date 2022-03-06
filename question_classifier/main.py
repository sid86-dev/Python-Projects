import time
from googlesearch import search
import pyshorteners
import emoji

start = time.time()

print(emoji.emojize('Server: Searching Answers :magnifying_glass_tilted_left: . . .'))

# read from clipboard data

with open('clip_history_data.txt', 'r', encoding='utf8') as f:
    read = f.read()
    f.close()

questions = (read).split('>>>')

# clean file

open('extract.txt', 'w').close()

# search answers in google

for question in questions[1::]:
    answers = []
    for j in search(question, tld="co.in", num=2, stop=2, pause=2):
        # shorten link
        s = pyshorteners.Shortener()
        link = s.tinyurl.short(j)
        # link = s
        answers.append(link)

# saves the question and answers

    with open('extract.txt', 'a', encoding='utf8') as f:
        try:
            f.write(
            (f'Question {questions.index(question)} : {question[:50]}.... \nAnswers : \nLink1: {answers[0]}\nLink2: {answers[1]}\n\n---xx---\n\n'))
        except:
             f.write(
            (f'Question {questions.index(question)} : {question}.... \nAnswers : \nLink1: {answers[0]}\nLink2: {answers[1]}\n\n---xx---\n\n'))

# saves warnings

with open('extract.txt', 'a', encoding='utf8') as f:
    f.write(emoji.emojize("\n:warning: Use this at ur own risk\n:warning: Don't share this w any1 "))
    f.close()


print(emoji.emojize('Server: file Saved as extract.txt :bookmark_tabs:'))

finish = time.time()

print(f"\nexecution completed in {round(finish-start, 2)} seconds")