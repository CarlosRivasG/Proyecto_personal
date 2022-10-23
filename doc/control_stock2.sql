-- MySQL Workbench Synchronization
-- Generated: 2022-10-15 15:06
-- Model: New Model
-- Version: 1.0
-- Project: Name of the project
-- Author: Carlos Rivas

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

CREATE SCHEMA IF NOT EXISTS `stock` DEFAULT CHARACTER SET utf8 ;

CREATE TABLE IF NOT EXISTS `stock`.`Usuarios` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NOT NULL,
  `apellido` VARCHAR(255) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `stock`.`Proveedores` (
  `id` INT(11) NOT NULL,
  `nombre` VARCHAR(255) NOT NULL,
  `empresa` VARCHAR(255) NOT NULL,
  `pais` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

CREATE TABLE IF NOT EXISTS `stock`.`Productos` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL,
  `cantidad` DECIMAL NOT NULL,
  `precio` DECIMAL NOT NULL,
  `descripcion` VARCHAR(255) NOT NULL,
  `tipo_producto` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL,
  `updated_at` DATETIME NOT NULL,
  `Usuario_id` INT(11) NOT NULL,
  `Proveedor_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Bodegas_Ususarios1_idx` (`Usuario_id` ASC) VISIBLE,
  INDEX `fk_Bodegas_Proveedores1_idx` (`Proveedor_id` ASC) VISIBLE,
  CONSTRAINT `fk_Bodegas_Ususarios1`
    FOREIGN KEY (`Usuario_id`)
    REFERENCES `stock`.`Usuarios` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Bodegas_Proveedores1`
    FOREIGN KEY (`Proveedor_id`)
    REFERENCES `stock`.`Proveedores` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
