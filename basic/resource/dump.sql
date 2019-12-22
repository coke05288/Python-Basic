BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text , phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Kim Young Jun','coke05288@naver.com','010-4903-9783','www.naver.com','2019-12-23 01:44:36');
INSERT INTO "users" VALUES(2,'Park','co@daum.net','010000','p.com','2019-12-23 01:44:36');
INSERT INTO "users" VALUES(3,'Lee','Lee@naver.com','01000002','w.com','2019-12-23 01:44:36');
INSERT INTO "users" VALUES(4,'Cho','Cho@naver.com','01200002','Chohcho.com','2019-12-23 01:44:36');
INSERT INTO "users" VALUES(5,'Choi','Choi@naver.com','012520002','weuh.com','2019-12-23 01:44:36');
COMMIT;
