/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80012
Source Host           : localhost:3306
Source Database       : vega_english

Target Server Type    : MYSQL
Target Server Version : 80012
File Encoding         : 65001

Date: 2020-05-25 20:01:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_news
-- ----------------------------
DROP TABLE IF EXISTS `t_news`;
CREATE TABLE `t_news` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(40) NOT NULL,
  `editor_id` int(10) unsigned NOT NULL,
  `type_id` int(10) unsigned NOT NULL,
  `content_id` char(12) NOT NULL,
  `is_top` tinyint(3) unsigned NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `state` enum('Draft','Pending','Approved','Invisible') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `editor_id` (`editor_id`),
  KEY `type_id` (`type_id`),
  KEY `state` (`state`),
  KEY `create_time` (`create_time`),
  KEY `is_top` (`is_top`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_news
-- ----------------------------
INSERT INTO `t_news` VALUES ('1', 'TITLE1', '1', '1', '1', '1', '2020-05-25 14:27:52', '2020-05-25 14:27:52', 'Pending');
INSERT INTO `t_news` VALUES ('2', 'TITLE2', '2', '1', '1', '1', '2020-05-25 14:29:56', '2020-05-25 14:29:56', 'Pending');
INSERT INTO `t_news` VALUES ('3', 'TITLE3', '1', '4', '1', '1', '2020-05-25 14:29:56', '2020-05-25 14:29:56', 'Pending');
INSERT INTO `t_news` VALUES ('4', 'TITLE4', '2', '2', '1', '1', '2020-05-25 14:29:56', '2020-05-25 14:29:56', 'Pending');
INSERT INTO `t_news` VALUES ('5', 'TITLE5', '1', '3', '1', '1', '2020-05-25 14:29:56', '2020-05-25 14:29:56', 'Pending');
INSERT INTO `t_news` VALUES ('6', 'TITLE6', '2', '5', '1', '1', '2020-05-25 14:29:56', '2020-05-25 14:29:56', 'Pending');
INSERT INTO `t_news` VALUES ('7', 'TITLE7', '1', '1', '1', '1', '2020-05-25 14:29:56', '2020-05-25 14:29:56', 'Pending');
INSERT INTO `t_news` VALUES ('8', 'TITLE8', '2', '4', '1', '1', '2020-05-25 14:29:56', '2020-05-25 14:29:56', 'Pending');
INSERT INTO `t_news` VALUES ('9', 'TITLE9', '1', '2', '1', '1', '2020-05-25 14:29:56', '2020-05-25 14:29:56', 'Pending');
INSERT INTO `t_news` VALUES ('10', 'TITLE10', '3', '3', '1', '1', '2020-05-25 14:29:56', '2020-05-25 14:29:56', 'Pending');
INSERT INTO `t_news` VALUES ('11', 'TITLE11', '1', '5', '1', '1', '2020-05-25 14:29:56', '2020-05-25 14:29:56', 'Pending');
INSERT INTO `t_news` VALUES ('12', 'TITLE12', '2', '1', '1', '1', '2020-05-25 14:30:24', '2020-05-25 14:30:24', 'Pending');
INSERT INTO `t_news` VALUES ('13', 'TITLE13', '1', '4', '1', '1', '2020-05-25 14:30:24', '2020-05-25 14:30:24', 'Pending');
INSERT INTO `t_news` VALUES ('14', 'TITLE14', '2', '2', '1', '1', '2020-05-25 14:30:24', '2020-05-25 14:30:24', 'Pending');
INSERT INTO `t_news` VALUES ('15', 'TITLE15', '1', '3', '1', '1', '2020-05-25 14:30:24', '2020-05-25 14:30:24', 'Pending');
INSERT INTO `t_news` VALUES ('16', 'TITLE16', '2', '5', '1', '1', '2020-05-25 14:30:24', '2020-05-25 14:30:24', 'Pending');
INSERT INTO `t_news` VALUES ('17', 'TITLE17', '1', '1', '1', '1', '2020-05-25 14:30:24', '2020-05-25 14:30:24', 'Pending');
INSERT INTO `t_news` VALUES ('18', 'TITLE18', '2', '4', '1', '1', '2020-05-25 14:30:24', '2020-05-25 14:30:24', 'Pending');
INSERT INTO `t_news` VALUES ('19', 'TITLE19', '1', '2', '1', '1', '2020-05-25 14:30:24', '2020-05-25 14:30:24', 'Pending');
INSERT INTO `t_news` VALUES ('20', 'TITLE20', '3', '3', '1', '1', '2020-05-25 14:30:24', '2020-05-25 14:30:24', 'Pending');
INSERT INTO `t_news` VALUES ('21', 'TITLE21', '1', '5', '1', '1', '2020-05-25 14:30:24', '2020-05-25 14:30:24', 'Pending');

-- ----------------------------
-- Table structure for t_role
-- ----------------------------
DROP TABLE IF EXISTS `t_role`;
CREATE TABLE `t_role` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `role` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `role` (`role`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_role
-- ----------------------------
INSERT INTO `t_role` VALUES ('1', 'Administrator');
INSERT INTO `t_role` VALUES ('2', 'News Editor');

-- ----------------------------
-- Table structure for t_type
-- ----------------------------
DROP TABLE IF EXISTS `t_type`;
CREATE TABLE `t_type` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `type` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type` (`type`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_type
-- ----------------------------
INSERT INTO `t_type` VALUES ('4', 'Entertainment News');
INSERT INTO `t_type` VALUES ('5', 'History News');
INSERT INTO `t_type` VALUES ('1', 'Important News');
INSERT INTO `t_type` VALUES ('2', 'Sports News');
INSERT INTO `t_type` VALUES ('3', 'Tech News');

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) NOT NULL,
  `password` varchar(500) NOT NULL,
  `email` varchar(100) NOT NULL,
  `role_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  KEY `username_2` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_user
-- ----------------------------
INSERT INTO `t_user` VALUES ('1', 'admin', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'admin@gmail.com', '1');
INSERT INTO `t_user` VALUES ('2', 'scott', '3E6BC27A781F0AC08BCFD78CC3DCE4CA', 'scott@gmail.com', '1');
