show databases;

use bank_management_system;


DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `acno` int(12) NOT NULL AUTO_INCREMENT,
  `name` char(30) DEFAULT  NULL,
  `address` varchar(100) DEFAULT  NULL,
  `phone` varchar(15) DEFAULT  NULL ,
  `email` varchar(80) DEFAULT  NULL,
  `aadhar_no` varchar(20) DEFAULT  NULL,
  `acc_type` varchar(20) DEFAULT  NULL,
  `status` char(15) DEFAULT NULL,
  `balance` float(15,2) DEFAULT  NULL,
  PRIMARY KEY (`acno`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`acno`, `name`, `address`, `phone`, `email`, `aadhar_no`, `acc_type`, `status`, `balance`) VALUES
(1, 'Kartikay Patni', 'HsNo.458 takana road Pithoragarh', '8534814236', 'kartikpatni729@gmail.com', '9107-6038-5851', 'saving', 'active', 775455.09),
(2, 'Harsh Singh Kharayat', 'Naya Bazar', '9673434431', 'harsh@gmail.com', '4545-1243-4545', 'current', 'active', 762935.00),
(3, 'Elvin Singh Dungriyal ', 'New Bajeti ', '9867345124', 'elvin@gmailcom.com', '1234-5656-4545', 'saving', 'active', 812524.00),
(4, 'ashutosh', 'd-100 brij vihar', '1122334455', 'ashu@gmail.com', '1124-5656-6576', 'saving', 'close', 56000.00),
(5, 'raman singh', 'e-40 radha bihar', '3344556677', 'raman@yahoo.com', '4455-5656-4545', 'saving', 'close', 20000.00),
(6, 'sam', 'f-12 surya nagar', '1234', 'sam@gmail.com', '1234-4556-5656', 'saving', 'active', 22000.00);

-- --------------------------------------------------------

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
CREATE TABLE IF NOT EXISTS `transaction` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `amount` int(10) DEFAULT NULL,
  `type` char(20) DEFAULT NULL,
  `acno` int(10) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transaction`
--

INSERT INTO `transaction` (`tid`, `date`, `amount`, `type`, `acno`) VALUES
(1, '2022-1-16', 2000, 'deposit', 1),
(2, '2022-1-15', 2000, 'deposit', 2),
(3, '2022-1-18', 1200, 'withdraw', 1),
(4, '2022-1-24', 2000, 'deposit', 1),
(5, '2022-1-30', 200, 'deposit', 1),
(6, '2022-2-30', 2000, 'withdraw', 1),
(7, '2022-1-30', 200, 'withdraw', 1),
(8, '2022-2-01', 2000, 'deposit', 6);
COMMIT


