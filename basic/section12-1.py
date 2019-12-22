# Section 12-1
# 파이썬 데이터 베이스 연동
# SQLite
# 테이블 생성 및 삽입

import sqlite3
import datetime

# 삽입 날짜 생성
now = datetime.datetime.now()
print('now : ', now)

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)

# sqlite 버전
print('sqlite3.version : ', sqlite3.version)
print('sqlite3.squite_version : ', sqlite3.sqlite_version)

# DB 생성 & Auto Commit(Rollback)
conn = sqlite3.connect('D:/Dev/python_basic/basic/resource/database.db',
                       isolation_level=None)

# Cursor
c = conn.cursor()
print("Cursor Type : ", type(c))

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute(
    "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text \
, phone text, website text, regdate text)")

# 데이터 삽입
c.execute("INSERT INTO users VALUES(1, 'Kim Young Jun', 'coke05288@naver.com',\
    '010-4903-9783', 'www.naver.com', ?)", (nowDatetime,))

c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)",\
 (2, 'Park', 'co@daum.net', '010000', 'p.com', nowDatetime))

# Many 삽입(튜플, 리스트 삽입)

userList = ((3, "Lee", "Lee@naver.com", "01000002", "w.com", nowDatetime),
            (4, "Cho", "Cho@naver.com", "01200002", "Chohcho.com", nowDatetime),
            (5, "Choi", "Choi@naver.com", "012520002", "weuh.com", nowDatetime))

c.executemany(
    "INSERT INTO users(id, username, email, phone, website, regdate) \
    VALUES (?,?,?,?,?,?)", userList)

# 데이터 테이블 삭제

# conn.execute("DELETE FROM users")
# print("users db deleted : ", conn.execute("DELETE FROM users").rowcount)

# 커밋 : isolation_level =None 일 경우 자동 커밋
# conn.commit()
# 롤백
# conn.rollback()

# 접속해제
conn.close()

