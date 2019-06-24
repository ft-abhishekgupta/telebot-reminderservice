-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 24, 2019 at 02:00 PM
-- Server version: 5.7.26-0ubuntu0.16.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `reminder`
--

-- --------------------------------------------------------

--
-- Table structure for table `crypto_curr`
--

CREATE TABLE `crypto_curr` (
  `BTC` varchar(20) NOT NULL,
  `MKR` varchar(20) NOT NULL,
  `THR` varchar(20) NOT NULL,
  `BCH` varchar(20) NOT NULL,
  `XIN` varchar(20) NOT NULL,
  `ETH` varchar(20) NOT NULL,
  `DASH` varchar(20) NOT NULL,
  `BSV` varchar(20) NOT NULL,
  `LTC` varchar(20) NOT NULL,
  `ZEC` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='current values of top ten crypto currencies';

--
-- Dumping data for table `crypto_curr`
--

INSERT INTO `crypto_curr` (`BTC`, `MKR`, `THR`, `BCH`, `XIN`, `ETH`, `DASH`, `BSV`, `LTC`, `ZEC`) VALUES
('4922.04', '749.28', '713.69', '285.44', '194.83', '157.80', '125.33', '85.05', '83.50', '68.11');

-- --------------------------------------------------------

--
-- Table structure for table `reminders`
--

CREATE TABLE `reminders` (
  `chatId` varchar(100) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL,
  `message` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `subscription`
--

CREATE TABLE `subscription` (
  `userid` varchar(100) NOT NULL,
  `BTC` int(1) NOT NULL,
  `MKR` int(1) NOT NULL,
  `THR` int(1) NOT NULL,
  `BCH` int(1) NOT NULL,
  `XIN` int(1) NOT NULL,
  `ETH` int(1) NOT NULL,
  `DASH` int(1) NOT NULL,
  `BSV` int(1) NOT NULL,
  `LTC` int(1) NOT NULL,
  `ZEC` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `chatId` varchar(100) NOT NULL,
  `displayName` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `reminders`
--
ALTER TABLE `reminders`
  ADD PRIMARY KEY (`chatId`,`date`,`time`,`message`);

--
-- Indexes for table `subscription`
--
ALTER TABLE `subscription`
  ADD PRIMARY KEY (`userid`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`chatId`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
