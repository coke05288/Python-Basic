# Section 13-2
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time
# 사운드 출력 가능 모음
import winsound
import sqlite3
import datetime

# DB & Auto Commit
# 본인 DB 경로

conn = sqlite3.connect('D:/dev/python_basic/basic/resource/records.db',
                       isolation_level=None)

# Cursor 연결

cursor = conn.cursor()

cursor.execute(
    'CREATE TABLE IF NOT EXISTS records(id INTEGER PRIMARY KEY AUTOINCREMENT, cor_cnt, record text, regdate text)'
)

words = []  # 단어를 담아줄 리스트

n = 1  # 게임 시도 횟수
cor_cnt = 0  # 정답 개수

with open('./basic/resource/word.txt', 'r') as f:
    for c in f:
        words.append(c.strip())

# print(words) # 단어리스트 확인

input("Ready? Press Enter Key!")

start = time.time()

while n <= 5:
    random.shuffle(words)
    q = random.choice(words)

    print()

    print("Question #{} : ".format(n), q)

    if str(q).strip() == str(input()).strip():
        print("Pass!")
        # 정답 소리 재생
        winsound.PlaySound('./basic/sound/good.wav', winsound.SND_FILENAME)
        cor_cnt += 1
    else:
        print("Wrong!")
        # 오답 소리 재생a
        winsound.PlaySound('./basic/sound/bad.wav', winsound.SND_FILENAME)

    print()

    n += 1

end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >= 3:
    print("합격!")
else:
    print("불합격!")

# 기록 DB 삽입

cursor.execute(
    "INSERT INTO records('cor_cnt', 'record', 'regdate') VALUES (?,?,?)",
    (cor_cnt, et, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

print("Game Results : ", et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작지점
if __name__ == '__main__':
    pass
