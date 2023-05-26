-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
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

CREATE TABLE `drop_accs` (
  `id_drop_accs` int NOT NULL,
  `tg_id` bigint DEFAULT NULL,
  `tg_username` varchar(33) DEFAULT NULL,
  `country` varchar(60) DEFAULT NULL,
  `full_name` varchar(60) DEFAULT NULL,
  `phone_number` varchar(30) DEFAULT NULL,
  `address` varchar(60) DEFAULT NULL,
  `postal_code` varchar(10) DEFAULT NULL,
  `photo_name` varchar(60) DEFAULT NULL,
  `language` varchar(5) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT 'en',
  `verified` tinyint(1) NOT NULL DEFAULT '0',
  `user_status` int NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `drop_accs`
--
ALTER TABLE `drop_accs`
  ADD PRIMARY KEY (`id_drop_accs`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `drop_accs`
--
ALTER TABLE `drop_accs`
  MODIFY `id_drop_accs` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=0;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
