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
-- Table structure for table `tbl_affilation`
--

DROP TABLE IF EXISTS `tbl_affilation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tbl_affilation` (
  `affilation_id` int(255) NOT NULL AUTO_INCREMENT,
  `affilation_name` varchar(50) NOT NULL,
  `tribhuwan_university` enum('1','0') NOT NULL COMMENT '1 for True, 0 for False',
  `kathmandu_university` enum('1','0') NOT NULL COMMENT '1 for True, 0 for False',
  `pokhara_university` enum('1','0') NOT NULL COMMENT '1 for True, 0 for False',
  `purbanchal_university` enum('1','0') NOT NULL COMMENT '1 for True, 0 for False',
  `ctevt` enum('1','0') NOT NULL COMMENT '1 for True, 0 for False',
  `others` enum('1','0') NOT NULL COMMENT '1 for True, 0 for False',
  PRIMARY KEY (`affilation_id`),
  FULLTEXT KEY `idx_tbl_affilation_affilation_name` (`affilation_name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_affilation`
--

LOCK TABLES `tbl_affilation` WRITE;
/*!40000 ALTER TABLE `tbl_affilation` DISABLE KEYS */;
INSERT INTO `tbl_affilation` VALUES (1,'Tribhuwan University','1','0','0','0','0','0'),(2,'Kathmandu University','0','1','0','0','0','0'),(3,'Pokhara University','0','0','1','0','0','0'),(4,'Purbanchal University','0','0','0','1','0','0'),(5,'CTEVT','0','0','0','0','1','0'),(6,'Others','0','0','0','0','0','1');
/*!40000 ALTER TABLE `tbl_affilation` ENABLE KEYS */;
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
