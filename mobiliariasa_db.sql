-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 18/03/2025 às 00:12
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `mobiliariasa_db`
--
CREATE DATABASE IF NOT EXISTS `mobiliariasa_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `mobiliariasa_db`;

-- --------------------------------------------------------

--
-- Estrutura para tabela `cadastro`
--

CREATE TABLE `cadastro` (
  `idusuario` int(11) NOT NULL,
  `nome` text DEFAULT NULL,
  `usuario` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `telefone` text DEFAULT NULL,
  `senha` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cadastro`
--

INSERT INTO `cadastro` (`idusuario`, `nome`, `usuario`, `email`, `telefone`, `senha`) VALUES
(1, 'Alisson Mecedez Fronza', 'ADM_AlissonFronza007', 'alissonn007@gmail.com', '47 99722-1010', 'spiderman007'),
(2, 'Bernado Luiz da Silva', 'ADM_BernadoSilva', 'bernadinhorico@gmail.com', '47 99887-3220', 'ricodemais@.com'),
(3, 'Henrrique Lima', 'lima_henrrique12', 'limas2020@gmail.com', 'limas2020@gmail.com', 'palmeirasmundial55'),
(4, 'Andressa Souza', 'souzax_ands', 'souzaandressapalmeiras@gmail.com', '47 99687-3243', 'luizagusto008');

-- --------------------------------------------------------

--
-- Estrutura para tabela `fornecedor`
--

CREATE TABLE `fornecedor` (
  `idfornecedor` int(11) NOT NULL,
  `nome_fornecedor` text DEFAULT NULL,
  `endereco` text DEFAULT NULL,
  `telefone` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `produto` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `fornecedor`
--

INSERT INTO `fornecedor` (`idfornecedor`, `nome_fornecedor`, `endereco`, `telefone`, `email`, `produto`) VALUES
(1, 'Carpintaria da Filha', 'rua iririu 890, bairro iririu Joinville/SC', '47 3434-0836', 'carpintariadafilha1900@gmail.com', 'Moveis de madeira'),
(2, 'Estofaria Bernedez', 'rua castelo-azul 1080, Jaragua do Sul/SC', '47 99834-0934', 'bernedezestofaria@gmail.com', 'Sofas,colchões,almofadas'),
(3, 'Vridraria Santos', 'rua ponte serrada 2321, Balneario do Sul/SC', '47 99943-0096', 'santosdevidro@gmail.com', 'Espelhos');

-- --------------------------------------------------------

--
-- Estrutura para tabela `funcionario`
--

CREATE TABLE `funcionario` (
  `idfuncionario` int(11) NOT NULL,
  `nome` text DEFAULT NULL,
  `cpf` text DEFAULT NULL,
  `telefone` text DEFAULT NULL,
  `email` text DEFAULT NULL,
  `cargo` text DEFAULT NULL,
  `salario` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `funcionario`
--

INSERT INTO `funcionario` (`idfuncionario`, `nome`, `cpf`, `telefone`, `email`, `cargo`, `salario`) VALUES
(1, 'Matheus dos Santos', '125.566.789-32', '47 99880-3421', 'corinthiastorcedor@gmail.com', 'Capintero de Ajustes', '3000'),
(2, 'Luiza Amanda de Oliveira', '968.008.231-32', '47 98890-2331', 'luizinhadogole@gmail.com', 'Vendendora', '1700'),
(3, 'Andressa Souza', '443.897.043-45', '47 99687-3243', 'souzaandressapalmeiras@gmail.com', 'Estoquista', '1500'),
(4, 'Luiz Costa', '123.443.588-54', '47 99844-0865', 'contapratrabalholuizcosta1972@gmail.com', 'Instalador ambulante de Moveis', '2800'),
(5, 'Henrrique Lima', '687.498.342-54', '47 9212-0932', 'limas2020@gmail.com', 'Lojista', '2100');

-- --------------------------------------------------------

--
-- Estrutura para tabela `produto`
--

CREATE TABLE `produto` (
  `codproduto` int(11) NOT NULL,
  `produto` text DEFAULT NULL,
  `descricao` text DEFAULT NULL,
  `quantidade` text DEFAULT NULL,
  `valordecompra` text DEFAULT NULL,
  `valordevenda` text DEFAULT NULL,
  `fornecedor` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `produto`
--

INSERT INTO `produto` (`codproduto`, `produto`, `descricao`, `quantidade`, `valordecompra`, `valordevenda`, `fornecedor`) VALUES
(1, 'Guarda-Roupa Luxe', 'Guarda-Roupa tres portas, espelho de corpo, 6 metros, carvalho', '150', '3000', '5400', 'Carpintaria da Filha'),
(2, 'Sofá 2 lugares marrom', 'Sofá pequeno de 2 lugares, de tecido madeira pau-Brasil marrom', '800', '500', '1200', 'Estofaria Bernedez'),
(3, 'Espelho de corpo 2x1', 'Espelho de corpo 2 metros por 1', '1100', '130', '240', 'VidrariaSantos'),
(4, 'Cama de solteiro ', 'Cama de solteiro de carvalho', '300', '400', '699', 'Carpintaria da Filha'),
(5, 'Mesa de Jantar de Roda', 'Mesa de Jantar com roda, de carvalho, marrom claro e escuro', '145', '650', '1050', 'Carpintaria da Filha');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cadastro`
--
ALTER TABLE `cadastro`
  ADD PRIMARY KEY (`idusuario`);

--
-- Índices de tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  ADD PRIMARY KEY (`idfornecedor`);

--
-- Índices de tabela `funcionario`
--
ALTER TABLE `funcionario`
  ADD PRIMARY KEY (`idfuncionario`);

--
-- Índices de tabela `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`codproduto`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cadastro`
--
ALTER TABLE `cadastro`
  MODIFY `idusuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de tabela `fornecedor`
--
ALTER TABLE `fornecedor`
  MODIFY `idfornecedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `funcionario`
--
ALTER TABLE `funcionario`
  MODIFY `idfuncionario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de tabela `produto`
--
ALTER TABLE `produto`
  MODIFY `codproduto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
