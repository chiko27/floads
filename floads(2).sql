# Host: localhost  (Version 5.5.5-10.4.19-MariaDB)
# Date: 2021-11-24 11:48:05
# Generator: MySQL-Front 6.0  (Build 2.20)


#
# Structure for table "spesies_ikan"
#

DROP TABLE IF EXISTS `spesies_ikan`;
CREATE TABLE `spesies_ikan` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `tglJam` varchar(150) DEFAULT NULL,
  `berat` float(10,3) DEFAULT NULL,
  `spesies` varchar(30) DEFAULT NULL,
  `hitung` int(11) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4;

#
# Data for table "spesies_ikan"
#

INSERT INTO `spesies_ikan` VALUES (1,'2021-11-10 22:58:22',167.683,'Euthynnus affinis',NULL),(2,'2021-11-10 22:58:24',130.723,'Euthynnus affinis',NULL),(3,'2021-11-10 22:58:25',140.504,'Katsuwonus pelamis',NULL),(4,'2021-11-10 22:58:26',126.858,'Euthynnus affinis',NULL),(5,'2021-11-10 22:58:27',138.245,'Euthynnus affinis',NULL),(6,'2021-11-10 22:58:28',122.453,'Katsuwonus pelamis',NULL),(7,'2021-11-10 22:58:29',132.031,'Euthynnus affinis',NULL),(8,'2021-11-10 22:58:30',144.194,'Katsuwonus pelamis',NULL),(9,'2021-11-10 22:58:31',156.082,'Katsuwonus pelamis',NULL),(10,'2021-11-10 22:58:32',166.832,'Euthynnus affinis',NULL),(11,'2021-11-10 22:58:33',146.915,'Katsuwonus pelamis',NULL),(12,'2021-11-10 22:58:34',135.979,'Euthynnus affinis',NULL),(13,'2021-11-10 22:58:35',121.318,'Katsuwonus pelamis',NULL),(14,'2021-11-10 22:58:36',168.782,'Katsuwonus pelamis',NULL),(15,'2021-11-10 22:58:38',120.267,'Euthynnus affinis',NULL),(16,'2021-11-10 22:59:37',160.341,'Katsuwonus pelamis',NULL),(17,'2021-11-10 22:59:38',132.297,'Euthynnus affinis',NULL),(18,'2021-11-10 22:59:39',147.594,'Euthynnus affinis',NULL),(19,'2021-11-10 22:59:40',131.873,'Euthynnus affinis',NULL),(20,'2021-11-10 22:59:42',140.433,'Katsuwonus pelamis',NULL),(21,'2021-11-10 22:59:43',131.800,'Katsuwonus pelamis',NULL),(22,'2021-11-10 22:59:44',131.924,'Euthynnus affinis',NULL),(23,'2021-11-10 22:59:45',148.436,'Euthynnus affinis',NULL),(24,'2021-11-10 22:59:46',120.925,'Euthynnus affinis',NULL),(25,'2021-11-10 22:59:47',127.639,'Katsuwonus pelamis',NULL);

#
# Structure for table "user"
#

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL DEFAULT '',
  `email` varchar(100) NOT NULL DEFAULT '',
  `password` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

#
# Data for table "user"
#

