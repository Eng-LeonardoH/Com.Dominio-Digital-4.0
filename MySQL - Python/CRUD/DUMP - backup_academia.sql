-- MySQL dump 10.13  Distrib 8.0.35, for Win64 (x86_64)
--
-- Host: localhost    Database: academia
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `alunos`
--

DROP TABLE IF EXISTS `alunos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alunos` (
  `telefone` char(11) NOT NULL,
  `matricula` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(128) NOT NULL,
  `endereco` varchar(256) NOT NULL,
  PRIMARY KEY (`matricula`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alunos`
--

LOCK TABLES `alunos` WRITE;
/*!40000 ALTER TABLE `alunos` DISABLE KEYS */;
INSERT INTO `alunos` VALUES ('22222222222',9,'Aluno01','Rua do Jaboticabal, Nº666, Junta de Seu Jorge, Maranguapaticatu, Alagoas, Brasil'),('22222222222',10,'Aluno01','Rua do Jaboticabal, Nº666, Junta de Seu Jorge, Maranguapaticatu, Alagoas, Brasil'),('22222222222',11,'Aluno01','Rua do Jaboticabal, Nº666, Junta de Seu Jorge, Maranguapaticatu, Alagoas, Brasil'),('111111111',12,'Aluno00','Logradouro, Nº000, Bairro, Cidade, Estado, País'),('111111111',13,'Aluno00','Logradouro, Nº000, Bairro, Cidade, Estado, País'),('111111111',14,'Aluno00','Logradouro, Nº000, Bairro, Cidade, Estado, País'),('111111111',15,'Aluno00','Logradouro, Nº000, Bairro, Cidade, Estado, País'),('111111111',16,'Aluno00','Logradouro, Nº000, Bairro, Cidade, Estado, País'),('111111111',17,'Aluno00','Logradouro, Nº000, Bairro, Cidade, Estado, País'),('111111111',18,'Aluno00','Logradouro, Nº000, Bairro, Cidade, Estado, País'),('111111111',19,'Aluno00','Logradouro, Nº000, Bairro, Cidade, Estado, País'),('111111111',20,'Aluno00','Logradouro, Nº000, Bairro, Cidade, Estado, País'),('111111111',21,'Aluno00','Logradouro, Nº000, Bairro, Cidade, Estado, País'),('111111111',22,'Aluno00','Logradouro, Nº000, Bairro, Cidade, Estado, País'),('111111111',23,'Aluno00','Logradouro, Nº000, Bairro, Cidade, Estado, País');
/*!40000 ALTER TABLE `alunos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(230) NOT NULL,
  `cpf` char(11) NOT NULL,
  `departamento` int NOT NULL,
  `cpf_supervisor` char(11) NOT NULL,
  `salario` float NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcoes`
--

DROP TABLE IF EXISTS `funcoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcoes` (
  `atribuicao` varchar(20) NOT NULL,
  `salario` float NOT NULL,
  `ID_FUNCAO` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID_FUNCAO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcoes`
--

LOCK TABLES `funcoes` WRITE;
/*!40000 ALTER TABLE `funcoes` DISABLE KEYS */;
/*!40000 ALTER TABLE `funcoes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-17 16:08:16
