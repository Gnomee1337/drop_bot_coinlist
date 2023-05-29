-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Server version: 8.0.30
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `reg_bot`
--

-- --------------------------------------------------------

--
-- Table structure for table `drop_accs`
--

CREATE TABLE IF NOT EXISTS `drop_accs` (
  `id_drop_accs` int NOT NULL AUTO_INCREMENT,
  `tg_id` bigint NOT NULL,
  `tg_username` varchar(33) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `middle_name` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `surname` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `country` varchar(60) DEFAULT NULL,
  `region` varchar(33) DEFAULT NULL,
  `city` varchar(33) DEFAULT NULL,
  `address` varchar(60) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `postcode` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `date_of_birth` varchar(15) DEFAULT NULL,
  `document_id` varchar(33) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `phone_number` varchar(30) DEFAULT NULL,
  `referral_id` bigint DEFAULT NULL,
  `language` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT 'ru',
  `verified` tinyint(1) NOT NULL DEFAULT '0',
  `user_status` varchar(33) NOT NULL DEFAULT 'new',
  `approve_date` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `payment_date` varchar(15) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`id_drop_accs`),
  UNIQUE KEY `tg_id` (`tg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `drop_manager`
--

CREATE TABLE IF NOT EXISTS `drop_manager` (
  `drop_manager_id` int NOT NULL AUTO_INCREMENT,
  `dm_tg_id` bigint NOT NULL,
  `dm_tg_username` varchar(33) NOT NULL,
  `invited_users` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`drop_manager_id`),
  UNIQUE KEY `dm_tg_id` (`dm_tg_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `top_manager`
--

CREATE TABLE IF NOT EXISTS `top_manager` (
  `id_top_manager` int NOT NULL AUTO_INCREMENT,
  `tg_id_top_manager` bigint NOT NULL,
  `tg_username_top_manager` varchar(35) NOT NULL,
  PRIMARY KEY (`id_top_manager`),
  UNIQUE KEY `tg_id_top_manager` (`tg_id_top_manager`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

-- --------------------------------------------------------

--
-- Table structure for table `webpanel_accounts`
--

CREATE TABLE IF NOT EXISTS `webpanel_accounts` (
  `id_wp_accs` int NOT NULL AUTO_INCREMENT,
  `username_wp_accs` varchar(30) NOT NULL,
  `password_wp_accs` varchar(80) NOT NULL,
  PRIMARY KEY (`id_wp_accs`),
  UNIQUE KEY `username_wp_accs` (`username_wp_accs`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
