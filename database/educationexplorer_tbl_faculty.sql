-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: educationexplorer
-- ------------------------------------------------------
-- Server version	5.7.18-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tbl_faculty`
--

DROP TABLE IF EXISTS `tbl_faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_faculty` (
  `faculty_id` int(200) NOT NULL AUTO_INCREMENT,
  `faculty_name` varchar(160) NOT NULL,
  `others` enum('1','0') NOT NULL COMMENT '1 for True, 0 for False',
  `management` enum('1','0') NOT NULL COMMENT '1 for True, 0 for False',
  `engineering` enum('1','0') NOT NULL COMMENT '1 for True, 0 for False',
  `information_technology` enum('1','0') NOT NULL COMMENT '1 for True, 0 for False',
  `medical` enum('1','0') NOT NULL COMMENT '1 for True, 0 for False',
  PRIMARY KEY (`faculty_id`),
  FULLTEXT KEY `idx_tbl_faculty_faculty_name` (`faculty_name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_faculty`
--

LOCK TABLES `tbl_faculty` WRITE;
/*!40000 ALTER TABLE `tbl_faculty` DISABLE KEYS */;
INSERT INTO `tbl_faculty` VALUES (1,'Business','0','1','0','0','0'),(2,'Engineering','0','0','1','0','0'),(3,'IT','0','0','0','1','0'),(4,'Medical','0','0','0','0','1'),(5,'Other','1','0','0','0','0');
/*!40000 ALTER TABLE `tbl_faculty` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-07-29 15:02:58
