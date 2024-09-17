-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 17 Sep 2024 pada 16.49
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.1.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `visdat`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `biayapendidikan`
--

CREATE TABLE `biayapendidikan` (
  `tingkat` int(16) DEFAULT NULL,
  `nominal` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data untuk tabel `biayapendidikan`
--

INSERT INTO `biayapendidikan` (`tingkat`, `nominal`) VALUES
(1, 1100000.00),
(2, 1300000.00),
(3, 1700000.00),
(4, 1900000.00),
(5, 2000000.00),
(6, 2100000.00),
(7, 2500000.00),
(8, 2700000.00),
(9, 2900000.00),
(10, 3000000.00),
(11, 3100000.00),
(12, 3500000.00);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
