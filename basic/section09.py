# 파일 읽기,쓰기
# 읽기 모드 = r, 쓰기모드(기존 파일 삭제) = w, 추가모드(파일 생성 및 추가) = a
# .. : 상대 경로, . : 절대 경로

# 파일 읽기
# 예제1

f = open('./basic/resource/review.txt','r')

content = f.read()
 
print(content)

f.close()

print('------------------------')
print('------------------------')

# 예제2
with open('./basic/resource/review.txt','r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))

print('------------------------')
print('------------------------')

# 예제3
with open('./basic/resource/review.txt','r') as f:
    for c in f:
        print(c.strip())

print('------------------------')
print('------------------------')

# 예제4
with open('./basic/resource/review.txt','r') as f:
    content = f.read()
    print(">", content)
    content = f.read()
    print(">", content) # 커서가 파일 맨끝으로 갔기 때문에 빈내용 출력

print('------------------------')
print('------------------------')

# 예제5 : 한문장씩 전처리를 할때
with open('./basic/resource/review.txt','r') as f:
    line = f.readline()
    # print(line)
    while line:
        print(line,end=' ')
        line = f.readline()

print('------------------------')
print('------------------------')

# 예제6
with open('./basic/resource/review.txt','r') as f:
    contents = f.readlines()
    print(contents)
    for c in contents:
        print(c, end = '***')

print('------------------------')
print('------------------------')

# 예제7
score =[]
with open('./basic/resource/score.txt', 'r') as f:
    for line in f:
        score.append(int(line))
    print(score)

print('Average : {:6.3}'.format(sum(score)/len(score)))


# 파일쓰기

# 예제 1
with open('./basic/resource/text1.txt', 'w') as f:
    f.write("niceman!\n")

# 예제 2
with open('./basic/resource/text1.txt', 'a') as f:
    f.write("goodman!\n")

# 예제 3
from random import randint

with open('./basic/resource/lotto.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50)))
        f.write('\n')

# 예제 4
# writelines : 리스트 => 파일로 저장
with open('./basic/resource/text2.txt', 'w') as f:
    list1 = ['kim\n', 'park\n']
    f.writelines(list1)

# 예제 5
with open('./basic/resource/text2.txt', 'w') as f:
    print("Test Contents1", file=f)
    print("Test Contents2", file=f)