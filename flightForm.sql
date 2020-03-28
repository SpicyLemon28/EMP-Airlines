-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Mar 25, 2020 at 04:08 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Airlines`
--

-- --------------------------------------------------------

--
-- Table structure for table `flightForm`
--

CREATE TABLE `flightForm` (
  `flyingFrom` varchar(50) NOT NULL,
  `flyingTo` varchar(50) NOT NULL,
  `departingOn` date DEFAULT NULL,
  `returningOn` date DEFAULT NULL,
  `departureTime` time DEFAULT NULL,
  `returningTime` time DEFAULT NULL,
  `fullName` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone` int(20) NOT NULL,
  `nationality` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `passportNo` int(20) NOT NULL,
  `passportExpiryDate` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `flightForm`
--

INSERT INTO `flightForm` (`flyingFrom`, `flyingTo`, `departingOn`, `returningOn`, `departureTime`, `returningTime`, `fullName`, `email`, `phone`, `nationality`, `gender`, `passportNo`, `passportExpiryDate`) VALUES
('a', 'a', '2020-01-01', '2020-01-01', '01:00:00', '02:00:00', 'a', 'a', 123, 'a', 'a', 222, '2020-02-02'),
('b', 'b', '2020-02-02', '2020-03-30', '02:00:00', '03:00:00', 'b', 'b', 123, 'b', 'b', 333, '2025-04-04');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
