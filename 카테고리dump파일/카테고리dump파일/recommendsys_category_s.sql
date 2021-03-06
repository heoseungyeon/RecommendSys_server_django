-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: recommendsys
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `category_s`
--

DROP TABLE IF EXISTS `category_s`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category_s` (
  `ctgr_sid` int NOT NULL AUTO_INCREMENT,
  `ctgr_name` varchar(45) NOT NULL,
  `large_id` int DEFAULT NULL,
  `middle_id` int DEFAULT NULL,
  PRIMARY KEY (`ctgr_sid`),
  UNIQUE KEY `name_middle` (`ctgr_name`,`middle_id`),
  KEY `middle_id_idx` (`middle_id`),
  KEY `large_id_s_idx` (`large_id`),
  CONSTRAINT `large_id_s` FOREIGN KEY (`large_id`) REFERENCES `category_m` (`large_id`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `middle_id_s` FOREIGN KEY (`middle_id`) REFERENCES `category_m` (`ctgr_mid`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=268 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category_s`
--

LOCK TABLES `category_s` WRITE;
/*!40000 ALTER TABLE `category_s` DISABLE KEYS */;
INSERT INTO `category_s` VALUES (1,'떡볶이',1,1),(2,'라볶이',1,1),(3,'쫄볶이',1,1),(4,'순대',1,1),(5,'어묵',1,1),(6,'냉면',1,1),(7,'비빔밥',1,1),(8,'칼국수',1,1),(9,'잔치국수',1,1),(10,'비빔국수',1,1),(11,'콩국수',1,1),(12,'수제비',1,1),(13,'쫄면',1,1),(14,'김밥',1,1),(15,'주먹밥',1,1),(16,'핫도그',1,1),(17,'김치볶음밥',1,1),(18,'육회',1,2),(19,'닭발',1,2),(20,'고등어구이',1,2),(21,'아구찜',1,2),(22,'해물찜',1,2),(23,'갈비',1,2),(24,'떡국',1,2),(25,'만두국,만둣국',1,2),(26,'추어탕',1,2),(27,'파전',1,2),(28,'김치전',1,2),(29,'대창',1,2),(30,'막창',1,2),(31,'곱창',1,2),(32,'주꾸미,쭈꾸미',1,2),(33,'찜닭',1,2),(34,'불고기',1,2),(35,'닭갈비',1,2),(36,'갈비찜',1,2),(37,'삼겹살',1,2),(38,'오겹살',1,2),(39,'제육',1,2),(40,'오징어볶음',1,2),(41,'낙지볶음',1,2),(42,'오리구이',1,2),(43,'닭볶음탕',1,2),(44,'갈비탕',1,2),(45,'돼지국밥',1,2),(46,'소고기국밥',1,2),(47,'육개장',1,2),(48,'감자탕',1,2),(49,'순대국밥',1,2),(50,'뼈해장국',1,2),(51,'곰탕',1,2),(52,'설렁탕',1,2),(53,'부대찌개',1,2),(54,'김치찌개',1,2),(55,'된장찌개',1,2),(56,'청국장찌개',1,2),(57,'삼계탕',1,2),(58,'순두부찌개',1,2),(59,'빈대떡',1,2),(60,'죽',1,2),(61,'돈까스,돈카츠',1,3),(62,'새우까스,새우카츠',1,3),(63,'생선까스',1,3),(64,'히레까스,히레카츠',1,3),(65,'로스까스,로스카츠',1,3),(66,'호르몬동',1,3),(67,'규동',1,3),(68,'사케동',1,3),(69,'가츠동',1,3),(70,'카레',1,3),(71,'소바',1,3),(72,'메밀',1,3),(73,'우동',1,3),(74,'라멘',1,3),(75,'나베,스키야키',1,3),(76,'초밥',1,3),(77,'회,우럭,광어,참치',1,3),(78,'타코야키,타코야끼',1,3),(79,'오코노미야키,오코노미야끼',1,3),(80,'샤브샤브',1,3),(81,'양장피',1,4),(82,'팔보채',1,4),(83,'유산슬',1,4),(84,'동파육',1,4),(85,'라조육',1,4),(86,'라조기',1,4),(87,'깐풍기',1,4),(88,'잡탕',1,4),(89,'해파리냉채',1,4),(90,'꿔바로우',1,4),(91,'칠리새우',1,4),(92,'탕수육',1,4),(93,'짜장면,자장면',1,4),(94,'짬뽕',1,4),(95,'울면',1,4),(96,'볶음밥',1,4),(97,'마라탕',1,4),(98,'마라샹궈',1,4),(99,'고추잡채',1,4),(100,'누룽지탕',1,4),(101,'양꼬치',1,4),(102,'치킨',1,5),(103,'피자',1,5),(104,'햄버거',1,5),(105,'파스타',1,5),(106,'까르보나라',1,5),(107,'리조또',1,5),(108,'스테이크',1,5),(109,'퀘사디아',1,5),(110,'브리또',1,5),(111,'필라프',1,5),(112,'월남쌈',1,6),(113,'쌀국수',1,6),(114,'팟타이',1,6),(115,'딤섬',1,6),(116,'공원',2,7),(117,'사찰',2,7),(118,'유적지',2,7),(119,'체험',2,7),(120,'박물관',2,8),(121,'미술관',2,8),(122,'도서관',2,8),(123,'영화관',2,8),(124,'공연장',2,8),(125,'연극',2,9),(126,'뮤지컬',2,9),(127,'오페라',2,9),(128,'전시회',2,9),(129,'캠핑장',2,10),(130,'스케이트장',2,10),(131,'당구장',2,10),(132,'볼링장',2,10),(133,'PC방',2,11),(134,'노래방',2,11),(135,'카페',2,11),(136,'술집',2,11),(137,'라볶이',1,12),(138,'쫄볶이',1,12),(139,'어묵',1,13),(140,'냉면',1,12),(141,'비빔밥',1,14),(142,'칼국수',1,12),(143,'잔치국수',1,12),(144,'비빔국수',1,12),(145,'콩국수',1,12),(146,'쫄면',1,12),(147,'김밥',1,14),(148,'주먹밥',1,14),(149,'핫도그',1,15),(150,'김치볶음밥',1,14),(151,'육회',1,16),(152,'닭발',1,16),(153,'고등어구이',1,17),(154,'아구찜',1,17),(155,'해물찜',1,18),(156,'갈비',1,16),(157,'떡국',1,20),(158,'만두국,만둣국',1,20),(159,'추어탕',1,20),(160,'파전',1,22),(161,'김치전',1,22),(162,'대창',1,16),(163,'막창',1,16),(164,'곱창',1,16),(165,'주꾸미,쭈꾸미',1,18),(166,'찜닭',1,16),(167,'불고기',1,16),(168,'닭갈비',1,16),(169,'갈비찜',1,16),(170,'삼겹살',1,16),(171,'오겹살',1,16),(172,'제육',1,16),(173,'오징어볶음',1,18),(174,'낙지볶음',1,18),(175,'오리구이',1,16),(176,'닭볶음탕',1,16),(177,'갈비탕',1,20),(178,'돼지국밥',1,20),(179,'소고기국밥',1,20),(180,'육개장',1,20),(181,'감자탕',1,20),(182,'순대국밥',1,20),(183,'뼈해장국',1,20),(184,'곰탕',1,20),(185,'설렁탕',1,20),(186,'부대찌개',1,23),(187,'김치찌개',1,23),(188,'된장찌개',1,23),(189,'청국장찌개',1,23),(190,'삼계탕',1,20),(191,'순두부찌개',1,23),(192,'빈대떡',1,22),(193,'죽',1,14),(194,'돈까스,돈카츠',1,24),(195,'새우까스,새우카츠',1,24),(196,'생선까스',1,24),(197,'히레까스,히레카츠',1,24),(198,'로스까스,로스카츠',1,24),(199,'호르몬동',1,25),(200,'규동',1,25),(201,'사케동',1,25),(202,'가츠동',1,25),(203,'카레',1,25),(204,'소바',1,12),(205,'메밀',1,12),(206,'우동',1,12),(207,'라멘',1,12),(208,'나베,스키야키',1,16),(209,'초밥',1,14),(210,'회,우럭,광어,참치',1,13),(211,'타코야키,타코야끼',1,19),(212,'오코노미야키,오코노미야끼',1,22),(213,'샤브샤브',1,16),(214,'양장피',1,18),(215,'팔보채',1,18),(216,'유산슬',1,18),(217,'동파육',1,16),(218,'라조육',1,16),(219,'라조기',1,16),(220,'깐풍기',1,16),(221,'잡탕',1,18),(222,'해파리냉채',1,18),(223,'꿔바로우',1,16),(224,'칠리새우',1,16),(225,'탕수육',1,16),(226,'짜장면,자장면',1,12),(227,'짬뽕',1,12),(228,'울면',1,12),(229,'볶음밥',1,14),(230,'마라탕',1,12),(231,'마라샹궈',1,12),(232,'고추잡채',1,16),(233,'누룽지탕',1,18),(234,'양꼬치',1,16),(235,'치킨',1,16),(236,'피자',1,15),(237,'햄버거',1,15),(238,'파스타',1,12),(239,'까르보나라',1,12),(240,'리조또',1,14),(241,'스테이크',1,16),(242,'퀘사디아',1,15),(243,'브리또',1,15),(244,'필라프',1,14),(245,'쌀국수',1,12),(246,'팟타이',1,12),(247,'딤섬',1,26),(248,'해물찜',1,19),(249,'추어탕',1,21),(250,'주꾸미,쭈꾸미',1,19),(251,'오징어볶음',1,19),(252,'낙지볶음',1,19),(253,'갈비탕',1,21),(254,'돼지국밥',1,21),(255,'소고기국밥',1,21),(256,'육개장',1,21),(257,'감자탕',1,21),(258,'순대국밥',1,21),(259,'뼈해장국',1,21),(260,'곰탕',1,21),(261,'설렁탕',1,21),(262,'양장피',1,19),(263,'팔보채',1,19),(264,'유산슬',1,19),(265,'잡탕',1,19),(266,'해파리냉채',1,19),(267,'누룽지탕',1,19);
/*!40000 ALTER TABLE `category_s` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-16 17:26:09
