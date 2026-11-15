-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 04, 2025 at 03:39 PM
-- Server version: 5.7.36
-- PHP Version: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_careersync`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_companytype`
--

DROP TABLE IF EXISTS `adminapp_tbl_companytype`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_companytype` (
  `companytypeid` int(11) NOT NULL AUTO_INCREMENT,
  `companytypename` varchar(25) NOT NULL,
  PRIMARY KEY (`companytypeid`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_companytype`
--

INSERT INTO `adminapp_tbl_companytype` (`companytypeid`, `companytypename`) VALUES
(1, 'IT'),
(5, 'Business'),
(6, 'Manufacturing ');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_district`
--

DROP TABLE IF EXISTS `adminapp_tbl_district`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_district` (
  `districtid` int(11) NOT NULL AUTO_INCREMENT,
  `districtname` varchar(25) NOT NULL,
  PRIMARY KEY (`districtid`)
) ENGINE=MyISAM AUTO_INCREMENT=415 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_district`
--

INSERT INTO `adminapp_tbl_district` (`districtid`, `districtname`) VALUES
(4, 'Kozhikode'),
(3, 'Wayanad'),
(2, 'Kannur'),
(1, 'Kasaragod'),
(5, 'Malappuram'),
(7, 'Thrissur'),
(8, 'Ernakulam'),
(9, 'Idukki'),
(10, 'Kottayam'),
(11, 'Alappuzha'),
(12, 'Pathanamthitta'),
(13, 'Kollam');

-- --------------------------------------------------------

--
-- Table structure for table `adminapp_tbl_location`
--

DROP TABLE IF EXISTS `adminapp_tbl_location`;
CREATE TABLE IF NOT EXISTS `adminapp_tbl_location` (
  `locationid` int(11) NOT NULL AUTO_INCREMENT,
  `locationname` varchar(25) NOT NULL,
  `districtid_id` int(11) NOT NULL,
  PRIMARY KEY (`locationid`),
  KEY `adminapp_tbl_location_districtid_id_582f66a5` (`districtid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `adminapp_tbl_location`
--

INSERT INTO `adminapp_tbl_location` (`locationid`, `locationname`, `districtid_id`) VALUES
(1, 'Vazhithala', 9),
(2, 'Thodupuzha', 9);

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add tbl_login', 7, 'add_tbl_login'),
(26, 'Can change tbl_login', 7, 'change_tbl_login'),
(27, 'Can delete tbl_login', 7, 'delete_tbl_login'),
(28, 'Can view tbl_login', 7, 'view_tbl_login'),
(29, 'Can add tbl_location', 8, 'add_tbl_location'),
(30, 'Can change tbl_location', 8, 'change_tbl_location'),
(31, 'Can delete tbl_location', 8, 'delete_tbl_location'),
(32, 'Can view tbl_location', 8, 'view_tbl_location'),
(33, 'Can add tbl_district', 9, 'add_tbl_district'),
(34, 'Can change tbl_district', 9, 'change_tbl_district'),
(35, 'Can delete tbl_district', 9, 'delete_tbl_district'),
(36, 'Can view tbl_district', 9, 'view_tbl_district'),
(37, 'Can add tbl_companytype', 10, 'add_tbl_companytype'),
(38, 'Can change tbl_companytype', 10, 'change_tbl_companytype'),
(39, 'Can delete tbl_companytype', 10, 'delete_tbl_companytype'),
(40, 'Can view tbl_companytype', 10, 'view_tbl_companytype'),
(41, 'Can add tbl_login', 11, 'add_tbl_login'),
(42, 'Can change tbl_login', 11, 'change_tbl_login'),
(43, 'Can delete tbl_login', 11, 'delete_tbl_login'),
(44, 'Can view tbl_login', 11, 'view_tbl_login'),
(45, 'Can add tbl_company', 12, 'add_tbl_company'),
(46, 'Can change tbl_company', 12, 'change_tbl_company'),
(47, 'Can delete tbl_company', 12, 'delete_tbl_company'),
(48, 'Can view tbl_company', 12, 'view_tbl_company'),
(49, 'Can add tbl_college', 13, 'add_tbl_college'),
(50, 'Can change tbl_college', 13, 'change_tbl_college'),
(51, 'Can delete tbl_college', 13, 'delete_tbl_college'),
(52, 'Can view tbl_college', 13, 'view_tbl_college'),
(53, 'Can add tbl_student', 14, 'add_tbl_student'),
(54, 'Can change tbl_student', 14, 'change_tbl_student'),
(55, 'Can delete tbl_student', 14, 'delete_tbl_student'),
(56, 'Can view tbl_student', 14, 'view_tbl_student'),
(57, 'Can add tbl_internship', 15, 'add_tbl_internship'),
(58, 'Can change tbl_internship', 15, 'change_tbl_internship'),
(59, 'Can delete tbl_internship', 15, 'delete_tbl_internship'),
(60, 'Can view tbl_internship', 15, 'view_tbl_internship');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `companyapp_tbl_internship`
--

