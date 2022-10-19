-- 【要求二】
CREATE DATABASE website;
USE website;
CREATE TABLE member (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    follower_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME DEFAULT CURRENT_TIMESTAMP
);
SHOW COLUMNS FROM member;
ALTER TABLE member MODIFY COLUMN id BIGINT AUTO_INCREMENT COMMENT '獨立編號';
ALTER TABLE member MODIFY COLUMN name VARCHAR(255) NOT NULL COMMENT '姓名';
ALTER TABLE member MODIFY COLUMN username VARCHAR(255) NOT NULL COMMENT '帳戶名稱';
ALTER TABLE member MODIFY COLUMN password VARCHAR(255) NOT NULL COMMENT '帳戶密碼';
ALTER TABLE member MODIFY COLUMN follower_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '追蹤者數量';
ALTER TABLE member MODIFY COLUMN time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '註冊時間';
SHOW FULL COLUMNS FROM member;

-- 【要求三】
INSERT INTO member(name, username, password) VALUES('tester', 'test', 'test');
INSERT INTO member(name, username, password, follower_count) VALUES('安妮亞', 'AnyaDontLike', 'LikePeanut', 999);
INSERT INTO member(name, username, password, follower_count) VALUES('乙骨優太', 'TrueLove', 'RikaOrimoto', 10);
INSERT INTO member(name, username, password, follower_count) VALUES('Steven Jobs', 'StayHungry', 'APPLE', 53);
INSERT INTO member(name, username, password, follower_count) VALUES('Paul Buchheit', 'DontBeEvil', 'Gmail', 1);
INSERT INTO member(name, username, password, follower_count) VALUES('菜英文', 'PresidentTsai', 'Tjuku', 57);
SELECT * FROM member;
SELECT * FROM member ORDER BY time DESC;
SELECT * FROM member ORDER BY time DESC LIMIT 1,3;
SELECT * FROM member WHERE username='test';
SELECT * FROM member WHERE username='test' AND password='test';
SET sql_safe_updates=0;
UPDATE member SET name='test2' WHERE username='test';
SELECT * FROM member WHERE username='test';

-- 【要求四】
SELECT COUNT(id), SUM(follower_count), AVG(follower_count) FROM member;

-- 【要求五】
CREATE TABLE message(
	id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '獨立編號',
    member_id BIGINT NOT NULL COMMENT '留言者會員編號',
    content VARCHAR(255) NOT NULL COMMENT '留言內容',
    like_count INT UNSIGNED NOT NULL DEFAULT 0 COMMENT '按讚的數量',
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '留言時間',
    FOREIGN KEY (member_id) REFERENCES member(id)
);
SHOW FULL COLUMNS FROM message;
INSERT INTO message(member_id, content, like_count) VALUES (1, '嗨，大家好~', 6);
INSERT INTO message(member_id, content, like_count) VALUES (2, '安妮亞跟tester說好~~~', 1);
INSERT INTO message(member_id, content, like_count) VALUES (3, '呃...嗨', 0);
INSERT INTO message(member_id, content, like_count) VALUES (4, 'Hello.', 0);
INSERT INTO message(member_id, content, like_count) VALUES (1, '欸Steven, 聽說iPhone 14 pro系列災情嚴重欸', 6);
UPDATE message SET like_count=0 WHERE id=5;
INSERT INTO message(member_id, content, like_count) VALUES (2, '安妮亞也不喜歡', 1);
INSERT INTO message(member_id, content, like_count) VALUES (4, 'Please contact with apple store service near your location.', 2);
INSERT INTO message(member_id, content, like_count) VALUES (1, '那我到底要不要跳槽到ios啊...', 3);
INSERT INTO message(member_id, content, like_count) VALUES (5, '請繼續支持好棒棒的Pixel(ˊ<_ˋ)', 5);
SELECT * FROM message;
SELECT message.id, message.member_id, member.name, member.username, message.content, message.like_count, message.time
	FROM message INNER JOIN member ON message.member_id=member.id;
SELECT message.id, message.member_id, member.name, member.username, message.content, message.like_count 
	FROM message INNER JOIN member ON message.member_id=member.id 
	WHERE member.username='test';
SELECT message.member_id, member.name, member.username, COUNT(like_count), SUM(like_count), AVG(like_count) 
	FROM message INNER JOIN member ON message.member_id=member.id 
	WHERE member.username='test';
DROP TABLE message;