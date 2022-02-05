/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80012
Source Host           : localhost:3306
Source Database       : vega

Target Server Type    : MYSQL
Target Server Version : 80012
File Encoding         : 65001

Date: 2020-05-24 18:59:04
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
  `state` enum('草稿','待审批','已审批','隐藏') NOT NULL,
  PRIMARY KEY (`id`),
  KEY `editor_id` (`editor_id`),
  KEY `type_id` (`type_id`),
  KEY `state` (`state`),
  KEY `create_time` (`create_time`),
  KEY `is_top` (`is_top`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_news
-- ----------------------------
INSERT INTO `t_news` VALUES ('1', '新闻标题1', '2', '1', '1', '1', '2018-11-22 18:55:56', '2018-11-22 18:55:56', '待审批');
INSERT INTO `t_news` VALUES ('2', '新闻标题2', '1', '3', '1', '1', '2020-05-24 17:18:31', '2020-05-24 17:18:31', '待审批');
INSERT INTO `t_news` VALUES ('3', '新闻标题3', '2', '4', '1', '1', '2020-05-24 18:10:56', '2020-05-24 18:10:56', '待审批');
INSERT INTO `t_news` VALUES ('4', '新闻标题4', '2', '4', '1', '1', '2020-05-24 18:10:57', '2020-05-24 18:10:57', '待审批');
INSERT INTO `t_news` VALUES ('5', '新闻标题5', '2', '4', '1', '1', '2020-05-24 18:10:58', '2020-05-24 18:10:58', '待审批');
INSERT INTO `t_news` VALUES ('6', '新闻标题6', '2', '4', '1', '1', '2020-05-24 18:10:58', '2020-05-24 18:10:58', '待审批');
INSERT INTO `t_news` VALUES ('7', '新闻标题7', '2', '1', '1', '1', '2020-05-24 18:10:58', '2020-05-24 18:10:58', '待审批');
INSERT INTO `t_news` VALUES ('8', '新闻标题8', '2', '4', '1', '1', '2020-05-24 18:10:59', '2020-05-24 18:10:59', '待审批');
INSERT INTO `t_news` VALUES ('9', '新闻标题9', '2', '4', '1', '1', '2020-05-24 18:10:59', '2020-05-24 18:10:59', '待审批');
INSERT INTO `t_news` VALUES ('10', '新闻标题10', '2', '4', '1', '1', '2020-05-24 18:10:59', '2020-05-24 18:10:59', '待审批');
INSERT INTO `t_news` VALUES ('11', '新闻标题11', '2', '4', '1', '1', '2020-05-24 18:10:59', '2020-05-24 18:10:59', '待审批');
INSERT INTO `t_news` VALUES ('12', '新闻标题12', '2', '5', '1', '1', '2020-05-24 18:10:59', '2020-05-24 18:10:59', '已审批');
INSERT INTO `t_news` VALUES ('13', '新闻标题13', '2', '4', '1', '1', '2020-05-24 18:10:59', '2020-05-24 18:10:59', '待审批');
INSERT INTO `t_news` VALUES ('14', '新闻标题14', '2', '4', '1', '1', '2020-05-24 18:10:59', '2020-05-24 18:10:59', '待审批');
INSERT INTO `t_news` VALUES ('15', '新闻标题15', '2', '4', '1', '1', '2020-05-24 18:11:00', '2020-05-24 18:11:00', '已审批');
INSERT INTO `t_news` VALUES ('16', '新闻标题16', '2', '4', '1', '1', '2020-05-24 18:11:00', '2020-05-24 18:11:00', '待审批');
INSERT INTO `t_news` VALUES ('17', '新闻标题17', '2', '4', '1', '1', '2020-05-24 18:11:00', '2020-05-24 18:11:00', '待审批');
INSERT INTO `t_news` VALUES ('18', '新闻标题18', '2', '4', '1', '1', '2020-05-24 18:11:00', '2020-05-24 18:11:00', '待审批');
INSERT INTO `t_news` VALUES ('19', '新闻标题19', '2', '4', '1', '1', '2020-05-24 18:11:01', '2020-05-24 18:11:01', '已审批');
INSERT INTO `t_news` VALUES ('20', '新闻标题20', '2', '4', '1', '1', '2020-05-24 18:11:01', '2020-05-24 18:11:01', '已审批');
INSERT INTO `t_news` VALUES ('21', '新闻标题21', '2', '4', '1', '1', '2020-05-24 18:11:01', '2020-05-24 18:11:01', '已审批');
INSERT INTO `t_news` VALUES ('22', '新闻标题22', '2', '4', '1', '1', '2020-05-24 18:11:01', '2020-05-24 18:11:01', '已审批');
INSERT INTO `t_news` VALUES ('23', '新闻标题23', '2', '4', '1', '1', '2020-05-24 18:11:01', '2020-05-24 18:11:01', '已审批');
INSERT INTO `t_news` VALUES ('24', '新闻标题24', '2', '4', '1', '1', '2020-05-24 18:11:08', '2020-05-24 18:11:08', '已审批');
INSERT INTO `t_news` VALUES ('25', '新闻标题25', '2', '4', '1', '1', '2020-05-24 18:11:08', '2020-05-24 18:11:08', '已审批');
INSERT INTO `t_news` VALUES ('26', '新闻标题26', '2', '4', '1', '1', '2020-05-24 18:11:08', '2020-05-24 18:11:08', '已审批');