DROP TABLE IF EXISTS `companyapp_tbl_internship`;
CREATE TABLE IF NOT EXISTS `companyapp_tbl_internship` (
  `internshipid` int(11) NOT NULL AUTO_INCREMENT,
  `internshipname` varchar(100) NOT NULL,
  `syllabus` varchar(100) NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `duration` bigint(20) NOT NULL,
  `description` longtext NOT NULL,
  `companyid_id` int(11) NOT NULL,
  PRIMARY KEY (`internshipid`),
  KEY `companyapp_tbl_internship_companyid_id_cef811cc` (`companyid_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'adminapp', 'tbl_login'),
(8, 'adminapp', 'tbl_location'),
(9, 'adminapp', 'tbl_district'),
(10, 'adminapp', 'tbl_companytype'),
(11, 'guestapp', 'tbl_login'),
(12, 'guestapp', 'tbl_company'),
(13, 'guestapp', 'tbl_college'),
(14, 'guestapp', 'tbl_student'),
(15, 'companyapp', 'tbl_internship');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-01-14 10:47:18.223838'),
(2, 'auth', '0001_initial', '2025-01-14 10:47:18.359824'),
(3, 'admin', '0001_initial', '2025-01-14 10:47:18.396055'),
(4, 'admin', '0002_logentry_remove_auto_add', '2025-01-14 10:47:18.405362'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2025-01-14 10:47:18.412897'),
(6, 'adminapp', '0001_initial', '2025-01-14 10:47:18.421276'),
(7, 'contenttypes', '0002_remove_content_type_name', '2025-01-14 10:47:18.453970'),
(8, 'auth', '0002_alter_permission_name_max_length', '2025-01-14 10:47:18.472207'),
(9, 'auth', '0003_alter_user_email_max_length', '2025-01-14 10:47:18.489383'),
(10, 'auth', '0004_alter_user_username_opts', '2025-01-14 10:47:18.498415'),
(11, 'auth', '0005_alter_user_last_login_null', '2025-01-14 10:47:18.513645'),
(12, 'auth', '0006_require_contenttypes_0002', '2025-01-14 10:47:18.517421'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2025-01-14 10:47:18.525794'),
(14, 'auth', '0008_alter_user_username_max_length', '2025-01-14 10:47:18.543547'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2025-01-14 10:47:18.561313'),
(16, 'auth', '0010_alter_group_name_max_length', '2025-01-14 10:47:18.577910'),
(17, 'auth', '0011_update_proxy_permissions', '2025-01-14 10:47:18.588812'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2025-01-14 10:47:18.605282'),
(19, 'sessions', '0001_initial', '2025-01-14 10:47:18.620917'),
(20, 'adminapp', '0002_tbl_district_tbl_location', '2025-01-14 11:02:37.019336'),
(21, 'adminapp', '0003_tbl_companytype_delete_tbl_login', '2025-01-15 10:43:47.959875'),
(22, 'guestapp', '0001_initial', '2025-01-15 15:20:39.750802'),
(23, 'guestapp', '0002_tbl_company', '2025-01-20 08:41:53.874384'),
(24, 'guestapp', '0003_tbl_college', '2025-01-22 15:47:37.562496'),
(26, 'guestapp', '0004_tbl_student', '2025-01-22 17:20:23.331964'),
(27, 'companyapp', '0001_initial', '2025-02-03 14:07:12.997962');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('xoha4ddacyw70pe4il03u9dlujstpl7n', 'eyJsb2dpbklkIjoyM30:1tfKSq:Hi8YL9NkZFCfJL6DyEkjMbkBOXa3SfQBRsk4cqgRJ40', '2025-02-18 15:03:48.305613');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_college`
--

DROP TABLE IF EXISTS `guestapp_tbl_college`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_college` (
  `collegeid` int(11) NOT NULL AUTO_INCREMENT,
  `collegename` varchar(100) NOT NULL,
  `collegeemail` varchar(100) NOT NULL,
  `collegecontact` bigint(20) NOT NULL,
  `collegewebsiteurl` varchar(200) NOT NULL,
  `locationid_id` int(11) NOT NULL,
  `loginid_id` int(11) NOT NULL,
  PRIMARY KEY (`collegeid`),
  UNIQUE KEY `collegeemail` (`collegeemail`),
  KEY `guestapp_tbl_college_locationid_id_c34834ce` (`locationid_id`),
  KEY `guestapp_tbl_college_loginid_id_91a68b2c` (`loginid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_college`
--

INSERT INTO `guestapp_tbl_college` (`collegeid`, `collegename`, `collegeemail`, `collegecontact`, `collegewebsiteurl`, `locationid_id`, `loginid_id`) VALUES
(1, 'aaaaaaaaaaaaaaaa', 'aaaaaaaaaaaaaa', 111111111111111, 'eeeeeeeeeeeeeeee', 1, 15),
(2, 'Ilahia', 'ajmalanas97314@gmail.com', 1239874560, 'aaaaaaaaa', 2, 25),
(3, 'Nirmala', 'nirmala@gmail.com', 1478523690, 'dddddddddd', 1, 26);

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_company`
--

DROP TABLE IF EXISTS `guestapp_tbl_company`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_company` (
  `companyid` int(11) NOT NULL AUTO_INCREMENT,
  `companyname` varchar(100) NOT NULL,
  `companylogo` varchar(100) NOT NULL,
  `companyemail` varchar(100) NOT NULL,
  `companycontact` bigint(20) NOT NULL,
  `companywebsiteurl` varchar(200) NOT NULL,
  `companytypeid_id` int(11) NOT NULL,
  `locationid_id` int(11) NOT NULL,
  `loginid_id` int(11) NOT NULL,
  PRIMARY KEY (`companyid`),
  UNIQUE KEY `companyemail` (`companyemail`),
  KEY `guestapp_tbl_company_companytypeid_id_21f17776` (`companytypeid_id`),
  KEY `guestapp_tbl_company_locationid_id_657881e8` (`locationid_id`),
  KEY `guestapp_tbl_company_loginid_id_d66faff3` (`loginid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_company`
--

INSERT INTO `guestapp_tbl_company` (`companyid`, `companyname`, `companylogo`, `companyemail`, `companycontact`, `companywebsiteurl`, `companytypeid_id`, `locationid_id`, `loginid_id`) VALUES
(1, 'Wiproooooo', 'Screenshot (1).png', 'ajmal92755@gmail.com', 1234666666, 'uuuuuu', 1, 1, 2),
(2, 'Wipro', 'Screenshot (1).png', 'aaa@gmail.com', 1234666667, 'qqq', 1, 2, 23),
(3, 'TCS', 'Screenshot (1).png', 'company2123@gmail.com', 1245639851, 'aaaaaaaaa', 1, 2, 24),
(4, 'JTSI', 'Screenshot_2.png', 'jtsi@gmail.com', 2345678976, 'jtsi.ac.in', 1, 1, 32),
(5, 'UrbanStyle Goods', 'Screenshot_2.png', 'urbanstyle@gmail.com', 4578963258, 'urbanstyle.ac.in', 5, 2, 34),
(6, 'RetailX Innovations', 'Screenshot_2024-08-11_180052.png', 'retailxinnovations@gmail.com', 1452368907, 'retailxinnovations.ac.in', 5, 2, 35),
(7, 'TechnoCraft Industries', 'logo_technocraft.png', 'technocraftindustries@gmail.com', 7534218690, 'technocraftindustries.ac.in', 6, 2, 36),
(8, 'NextGen Fabricators', '.png', 'nextgenfabricators@gmail.com', 478932516, 'nextgenfabricators.ac.in', 6, 2, 37);

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_login`
--

DROP TABLE IF EXISTS `guestapp_tbl_login`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_login` (
  `loginid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `role` varchar(25) NOT NULL,
  `status` varchar(25) NOT NULL,
  PRIMARY KEY (`loginid`)
) ENGINE=MyISAM AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_login`
--

INSERT INTO `guestapp_tbl_login` (`loginid`, `username`, `password`, `role`, `status`) VALUES
(1, 'admin', 'admin', 'admin', 'confirmed'),
(30, 'pppp', 'pppp', 'company', 'requested'),
(23, 'wipro', 'wipro', 'company', 'Confirmed'),
(26, 'nirmala123', 'nirmala@123', 'college', 'Confirmed'),
(28, 'iiuuu', 'dttt', 'company', 'requested'),
(29, 'iiiiii', 'iiiiiii', 'company', 'requested'),
(25, 'ilahia123', 'ilahia@123', 'college', 'Reject'),
(24, 'tcs', 'tcs', 'company', 'requested'),
(31, 'abc', 'abc', 'company', 'requested'),
(32, 'jtsi123', 'jtsi@123', 'company', 'requested'),
(33, 'mariya', 'mariya', 'student', 'confirmed'),
(34, 'urbanstyle', 'urbanstyle', 'company', 'requested'),
(35, 'RetailXInnovations', 'RetailXInnovations', 'company', 'requested'),
(36, 'TechnoCraftIndustries', 'TechnoCraftIndustries', 'company', 'requested'),
(37, 'NextGenFabricators', 'NextGenFabricators', 'company', 'requested');

-- --------------------------------------------------------

--
-- Table structure for table `guestapp_tbl_student`
--

DROP TABLE IF EXISTS `guestapp_tbl_student`;
CREATE TABLE IF NOT EXISTS `guestapp_tbl_student` (
  `studentid` int(11) NOT NULL AUTO_INCREMENT,
  `studentname` varchar(100) NOT NULL,
  `studentemail` varchar(100) NOT NULL,
  `studentcontact` bigint(20) NOT NULL,
  `studentdateofbirth` date NOT NULL,
  `collegename` varchar(100) NOT NULL,
  `course` varchar(100) NOT NULL,
  `sem` bigint(20) NOT NULL,
  `locationid_id` int(11) NOT NULL,
  `loginid_id` int(11) NOT NULL,
  PRIMARY KEY (`studentid`),
  UNIQUE KEY `studentemail` (`studentemail`),
  KEY `guestapp_tbl_student_locationid_id_7487e626` (`locationid_id`),
  KEY `guestapp_tbl_student_loginid_id_36daab86` (`loginid_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `guestapp_tbl_student`
--

INSERT INTO `guestapp_tbl_student` (`studentid`, `studentname`, `studentemail`, `studentcontact`, `studentdateofbirth`, `collegename`, `course`, `sem`, `locationid_id`, `loginid_id`) VALUES
(5, 'mariya', 'mariya@gmail.com', 552689565, '2025-06-17', 'Santhigiri', 'MCA', 6, 2, 33);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
