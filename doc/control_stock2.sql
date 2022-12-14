-- MySQL Workbench Synchronization
-- Generated: 2022-10-24 09:31
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: Carlos Rivas

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

ALTER SCHEMA `stock`  DEFAULT CHARACTER SET utf8  DEFAULT COLLATE utf8_general_ci ;

ALTER TABLE `stock`.`Usuarios` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `stock`.`Proveedores` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;

ALTER TABLE `stock`.`Productos` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ,
CHANGE COLUMN `precio` `precio` DECIMAL(11,2) NOT NULL ;

ALTER TABLE `stock`.`cantidades` 
CHARACTER SET = utf8 , COLLATE = utf8_general_ci ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
