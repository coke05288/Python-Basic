# Section 13-1
# 업그레이드 타이핑 게임 제작
# 타이핑 게임 제작 및 기본 완성

import random
import time

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
        cor_cnt += 1
    else:
        print("Wrong!")

    print()

    n += 1

end = time.time()
et = end - start
et = format(et, ".3f")

if cor_cnt >= 3:
    print("합격!")
else:
    print("불합격!")

print("Game Results : ", et, "초", "정답 개수 : {}".format(cor_cnt))

# 시작지점
if __name__ == '__main__':
    pass
