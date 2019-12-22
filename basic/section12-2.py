# Section12-2
# 파이썬 데이터 베이스 연동
# SQLite

import sqlite3

# DB 파일 조회(없으면 새로 생성)
conn = sqlite3.connect(
    "D:/dev/python_basic/basic/resource/database.db")  # 본인 DB 경로

# 커서 바인딩
C = conn.cursor()

# 데이터 조회(전체)
C.execute("SELECT * FROM users")

# # 커서 위치 변경을 증명
# # 1개 로우 선택
# print("One => \n", C.fetchone())

# # 지정 로우 선택
# print("Three => \n", C.fetchmany(size=3))

# # 전체 로우 선택
# print("ALL => \n", C.fetchall())

# print("커서가 마지막(빈 리스트) => \n", C.fetchall())

print()

# 순회 1
# rows = C.fetchall()
# for row in rows:
#     print('retrieve1 > ', row)

# 순회 2 ( 이게 더 많이 쓰임 )
# for row in C.fetchall():
#     print('retrueve2 >', row)

# 순회 3
# for row in C.execute('SELECT * from users ORDER BY id desc'):
#     print('retrueve3 >', row)

print()

# WHERE Retrieve1
param1 = (3, )
C.execute('SELECT * from users WHERE id = ?', param1)
print('param1 : ', C.fetchone())
print('param1 : ', C.fetchall())

# WHERE Retrieve2
param2 = 4
C.execute('SELECT * from users WHERE id = "%s"' % param2) # %s, %f, %f
print('param2 : ', C.fetchone())
print('param2 : ', C.fetchall())

# WHERE Retrieve3
C.execute('SELECT * from users WHERE id=:Id', {"Id" : 5})
print('param3 : ', C.fetchone())
print('param3 : ', C.fetchall())

# WHERE Retrieve4
param4 = (3,5)
C.execute('SELECT * from users WHERE id IN(?,?)', param4)
print('param4 : ', C.fetchall())

# WHERE Retrieve5
C.execute('SELECT * from users WHERE id IN("%d","%d")' % (3,4))
print('param5 : ', C.fetchall())

# WHERE Retrieve6
C.execute('SELECT * from users WHERE id=:id1 OR id=:id2' ,{"id1" : 2, "id2" : 3} )
print('param6 : ', C.fetchall())

# Dump 출력 / Dump 떠야 할 데이터양이 많을 경우 분할 설계해야함 => 클러스터링
with conn:
    with open('d:/dev/python_basic/basic/resource/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete')
# f.close(), conn.close() <= with 문 개이득