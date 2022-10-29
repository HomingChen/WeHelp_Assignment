-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: website
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '獨立編號',
  `name` varchar(255) NOT NULL COMMENT '姓名',
  `username` varchar(255) NOT NULL COMMENT '帳戶名稱',
  `password` varchar(255) NOT NULL COMMENT '帳戶密碼',
  `follower_count` int unsigned NOT NULL DEFAULT '0' COMMENT '追蹤者數量',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '註冊時間',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'test2','test','test',0,'2022-10-18 22:53:43'),(2,'安妮亞','AnyaDontLike','LikePeanut',999,'2022-10-18 22:56:25'),(3,'乙骨優太','TrueLove','RikaOrimoto',10,'2022-10-18 23:25:58'),(4,'Steven Jobs','StayHungry','APPLE',53,'2022-10-18 23:32:03'),(5,'Paul Buchheit','DontBeEvil','Gmail',1,'2022-10-18 23:32:06'),(6,'菜英文','PresidentTsai','Tjuku',57,'2022-10-18 23:32:07'),(7,'test no.2','test2','1234',0,'2022-10-25 23:46:24'),(8,'test newcomer','test3','1234',0,'2022-10-29 10:44:23'),(9,'test signup','test4','1234',0,'2022-10-29 11:17:49'),(10,'test signup','test5','1234',0,'2022-10-29 11:25:54'),(11,'test signup','test6','1234',0,'2022-10-29 11:34:03'),(15,'test newcomer','test7','1234',0,'2022-10-29 13:42:01');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` bigint NOT NULL AUTO_INCREMENT COMMENT '獨立編號',
  `member_id` bigint NOT NULL COMMENT '留言者會員編號',
  `content` varchar(255) NOT NULL COMMENT '留言內容',
  `like_count` int unsigned NOT NULL DEFAULT '0' COMMENT '案讚的數量',
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '留言時間',
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,1,'嗨，大家好~',6,'2022-10-19 11:00:27'),(2,2,'安妮亞跟tester說好~~~',1,'2022-10-19 13:04:32'),(3,3,'呃...嗨',0,'2022-10-19 13:04:37'),(4,4,'Hello.',0,'2022-10-19 13:04:42'),(5,1,'欸Steven, 聽說iPhone 14 pro系列災情嚴重欸',0,'2022-10-19 13:04:43'),(6,2,'安妮亞也不喜歡',1,'2022-10-19 13:04:46'),(7,4,'Please contact with apple store service near your location.',2,'2022-10-19 13:04:48'),(8,1,'那我到底要不要跳槽到ios啊...',3,'2022-10-19 13:04:50'),(9,5,'請繼續支持好棒棒的Pixel(ˊ<_ˋ)',5,'2022-10-19 13:04:51'),(10,7,'Hi Hi',0,'2022-10-26 03:02:58'),(11,7,'是這裡嗎?',0,'2022-10-26 03:06:37'),(12,1,'原來按讚的功能很困難...',0,'2022-10-29 06:20:30'),(13,1,'再試一次看看',0,'2022-10-29 06:40:38'),(14,1,'QQQ',0,'2022-10-29 06:43:01'),(15,1,'再試試看~~~',0,'2022-10-29 07:02:06'),(16,7,'來聊天吧',0,'2022-10-29 10:39:08'),(19,8,'最後測試',0,'2022-10-29 13:40:59'),(20,15,'成功啦~~~',0,'2022-10-29 13:42:37'),(21,15,'<b>測試一<br>下漏洞<b>用tag語法輸入會不會有問題呢?',0,'2022-10-29 13:43:25'),(22,15,'<a ref=\"/\">link</a>',0,'2022-10-29 13:44:08'),(23,15,'<a href=\"/\">link</a>',0,'2022-10-29 13:44:44'),(24,1,'哇，樓上連結表示安全性失敗了',0,'2022-10-29 13:45:32'),(25,1,'按鈕也失敗了QQ',0,'2022-10-29 13:45:53');
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-29 13:55:57
