-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: mysql:3306
-- Generation Time: Apr 06, 2025 at 11:46 PM
-- Server version: 8.0.41
-- PHP Version: 8.2.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mindtrack`
--

-- --------------------------------------------------------

--
-- Table structure for table `projeto_mindtrack_formulario`
--

CREATE TABLE `projeto_mindtrack_formulario` (
  `formularioID` int NOT NULL,
  `data_resposta` date DEFAULT NULL,
  `usuario_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `projeto_mindtrack_formulariopergunta`
--

CREATE TABLE `projeto_mindtrack_formulariopergunta` (
  `id` bigint NOT NULL,
  `formulario_id` int NOT NULL,
  `pergunta_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `projeto_mindtrack_pergunta`
--

CREATE TABLE `projeto_mindtrack_pergunta` (
  `perguntaID` int NOT NULL,
  `pergunta` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `projeto_mindtrack_resposta`
--

CREATE TABLE `projeto_mindtrack_resposta` (
  `id` bigint NOT NULL,
  `resposta` tinyint(1) NOT NULL,
  `formulario_id` int NOT NULL,
  `pergunta_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `projeto_mindtrack_resultado`
--

CREATE TABLE `projeto_mindtrack_resultado` (
  `resultadoID` int NOT NULL,
  `pontuacao` int NOT NULL,
  `estratificacao` varchar(50) NOT NULL,
  `formulario_id` int NOT NULL,
  `usuario_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `projeto_mindtrack_usuario`
--

CREATE TABLE `projeto_mindtrack_usuario` (
  `usuarioID` int NOT NULL,
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `idade` int NOT NULL,
  `sexo` varchar(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `projeto_mindtrack_formulario`
--
ALTER TABLE `projeto_mindtrack_formulario`
  ADD PRIMARY KEY (`formularioID`),
  ADD KEY `projeto_mindtrack_fo_usuario_id_937b226c_fk_projeto_m` (`usuario_id`);

--
-- Indexes for table `projeto_mindtrack_formulariopergunta`
--
ALTER TABLE `projeto_mindtrack_formulariopergunta`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `projeto_mindtrack_formul_formulario_id_pergunta_i_6bb602d0_uniq` (`formulario_id`,`pergunta_id`),
  ADD KEY `projeto_mindtrack_fo_pergunta_id_e16bd918_fk_projeto_m` (`pergunta_id`);

--
-- Indexes for table `projeto_mindtrack_pergunta`
--
ALTER TABLE `projeto_mindtrack_pergunta`
  ADD PRIMARY KEY (`perguntaID`);

--
-- Indexes for table `projeto_mindtrack_resposta`
--
ALTER TABLE `projeto_mindtrack_resposta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `projeto_mindtrack_re_formulario_id_8faa205b_fk_projeto_m` (`formulario_id`),
  ADD KEY `projeto_mindtrack_re_pergunta_id_f09eb173_fk_projeto_m` (`pergunta_id`);

--
-- Indexes for table `projeto_mindtrack_resultado`
--
ALTER TABLE `projeto_mindtrack_resultado`
  ADD PRIMARY KEY (`resultadoID`),
  ADD KEY `projeto_mindtrack_re_formulario_id_f8db03eb_fk_projeto_m` (`formulario_id`),
  ADD KEY `projeto_mindtrack_re_usuario_id_78e5992f_fk_projeto_m` (`usuario_id`);

--
-- Indexes for table `projeto_mindtrack_usuario`
--
ALTER TABLE `projeto_mindtrack_usuario`
  ADD PRIMARY KEY (`usuarioID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `projeto_mindtrack_formulario`
--
ALTER TABLE `projeto_mindtrack_formulario`
  MODIFY `formularioID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projeto_mindtrack_formulariopergunta`
--
ALTER TABLE `projeto_mindtrack_formulariopergunta`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projeto_mindtrack_pergunta`
--
ALTER TABLE `projeto_mindtrack_pergunta`
  MODIFY `perguntaID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projeto_mindtrack_resposta`
--
ALTER TABLE `projeto_mindtrack_resposta`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projeto_mindtrack_resultado`
--
ALTER TABLE `projeto_mindtrack_resultado`
  MODIFY `resultadoID` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projeto_mindtrack_usuario`
--
ALTER TABLE `projeto_mindtrack_usuario`
  MODIFY `usuarioID` int NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `projeto_mindtrack_formulario`
--
ALTER TABLE `projeto_mindtrack_formulario`
  ADD CONSTRAINT `projeto_mindtrack_fo_usuario_id_937b226c_fk_projeto_m` FOREIGN KEY (`usuario_id`) REFERENCES `projeto_mindtrack_usuario` (`usuarioID`);

--
-- Constraints for table `projeto_mindtrack_formulariopergunta`
--
ALTER TABLE `projeto_mindtrack_formulariopergunta`
  ADD CONSTRAINT `projeto_mindtrack_fo_formulario_id_01850291_fk_projeto_m` FOREIGN KEY (`formulario_id`) REFERENCES `projeto_mindtrack_formulario` (`formularioID`),
  ADD CONSTRAINT `projeto_mindtrack_fo_pergunta_id_e16bd918_fk_projeto_m` FOREIGN KEY (`pergunta_id`) REFERENCES `projeto_mindtrack_pergunta` (`perguntaID`);

--
-- Constraints for table `projeto_mindtrack_resposta`
--
ALTER TABLE `projeto_mindtrack_resposta`
  ADD CONSTRAINT `projeto_mindtrack_re_formulario_id_8faa205b_fk_projeto_m` FOREIGN KEY (`formulario_id`) REFERENCES `projeto_mindtrack_formulario` (`formularioID`),
  ADD CONSTRAINT `projeto_mindtrack_re_pergunta_id_f09eb173_fk_projeto_m` FOREIGN KEY (`pergunta_id`) REFERENCES `projeto_mindtrack_pergunta` (`perguntaID`);

--
-- Constraints for table `projeto_mindtrack_resultado`
--
ALTER TABLE `projeto_mindtrack_resultado`
  ADD CONSTRAINT `projeto_mindtrack_re_formulario_id_f8db03eb_fk_projeto_m` FOREIGN KEY (`formulario_id`) REFERENCES `projeto_mindtrack_formulario` (`formularioID`),
  ADD CONSTRAINT `projeto_mindtrack_re_usuario_id_78e5992f_fk_projeto_m` FOREIGN KEY (`usuario_id`) REFERENCES `projeto_mindtrack_usuario` (`usuarioID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
