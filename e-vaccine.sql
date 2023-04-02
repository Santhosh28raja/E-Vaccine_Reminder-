-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 16, 2021 at 02:35 PM
-- Server version: 10.1.34-MariaDB
-- PHP Version: 7.2.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `e-vaccine`
--

-- --------------------------------------------------------

--
-- Table structure for table `adddetail`
--

CREATE TABLE `adddetail` (
  `poid` varchar(20) NOT NULL,
  `id` int(25) NOT NULL,
  `childname` varchar(11) NOT NULL,
  `birthplace` varchar(56) NOT NULL,
  `dob` varchar(25) NOT NULL,
  `childage` varchar(20) NOT NULL,
  `weight` varchar(18) NOT NULL,
  `parentname` varchar(30) NOT NULL,
  `phoneno` varchar(29) NOT NULL,
  `email` varchar(100) NOT NULL,
  `vaccine1` varchar(150) NOT NULL,
  `vaccine2` varchar(150) NOT NULL,
  `vaccine3` varchar(150) NOT NULL,
  `vaccine4` varchar(150) NOT NULL,
  `vaccine5` varchar(150) NOT NULL,
  `vaccine6` varchar(150) NOT NULL,
  `vaccine7` varchar(150) NOT NULL,
  `vaccine8` varchar(150) NOT NULL,
  `vaccine9` varchar(150) NOT NULL,
  `vaccine10` varchar(150) NOT NULL,
  `emailstatus` varchar(25) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adddetail`
--

INSERT INTO `adddetail` (`poid`, `id`, `childname`, `birthplace`, `dob`, `childage`, `weight`, `parentname`, `phoneno`, `email`, `vaccine1`, `vaccine2`, `vaccine3`, `vaccine4`, `vaccine5`, `vaccine6`, `vaccine7`, `vaccine8`, `vaccine9`, `vaccine10`, `emailstatus`, `status`) VALUES
('6', 1, 'baby', 'psg hospital', '11.02.2020', '1', '2.5kg', 'anand', '9944973761', '', '', '', '', '', '', '', '', '', '', '', '', ''),
('6', 3, 'dev', 'psg hospital', '11.02.2020', '1', '2', 'jon', '123654741258', '', '', '', '', '', '', '', '', '', '', '', '', ''),
('7', 4, 'nive', 'ramakrishna hospital', '11.06.2020', '1', '1.5', 'jeeva', '123654741258', '', '', '', '', '', '', '', '', '', '', '', '', ''),
('7', 5, 'diya', 'apollo hospital', '11.02.2021', '2', '3.5', 'siva', '12346798245', '', '', '', '', '', '', '', '', '', '', '', '', ''),
('8', 6, 'diya', 'gct  hospital', '11.2.2020', '2', '2', 'jeeva', '1234567891', 'sandycsekar@gmail.com', 'Vaccine as been taken on 01/03/2021', 'Vaccine as been taken on 03/03/2021', 'Vaccine as been taken on 05/03/2021', 'Vaccine as been taken on 10/03/2021', '12/06/2021', '12/09/2021', '12/01/2022', '12/12/2022', '12/12/2024', '12/12/2026', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `adddoc`
--

CREATE TABLE `adddoc` (
  `id` int(25) NOT NULL,
  `hoid` varchar(20) NOT NULL,
  `name` varchar(50) NOT NULL,
  `specialization` varchar(56) NOT NULL,
  `degree` varchar(20) NOT NULL,
  `experience` varchar(28) NOT NULL,
  `joiningdate` varchar(20) NOT NULL,
  `gender` varchar(46) NOT NULL,
  `emailid` varchar(40) NOT NULL,
  `phoneno` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adddoc`
--

INSERT INTO `adddoc` (`id`, `hoid`, `name`, `specialization`, `degree`, `experience`, `joiningdate`, `gender`, `emailid`, `phoneno`) VALUES
(2, '15', 'DR.SHANTHI', 'GASTRO SURGEON', 'MBBS', '14', '06.11.1998', 'female', 'divya@gmail.com', '123654741258'),
(3, '15', 'DR.KARTHI', 'PSYCIATRIST', 'MBBS', '10', '1.2.2020', 'male', 'karthi@gmail.com', '12346798245'),
(4, '16', 'DR.LOKESH', 'PSYCIATRIST', 'MBBS', '12', '1.2.2020', 'male', 'lokesh@gmail.com', '123654741258');

-- --------------------------------------------------------

--
-- Table structure for table `addhos`
--

CREATE TABLE `addhos` (
  `id` int(20) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `hosname` varchar(250) NOT NULL,
  `hosaddress` varchar(254) NOT NULL,
  `phoneno` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `addhos`
--

INSERT INTO `addhos` (`id`, `username`, `password`, `hosname`, `hosaddress`, `phoneno`, `email`) VALUES
(15, 'james', 'james', 'sakthi hospital', 'rs puram', '123654741258', 'sakthi@gmail.com'),
(16, 'sara', 'sara', 'bethel hospital', 'gandhipuram 100feet road', '9944973761', 'bethel@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `polio`
--

CREATE TABLE `polio` (
  `id` int(20) NOT NULL,
  `poliodate` date NOT NULL,
  `agelimit` varchar(35) NOT NULL,
  `poliostatus` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `polio`
--

INSERT INTO `polio` (`id`, `poliodate`, `agelimit`, `poliostatus`) VALUES
(1, '2021-04-18', '1-10 Age', 'enable');

-- --------------------------------------------------------

--
-- Table structure for table `query`
--

CREATE TABLE `query` (
  `id` int(10) NOT NULL,
  `pid` int(10) NOT NULL,
  `docid` int(10) NOT NULL,
  `message` varchar(100) NOT NULL,
  `desp` varchar(255) NOT NULL,
  `reply` varchar(255) NOT NULL,
  `status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `query`
--

INSERT INTO `query` (`id`, `pid`, `docid`, `message`, `desp`, `reply`, `status`) VALUES
(1, 8, 15, 'My as skin crash', 'we apply the pointy what shall we do', 'Take a rest and sleep well take dolo 650 dosage tablet', 'Message Replied'),
(2, 8, 15, 'Fever', '100c with body pain', '', 'Not Completed');

-- --------------------------------------------------------

--
-- Table structure for table `regi`
--

CREATE TABLE `regi` (
  `id` int(20) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `phoneno` varchar(20) NOT NULL,
  `email` varchar(25) NOT NULL,
  `polioemail` varchar(54) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `regi`
--

INSERT INTO `regi` (`id`, `username`, `password`, `gender`, `phoneno`, `email`, `polioemail`) VALUES
(4, 'divya', 'divya', 'Female', '9944973761', 'vinithasri@gmail.com', ''),
(6, 'sri', 'sri', 'Female', '1345649', 'vinithasri@gmail.com', ''),
(7, 'siva', 'siva', 'Male', '123654741258', 'siva@gmail.com', ''),
(8, 'sandhiya', 'sandhiya', 'Female', '9944973761', 'sandycsekar@gmail.com', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adddetail`
--
ALTER TABLE `adddetail`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `adddoc`
--
ALTER TABLE `adddoc`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `addhos`
--
ALTER TABLE `addhos`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `polio`
--
ALTER TABLE `polio`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `query`
--
ALTER TABLE `query`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `regi`
--
ALTER TABLE `regi`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adddetail`
--
ALTER TABLE `adddetail`
  MODIFY `id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `adddoc`
--
ALTER TABLE `adddoc`
  MODIFY `id` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `addhos`
--
ALTER TABLE `addhos`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `polio`
--
ALTER TABLE `polio`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `query`
--
ALTER TABLE `query`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `regi`
--
ALTER TABLE `regi`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
