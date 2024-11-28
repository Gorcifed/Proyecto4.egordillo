-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: heladeria
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `ingredientes`
--

DROP TABLE IF EXISTS `ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) DEFAULT NULL,
  `precio` int NOT NULL,
  `calorias` decimal(5,2) NOT NULL,
  `vegetariano` int NOT NULL,
  `inventario` decimal(5,2) NOT NULL,
  `tipo` varchar(15) NOT NULL,
  `sabor` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_UNIQUE` (`nombre`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientes`
--

LOCK TABLES `ingredientes` WRITE;
/*!40000 ALTER TABLE `ingredientes` DISABLE KEYS */;
INSERT INTO `ingredientes` VALUES (1,'Helado de fresa',1500,50.00,0,1.00,'Base','Fresa'),(2,'Chispas de chocolate',2500,80.00,0,0.80,'Base','Chocolate'),(3,'Maní sin dulce',1200,10.00,1,20.00,'Complemento','Maní'),(4,'Helado de vainilla',1300,48.00,0,0.20,'Base','Vainilla'),(5,'Helado de chocolate',1800,120.00,0,0.60,'Base','Chocolate'),(6,'Cereales',500,10.00,1,1.20,'Base','Maíz'),(7,'Frutas varias',900,25.00,1,5.00,'Complemento','Frutas varias'),(8,'Chispas de colores',1000,52.00,1,5.00,'Complemento','Dulce'),(9,'Crema de leche',1500,400.00,0,10.00,'Complemento','Leche'),(10,'Crema chantilly',3000,200.00,0,5.00,'Complemento','Crema');
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `precio` int NOT NULL,
  `ventas_dia` int NOT NULL,
  `precio_ventas_dia` int NOT NULL,
  `id_ingrediente1` int NOT NULL,
  `id_ingrediente2` int NOT NULL,
  `id_ingrediente3` int NOT NULL,
  `tipo` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre_UNIQUE` (`nombre`),
  KEY `fk_producto_ingrediente1_idx` (`id_ingrediente1`),
  KEY `fk_producto_ingrediente2_idx` (`id_ingrediente2`),
  KEY `fk_producto_ingrediente3_idx` (`id_ingrediente3`),
  CONSTRAINT `fk_producto_ingrediente1` FOREIGN KEY (`id_ingrediente1`) REFERENCES `ingredientes` (`id`),
  CONSTRAINT `fk_producto_ingrediente2` FOREIGN KEY (`id_ingrediente2`) REFERENCES `ingredientes` (`id`),
  CONSTRAINT `fk_producto_ingrediente3` FOREIGN KEY (`id_ingrediente3`) REFERENCES `ingredientes` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Copa Mickey de fresa',15000,0,0,1,2,3,'Copa'),(2,'Copa Donald',12000,0,0,6,9,8,'Copa'),(3,'Copa Goofy',11500,0,0,4,9,7,'Copa'),(4,'Malteada Deisy',18000,0,0,4,9,7,'Malteada'),(5,'Malteada Pluto',15000,0,0,5,9,8,'Malteada'),(6,'Malteada Minnie',12000,0,0,1,9,8,'Malteada');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `alias` varchar(45) NOT NULL,
  `contrasena` varchar(45) NOT NULL,
  `es_admin` int NOT NULL,
  `es_empleado` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'admin','123',1,0),(2,'administrator','234',1,0),(3,'user1','345',0,0),(4,'user2','456',0,1);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-26 17:47:20
