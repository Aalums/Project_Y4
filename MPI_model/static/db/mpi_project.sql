-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 14, 2020 at 11:35 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mpi_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user`
--

CREATE TABLE `accounts_user` (
  `id` int(11) NOT NULL,
  `username` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_user`
--

INSERT INTO `accounts_user` (`id`, `username`, `password`) VALUES
(1, 'phpond', '1234'),
(4, 'aal', '2345');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

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
(25, 'Can add user', 7, 'add_user'),
(26, 'Can change user', 7, 'change_user'),
(27, 'Can delete user', 7, 'delete_user'),
(28, 'Can view user', 7, 'view_user'),
(29, 'Can add patient_characteristic', 8, 'add_patient_characteristic'),
(30, 'Can change patient_characteristic', 8, 'change_patient_characteristic'),
(31, 'Can delete patient_characteristic', 8, 'delete_patient_characteristic'),
(32, 'Can view patient_characteristic', 8, 'view_patient_characteristic'),
(33, 'Can add patients', 9, 'add_patients'),
(34, 'Can change patients', 9, 'change_patients'),
(35, 'Can delete patients', 9, 'delete_patients'),
(36, 'Can view patients', 9, 'view_patients'),
(37, 'Can add patient_mpi', 10, 'add_patient_mpi'),
(38, 'Can change patient_mpi', 10, 'change_patient_mpi'),
(39, 'Can delete patient_mpi', 10, 'delete_patient_mpi'),
(40, 'Can view patient_mpi', 10, 'view_patient_mpi');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$180000$0GHMNFGj27iU$vD7ULuAfcmQorTwgjtYFpHA91qh/NgplJd6M/6AENr0=', '2020-04-14 09:11:46.308633', 1, 'admin', '', '', '', 1, 1, '2020-04-07 15:49:05.018098'),
(2, 'pbkdf2_sha256$180000$RcrCRF7NuHAT$TsmK3DfjaWJ1Gy2vlAAT3DPelUlEBtrE4s/YtWsn+TQ=', '2020-04-14 09:28:29.880379', 0, 'phpond', 'pond', 'pond', '1234@gmail.com', 0, 1, '2020-04-12 15:18:59.000000');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-04-07 15:51:06.208271', '1', 'user object (1)', 1, '[{\"added\": {}}]', 7, 1),
(2, '2020-04-07 16:01:44.823923', '4', 'aal', 1, '[{\"added\": {}}]', 7, 1),
(3, '2020-04-12 15:18:59.235888', '2', 'phpond', 1, '[{\"added\": {}}]', 4, 1),
(4, '2020-04-12 15:19:39.837769', '2', 'phpond', 2, '[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Email address\"]}}]', 4, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'user'),
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'patients', 'patients'),
(8, 'patients', 'patient_characteristic'),
(10, 'patients', 'patient_mpi'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-04-07 15:02:29.312738'),
(2, 'auth', '0001_initial', '2020-04-07 15:02:29.496248'),
(3, 'admin', '0001_initial', '2020-04-07 15:02:30.095724'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-04-07 15:02:30.235388'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-04-07 15:02:30.247357'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-04-07 15:02:30.439256'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-04-07 15:02:30.700145'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-04-07 15:02:30.724087'),
(9, 'auth', '0004_alter_user_username_opts', '2020-04-07 15:02:30.740126'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-04-07 15:02:30.809915'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-04-07 15:02:30.812908'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-04-07 15:02:30.830860'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-04-07 15:02:30.851806'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-04-07 15:02:30.878731'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-04-07 15:02:30.902668'),
(16, 'auth', '0011_update_proxy_permissions', '2020-04-07 15:02:30.915639'),
(17, 'sessions', '0001_initial', '2020-04-07 15:02:30.953531'),
(18, 'accounts', '0001_initial', '2020-04-07 15:50:31.502269'),
(19, 'patients', '0001_initial', '2020-04-12 12:27:51.345166'),
(20, 'patients', '0002_auto_20200414_1552', '2020-04-14 08:52:48.319376');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('o6ysxonbmcrlhqh84m1ztckqumpjusxf', 'OWI1NGIzMjg2MTg4YmJmYWIxNWFmYmE0NGM0M2U4YTlkOGRhMTBjNTp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlZTlhODY4NzQ5NmEyMTBjMmNjYmJmODhhYTkyMTE4Y2M5ZTU4YjI4In0=', '2020-04-28 09:28:29.891556'),
('xpzu1rj011zc1d9im7pwok7tn6auwhew', 'NTY3YjZmODU3ODI1NTc2YzcyMWZlYTA1MzdkMjZkNjAyNzFlYTk1Mzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJkN2M3ZGE1OTI4NGQ3ZjExYjhkNjg3ZWI5ZjQ1MjQxNDE5MjBhMzdmIn0=', '2020-04-21 15:49:14.352200');

-- --------------------------------------------------------

--
-- Table structure for table `patients_patients`
--

CREATE TABLE `patients_patients` (
  `id` int(11) NOT NULL,
  `HN` varchar(9) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `gender` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `patients_patient_characteristic`
--

CREATE TABLE `patients_patient_characteristic` (
  `cha_id` int(11) NOT NULL,
  `cha_date` datetime(6) NOT NULL,
  `bmi` decimal(20,2) NOT NULL,
  `dm` varchar(1) NOT NULL,
  `ht` varchar(1) NOT NULL,
  `dlp` varchar(1) NOT NULL,
  `ckd` varchar(1) NOT NULL,
  `HN_id` int(11) NOT NULL,
  `age` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `patients_patient_mpi`
--

CREATE TABLE `patients_patient_mpi` (
  `mpi_id` int(11) NOT NULL,
  `mpi_date` datetime(6) NOT NULL,
  `LAD_4dmspect` decimal(20,2) NOT NULL,
  `LAD_wallthick` decimal(20,2) NOT NULL,
  `LAD_wallmotion` decimal(20,2) NOT NULL,
  `LAD_CAG` varchar(1) NOT NULL,
  `LCX_4dmspect` decimal(20,2) NOT NULL,
  `LCX_wallthick` decimal(20,2) NOT NULL,
  `LCX_wallmotion` decimal(20,2) NOT NULL,
  `LCX_CAG` varchar(1) NOT NULL,
  `RCA_4dmspect` decimal(20,2) NOT NULL,
  `RCA_wallthick` decimal(20,2) NOT NULL,
  `RCA_wallmotion` decimal(20,2) NOT NULL,
  `RCA_CAG` varchar(1) NOT NULL,
  `LVEF` int(11) NOT NULL,
  `HN_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_user`
--
ALTER TABLE `accounts_user`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `patients_patients`
--
ALTER TABLE `patients_patients`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patients_patient_characteristic`
--
ALTER TABLE `patients_patient_characteristic`
  ADD PRIMARY KEY (`cha_id`),
  ADD KEY `patients_patient_cha_HN_id_ec5f6881_fk_patients_` (`HN_id`);

--
-- Indexes for table `patients_patient_mpi`
--
ALTER TABLE `patients_patient_mpi`
  ADD PRIMARY KEY (`mpi_id`),
  ADD KEY `patients_patient_mpi_HN_id_765e6c69_fk_patients_patients_id` (`HN_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_user`
--
ALTER TABLE `accounts_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `patients_patients`
--
ALTER TABLE `patients_patients`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `patients_patient_characteristic`
--
ALTER TABLE `patients_patient_characteristic`
  MODIFY `cha_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `patients_patient_mpi`
--
ALTER TABLE `patients_patient_mpi`
  MODIFY `mpi_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `patients_patient_characteristic`
--
ALTER TABLE `patients_patient_characteristic`
  ADD CONSTRAINT `patients_patient_cha_HN_id_ec5f6881_fk_patients_` FOREIGN KEY (`HN_id`) REFERENCES `patients_patients` (`id`);

--
-- Constraints for table `patients_patient_mpi`
--
ALTER TABLE `patients_patient_mpi`
  ADD CONSTRAINT `patients_patient_mpi_HN_id_765e6c69_fk_patients_patients_id` FOREIGN KEY (`HN_id`) REFERENCES `patients_patients` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
