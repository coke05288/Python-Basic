# Section12-3
# 파이썬 데이터 베이스 연동
# SQLite

# 테이블 수정 및 삭제

import sqlite3

# DB 생성(파일)
conn = sqlite3.connect('D:/dev/python_basic/basic/resource/database.db')

# Cursor 연결
c = conn.cursor()

# 데이터 수정 1
# c.execute('UPDATE users SET username =? WHERE id = ?', ('niceman', 2))

# 데이터 수정 2
# c.execute('UPDATE users SET username =:name WHERE id =:id', {"name" : "goodman", "id" : 5})

# 데이터 수정 3
# c.execute('UPDATE users SET username ="%s" WHERE id ="%s"' % ("badboy", '1'))

# 중간데이터 확인
for user in c.execute("SELECT *from users"):
    print(user)

# Row Delete 1
# c.execute('DELETE from users WHERE id = ?', (2,))

# Row Delete 2
# c.execute('DELETE from users WHERE id = :id', {"id" : 5})

# Row Delete 3
# c.execute('DELETE from users WHERE id = "%s"'%("3"))

# 중간데이터 확인
for user in c.execute("SELECT *from users"):
    print(user)

# 테이블 전체 데이터 삭제
print("user db deleted : ", conn.execute('DELETE from users').rowcount, "rows")

# 커밋
conn.commit()

# 접속 해제
conn.close()
