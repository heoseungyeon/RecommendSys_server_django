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
-- Table structure for table `category_m`
--

DROP TABLE IF EXISTS `category_m`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category_m` (
  `ctgr_mid` int NOT NULL AUTO_INCREMENT,
  `ctgr_name` varchar(45) NOT NULL,
  `large_id` int DEFAULT NULL,
  PRIMARY KEY (`ctgr_mid`),
  KEY `ctgr_lid_idx` (`large_id`),
  CONSTRAINT `large_id_m` FOREIGN KEY (`large_id`) REFERENCES `category_l` (`ctgr_lid`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category_m`
--

LOCK TABLES `category_m` WRITE;
/*!40000 ALTER TABLE `category_m` DISABLE KEYS */;
INSERT INTO `category_m` VALUES (1,'분식',1),(2,'한식',1),(3,'일식',1),(4,'중식',1),(5,'양식',1),(6,'아시안식',1),(7,'관광지',2),(8,'문화시설',2),(9,'공연행사',2),(10,'레포츠',2),(11,'엔조이',2),(12,'면',1),(13,'생선',1),(14,'밥',1),(15,'빵',1),(16,'고기',1),(17,'생선',1),(18,'해물',1),(19,'해산물',1),(20,'국',1),(21,'국밥',1),(22,'전',1),(23,'찌개',1),(24,'튀김',1),(25,'덮밥',1),(26,'만두',1);
/*!40000 ALTER TABLE `category_m` ENABLE KEYS */;
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
