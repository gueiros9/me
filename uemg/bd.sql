-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 22, 2020 at 03:40 PM
-- Server version: 10.4.16-MariaDB
-- PHP Version: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `trabalho`
--

-- --------------------------------------------------------

--
-- Table structure for table `cidade`
--

CREATE TABLE `cidade` (
  `cod_cid` int(11) NOT NULL,
  `nome_cid` varchar(45) DEFAULT NULL,
  `sigla_uf` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `classe`
--

CREATE TABLE `classe` (
  `cod_cla` int(11) NOT NULL,
  `nome_cla` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `cliente`
--

CREATE TABLE `cliente` (
  `cod_cli` int(11) NOT NULL,
  `nome_cli` varchar(40) NOT NULL,
  `nm_logr` varchar(100) NOT NULL,
  `nr_logr` int(11) NOT NULL,
  `nm_bairro` varchar(45) NOT NULL,
  `nr_cep` int(11) NOT NULL,
  `cod_cid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `parcela`
--

CREATE TABLE `parcela` (
  `cod_ven` int(11) NOT NULL,
  `cod_par` int(11) NOT NULL,
  `data_vcto` date NOT NULL,
  `valor_par` double NOT NULL,
  `data_pagto` date NOT NULL,
  `valor_pago` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `produto`
--

CREATE TABLE `produto` (
  `cod_pro` int(11) NOT NULL,
  `desc_pro` varchar(45) NOT NULL,
  `valor_pro` double NOT NULL,
  `qtde_pro` int(11) NOT NULL,
  `cod_cla` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `produto_vendido`
--

CREATE TABLE `produto_vendido` (
  `cod_ven` int(11) NOT NULL,
  `cod_pro` int(11) NOT NULL,
  `qt_ven` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `venda`
--

CREATE TABLE `venda` (
  `cod_ven` int(11) NOT NULL,
  `data_ven` date NOT NULL,
  `valor_ven` double NOT NULL,
  `cod_cli` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cidade`
--
ALTER TABLE `cidade`
  ADD PRIMARY KEY (`cod_cid`);

--
-- Indexes for table `classe`
--
ALTER TABLE `classe`
  ADD PRIMARY KEY (`cod_cla`);

--
-- Indexes for table `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`cod_cli`),
  ADD KEY `cod_cid` (`cod_cid`);

--
-- Indexes for table `parcela`
--
ALTER TABLE `parcela`
  ADD PRIMARY KEY (`cod_par`),
  ADD KEY `cod_ven` (`cod_ven`);

--
-- Indexes for table `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`cod_pro`),
  ADD KEY `cod_cla` (`cod_cla`);

--
-- Indexes for table `produto_vendido`
--
ALTER TABLE `produto_vendido`
  ADD KEY `cod_ven` (`cod_ven`),
  ADD KEY `cod_pro` (`cod_pro`);

--
-- Indexes for table `venda`
--
ALTER TABLE `venda`
  ADD PRIMARY KEY (`cod_ven`),
  ADD KEY `cod_cli` (`cod_cli`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cliente`
--
ALTER TABLE `cliente`
  ADD CONSTRAINT `cliente_ibfk_1` FOREIGN KEY (`cod_cid`) REFERENCES `cidade` (`cod_cid`);

--
-- Constraints for table `parcela`
--
ALTER TABLE `parcela`
  ADD CONSTRAINT `parcela_ibfk_1` FOREIGN KEY (`cod_ven`) REFERENCES `venda` (`cod_ven`);

--
-- Constraints for table `produto`
--
ALTER TABLE `produto`
  ADD CONSTRAINT `produto_ibfk_1` FOREIGN KEY (`cod_cla`) REFERENCES `classe` (`cod_cla`);

--
-- Constraints for table `produto_vendido`
--
ALTER TABLE `produto_vendido`
  ADD CONSTRAINT `produto_vendido_ibfk_1` FOREIGN KEY (`cod_ven`) REFERENCES `venda` (`cod_ven`),
  ADD CONSTRAINT `produto_vendido_ibfk_2` FOREIGN KEY (`cod_pro`) REFERENCES `produto` (`cod_pro`);

--
-- Constraints for table `venda`
--
ALTER TABLE `venda`
  ADD CONSTRAINT `venda_ibfk_1` FOREIGN KEY (`cod_cli`) REFERENCES `cliente` (`cod_cli`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
