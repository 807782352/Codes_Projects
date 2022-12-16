/*
 Navicat Premium Data Transfer

 Source Server         : Tripedia
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : database-tripedia.chn0lcgtnjar.us-east-1.rds.amazonaws.com:3306
 Source Schema         : tripedia

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 15/12/2022 23:43:24
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment`  (
  `comment_id` bigint(0) NOT NULL,
  `comment_date` datetime(6) NOT NULL,
  `comment_text` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `post_id` bigint(0) NULL DEFAULT NULL,
  `user_id` bigint(0) NULL DEFAULT NULL,
  PRIMARY KEY (`comment_id`) USING BTREE,
  INDEX `FKs1slvnkuemjsq2kj4h3vhx7i1`(`post_id`) USING BTREE,
  INDEX `FK8kcum44fvpupyw6f5baccx25c`(`user_id`) USING BTREE,
  CONSTRAINT `FK8kcum44fvpupyw6f5baccx25c` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FKs1slvnkuemjsq2kj4h3vhx7i1` FOREIGN KEY (`post_id`) REFERENCES `post` (`post_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of comment
-- ----------------------------

-- ----------------------------
-- Table structure for hibernate_sequence
-- ----------------------------
DROP TABLE IF EXISTS `hibernate_sequence`;
CREATE TABLE `hibernate_sequence`  (
  `next_val` bigint(0) NULL DEFAULT NULL
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of hibernate_sequence
-- ----------------------------
INSERT INTO `hibernate_sequence` VALUES (9);
INSERT INTO `hibernate_sequence` VALUES (15);

-- ----------------------------
-- Table structure for image
-- ----------------------------
DROP TABLE IF EXISTS `image`;
CREATE TABLE `image`  (
  `image_id` bigint(0) NOT NULL,
  `image_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `post_id` bigint(0) NULL DEFAULT NULL,
  `spot_id` bigint(0) NULL DEFAULT NULL,
  `user_id` bigint(0) NULL DEFAULT NULL,
  PRIMARY KEY (`image_id`) USING BTREE,
  INDEX `FKe2l07hc93u2bbjnl80meu3rn4`(`post_id`) USING BTREE,
  INDEX `FKd8iofq9x7700ohcmct1cbsyj4`(`spot_id`) USING BTREE,
  INDEX `FKlxnnh0ir05khn8iu9tgwh1yyk`(`user_id`) USING BTREE,
  CONSTRAINT `FKd8iofq9x7700ohcmct1cbsyj4` FOREIGN KEY (`spot_id`) REFERENCES `spot` (`spot_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FKe2l07hc93u2bbjnl80meu3rn4` FOREIGN KEY (`post_id`) REFERENCES `post` (`post_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FKlxnnh0ir05khn8iu9tgwh1yyk` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of image
-- ----------------------------
INSERT INTO `image` VALUES (1, 'https://www.banfftours.com/wp-content/uploads/2017/08/Banff-Ave-and-Town-in-Winter-1140x530.jpg', 1, 1, 1);
INSERT INTO `image` VALUES (2, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/13/26/38/ripley-s-aquarium-of.jpg?w=1200&h=-1&s=1', 1, 1, 1);
INSERT INTO `image` VALUES (3, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/06/0b/ca/df/coral-and-color.jpg?w=1100&h=-1&s=1', 2, 1, 2);
INSERT INTO `image` VALUES (4, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/05/e3/e6/58/ripley-s-aquarium-of.jpg?w=1200&h=-1&s=1', 3, 1, 3);
INSERT INTO `image` VALUES (5, 'https://dynamic-media-cdn.tripadvisor.com/media/daodao/photo-o/10/9d/ed/bb/caption.jpg?w=1200&h=-1&s=1', 4, 2, 3);
INSERT INTO `image` VALUES (6, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/10/7a/7f/df/photo1jpg.jpg?w=1200&h=-1&s=1', 5, 2, 4);
INSERT INTO `image` VALUES (7, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/10/76/ae/ad/photo0jpg.jpg?w=1200&h=-1&s=1', 5, 2, 4);
INSERT INTO `image` VALUES (8, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/10/75/3b/18/photo1jpg.jpg?w=1200&h=-1&s=1', 6, 2, 5);
INSERT INTO `image` VALUES (9, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/1c/53/c6/monte-royal.jpg?w=1200&h=-1&s=1', 7, 3, 1);
INSERT INTO `image` VALUES (10, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/1c/53/c3/monte-royal.jpg?w=1200&h=-1&s=1', 7, 3, 1);
INSERT INTO `image` VALUES (11, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/19/02/fd/photo0jpg.jpg?w=1200&h=-1&s=1', 8, 3, 2);
INSERT INTO `image` VALUES (12, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/11/11/73/8f/parc.jpg?w=1200&h=-1&s=1', 8, 3, 2);
INSERT INTO `image` VALUES (13, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/4f/cf/de/interior-from-the-main.jpg?w=1200&h=-1&s=1', 9, 4, 3);
INSERT INTO `image` VALUES (14, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1b/4f/cf/dd/view-from-the-place-d.jpg?w=1200&h=-1&s=1', 10, 4, 5);
INSERT INTO `image` VALUES (15, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/18/ec/69/97/notre-dame-basilica.jpg?w=1200&h=-1&s=1', 10, 4, 5);
INSERT INTO `image` VALUES (16, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/16/b0/c2/7b/view.jpg?w=1200&h=-1&s=1', 10, 4, 5);
INSERT INTO `image` VALUES (17, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/08/63/00/14/lake-minnewanka.jpg?w=1200&h=-1&s=1', 11, 5, 2);
INSERT INTO `image` VALUES (18, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/01/ed/b5/d1/bow-falls.jpg?w=1100&h=-1&s=1', 11, 5, 2);
INSERT INTO `image` VALUES (19, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/12/be/4b/83/photo4jpg.jpg?w=1200&h=-1&s=1', 12, 5, 3);
INSERT INTO `image` VALUES (20, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/00/a5/05/bird-s-eye-view-of-banff.jpg?w=1200&h=-1&s=1', 12, 5, 3);
INSERT INTO `image` VALUES (21, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/12/79/14/ca/sightseeing-at-vermilion.jpg?w=1200&h=-1&s=1', 13, 5, 4);
INSERT INTO `image` VALUES (22, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/ab/44/45/banff-avenue-in-winter.jpg?w=1200&h=-1&s=1', 14, 5, 5);
INSERT INTO `image` VALUES (23, 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0a/ab/40/b4/town-of-banff-at-night.jpg?w=1200&h=-1&s=1', 14, 5, 5);

-- ----------------------------
-- Table structure for post
-- ----------------------------
DROP TABLE IF EXISTS `post`;
CREATE TABLE `post`  (
  `post_id` bigint(0) NOT NULL,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `cost` bigint(0) NULL DEFAULT NULL,
  `is_brief` bit(1) NOT NULL,
  `post_time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `trip_time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `visitor_num` bigint(0) NULL DEFAULT NULL,
  `spot_id` bigint(0) NULL DEFAULT NULL,
  `user_id` bigint(0) NULL DEFAULT NULL,
  PRIMARY KEY (`post_id`) USING BTREE,
  UNIQUE INDEX `UK_2jm25hjrq6iv4w8y1dhi0d9p4`(`title`) USING BTREE,
  INDEX `FKqng73nkpy18qx7h7k6wq87ygx`(`spot_id`) USING BTREE,
  INDEX `FK72mt33dhhs48hf9gcqrq4fxte`(`user_id`) USING BTREE,
  CONSTRAINT `FK72mt33dhhs48hf9gcqrq4fxte` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `FKqng73nkpy18qx7h7k6wq87ygx` FOREIGN KEY (`spot_id`) REFERENCES `spot` (`spot_id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of post
-- ----------------------------
INSERT INTO `post` VALUES (1, 'Here is my full and honest review (including tips) of Ripley\'s Aquarium as I experienced it on December 30, 2013: *Buying tickets ahead of time: The website has 2 options for ticket purchases, either an \"anytime\" ticket or a \"reserved time\" ticket, so I c', 30, b'0', NULL, 'Worth a visit, but....11111111111111111111111111111', NULL, 2, 1, 1);
INSERT INTO `post` VALUES (2, 'I recently visited Ripley’s Aquarium of Canada for the first time since it’s opening two years ago. Its situated directly next to the CN Tower, so those interested in seeing both (tourists and residents alike) might enjoy making use of the “Sea the Sky” c', 35, b'0', NULL, 'Ripley\'s Aquarium of Canada - Review', NULL, 2, 1, 2);
INSERT INTO `post` VALUES (3, 'We love to go to the best aquariums in our family, so we naturally decided that we needed to visit Ripley’s in Toronto when we were there. It is as good as the top aquariums in the United States and better than most for its kid friendly activities. Truly ', 40, b'0', NULL, 'Top Travel Tips – Ripley’s Aquarium in Toronto', NULL, 4, 1, 3);
INSERT INTO `post` VALUES (4, 'Toronto’s newest, tallest extreme urban adventure is hands-down the CN Tower Edgewalk. The city’s tallest attraction now gives thrill seekers a chance to walk OUTSIDE the tower – around the circumference of the roof, 1,168 feet above the ground. That’s ri', 60, b'0', NULL, 'Adventure Review: CN Tower Edgewalk in Toronto', NULL, 2, 2, 3);
INSERT INTO `post` VALUES (5, 'The tallest freestanding tower in the Western Hemisphere, this landmark stretches 1,815 feet and 5 inches high and marks Toronto with its distinctive silhouette. The CN Tower is tall for a reason: prior to the opening of this telecommunications tower in 1', 84, b'0', NULL, 'FODOR\'S EXPERT REVIEW', NULL, 3, 2, 4);
INSERT INTO `post` VALUES (6, 'The CN Tower is one of the tallest free standing structures in the world and has been Toronto’s biggest tourist attraction since it opened in 1976. It was the world’s tallest for tower for more than 30 years, but lost that crown back in 2010. The tower do', 82, b'0', NULL, 'CN Tower', NULL, 4, 2, 5);
INSERT INTO `post` VALUES (7, 'Very unique, a mountain in the middle of the city. This is our second visit. First time it was summertime, and before the pandemic, and we took the the bus there. The conservatory/L’Oratoireum was closed this time due to pandemic . Our tour bus drive us t', 26, b'0', NULL, 'It gave the city its name', NULL, 1, 3, 1);
INSERT INTO `post` VALUES (8, 'When you are in Montreal, please do not miss this place. I was there during the Fall in 2019. Weather was good. Nothing is more peaceful than being surrounded by nature, beautiful landscape of trees and tranquility. Hike to the top of the mountain. It is ', 14, b'0', NULL, 'Views, Fresh Air, Nature and Montreal from the Top', NULL, 3, 3, 2);
INSERT INTO `post` VALUES (9, 'Notre-Dame Basilica of Montréal is a crown jewel in Québec’s rich religious heritage. Built between 1824 and 1829 and in Old Montreal, the church features two soaring towers and stands as a dramatic example of the Gothic Revival style. Its grand interior ', 28, b'0', NULL, 'Notre-Dame Basilica of Montréal', NULL, 2, 4, 3);
INSERT INTO `post` VALUES (10, 'The basilica is both beautiful and impressive, very much worth a visit. Aura (the show) is pretty good, the lighting excellent, the organ music leaves room for improvement. Woulda been nice to hear a choir or some holiday music. If I had to do it over, I’', NULL, b'1', NULL, 'The basilica is incredible.', NULL, NULL, 4, 5);
INSERT INTO `post` VALUES (11, 'Where to stay: We decided to stay within the town of Banff during this trip. Banff has many hotels and lodges that are popular for hikers. You can also camp within the national park, but competition for the camp sites can be high. Info on camping can be f', 37, b'0', NULL, 'Banff National Park Management Plan Review', NULL, 3, 5, 2);
INSERT INTO `post` VALUES (12, 'Some people never seem to go to bed... just weeks after their amazing K2 - Karakorum 3D, Frank Dainese and Fabio Bellini have now released another epic scenery that covers the Banff National Park in Western Canada. Banff National Park (French: Parc nation', 168, b'0', NULL, 'Scenery Review : Banff National Park UHD by Frank Dainese and Fabio Bellini', NULL, 2, 5, 3);
INSERT INTO `post` VALUES (13, 'We camped in Banff National Park twice over the months of May and June, staying at two different campgrounds near the townsite of Banff. We also spent a couple of nights in the park close to town last summer at a third campground. Each campground was VERY', 154, b'0', NULL, 'Banff National Park Management Plan', NULL, 2, 5, 4);
INSERT INTO `post` VALUES (14, '012345678910121301234567891012130123456789101213012345678910121301234567891012130123456789101213012345678910121301234567891012130123456789101213012345678910121301234567891012130123456789101213012345678910121301234567891012130123456789101213012345678910121', NULL, b'1', NULL, 'Unbelievable views of the many peaks of the Rockies.', NULL, NULL, 5, 5);

-- ----------------------------
-- Table structure for spot
-- ----------------------------
DROP TABLE IF EXISTS `spot`;
CREATE TABLE `spot`  (
  `spot_id` bigint(0) NOT NULL,
  `address` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `introduction` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `map_url` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `popularity` bigint(0) NULL DEFAULT NULL,
  `province` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `spot_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`spot_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of spot
-- ----------------------------
INSERT INTO `spot` VALUES (1, '288 Bremner Boulevard, Toronto, ON', 'Explore the Waters of the World at Ripley\'s Aquarium of Canada. Located in the heart of downtown Toronto at the base of the CN Tower, the aquarium is Toronto\'s must-see attraction for tourists and locals of all ages. Immerse yourself in a world of 20,000 ', '', 3, '', 'Ripley\'s Aquarium of Canada', '');
INSERT INTO `spot` VALUES (2, '290 Bremner Blvd, Toronto, ON', 'At a height of 553.33 m (1,815 ft., 5 in), the CN Tower is Canada’s National Tower, an engineering Wonder, award-winning dining & entertainment destination, and Toronto’s “must-see” for over 4 decades. Rocket to the top in a thrilling 58 second ride aboar', '', 5, '', 'CN Tower', '');
INSERT INTO `spot` VALUES (3, '1260 Chem. Remembrance, Montréal, QC ', 'Inaugurated in 1876, the Mount Royal Park was designed by Frederick Law Olmsted, the highly skilled designer behind New York\'s Central Park. It is an ideal site for admiring a wide variety of plants and birds or for enjoying outdoor activities. Les amis d', '', 4, '', 'Mount Royal Park', '');
INSERT INTO `spot` VALUES (4, '110 Rue Notre Dame O, Montréal, QC', 'Montreal\'s oldest Catholic church, built in 1656, is known for its intricately designed interior, which includes stained glass chronicling the history of the city.', '', 4, '', 'Notre-Dame Basilica', '');
INSERT INTO `spot` VALUES (5, '100 Sundance Rd, Banff, AB', 'Soaring mountains, jewel-colored lakes and pristine wilderness await you in Canada’s first National Park. The irresistible beauty of the landscape invites travelers to immerse themselves in the outdoors all year round — whether hiking through untouched fo', '', 5, '', 'Banff', '');
INSERT INTO `spot` VALUES (6, '289 Bremner Boulevard, Toronto, ON', 'Explore the Waters of the World at Ripley\'s Aquarium of Canada. Located in the heart of downtown Toronto at the base of the CN Tower, the aquarium is Toronto\'s must-see attraction for tourists and locals of all ages. Immerse yourself in a world of 20,000 ', '', 10, '', 'Ripley\'s Aquarium of Canada One', '');
INSERT INTO `spot` VALUES (8, '291 Bremner Boulevard, Toronto, ON', 'Explore the Waters of the World at Ripley\'s Aquarium of Canada. Located in the heart of downtown Toronto at the base of the CN Tower, the aquarium is Toronto\'s must-see attraction for tourists and locals of all ages. Immerse yourself in a world of 20,000 ', '', 20, '', 'Ripley\'s Aquarium of Canada Three', '');
INSERT INTO `spot` VALUES (9, '292 Bremner Boulevard, Toronto, ON', 'Explore the Waters of the World at Ripley\'s Aquarium of Canada. Located in the heart of downtown Toronto at the base of the CN Tower, the aquarium is Toronto\'s must-see attraction for tourists and locals of all ages. Immerse yourself in a world of 20,000 ', '', 30, '', 'Ripley\'s Aquarium of Canada Four', '');
INSERT INTO `spot` VALUES (10, '290 Bremner Boulevard, Toronto, ON', 'Explore the Waters of the World at Ripley\'s Aquarium of Canada. Located in the heart of downtown Toronto at the base of the CN Tower, the aquarium is Toronto\'s must-see attraction for tourists and locals of all ages. Immerse yourself in a world of 20,000 ', '', 10, '', 'Ripley\'s Aquarium of Canada Two', '');
INSERT INTO `spot` VALUES (11, '290 Bremner Boulevard, Toronto, ON', 'Explore the Waters of the World at Ripley\'s Aquarium of Canada. Located in the heart of downtown Toronto at the base of the CN Tower, the aquarium is Toronto\'s must-see attraction for tourists and locals of all ages. Immerse yourself in a world of 20,000 ', '', 10, '', 'Waterloo', '');
INSERT INTO `spot` VALUES (14, '390 Bremner Boulevard, Toronto, ON', 'Explore the Waters of the World at Ripley\'s Aquarium of Canada. Located in the heart of downtown Toronto at the base of the CN Tower, the aquarium is Toronto\'s must-see attraction for tourists and locals of all ages. Immerse yourself in a world of 20,000 ', '', 10, '', 'Waterloo', '');

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `user_id` bigint(0) NOT NULL,
  `avatar_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `city` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `email` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `introduction` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `profile_bg_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `rating` bigint(0) NULL DEFAULT NULL,
  `sign_time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`user_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, 'https://upload-images.jianshu.io/upload_images/5809200-a99419bb94924e6d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240', 'Waterloo', 'test1@gmail.com', 'Go for it', 'Test1234', '1', 5, '2022-03-29 00:57:34', 'nourah1992');
INSERT INTO `user` VALUES (2, NULL, NULL, 'kyrie@gmail.com', NULL, '$2a$10$KCIQuxkcOISPDVYqNAD5Je4lB0Tz.HhKRgA.nvan0citlVTBwLNtO', NULL, NULL, '2022-03-29 15:40:41', 'Kyrie');
INSERT INTO `user` VALUES (3, 'https://upload-images.jianshu.io/upload_images/5809200-7fe8c323e533f656.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240', 'Montreal', 'test3@gmail.com', 'today is rainy', 'Test1234', '13', 3, '2022-03-08 00:57:41', 'Janet S');
INSERT INTO `user` VALUES (4, 'https://upload-images.jianshu.io/upload_images/5809200-caf66b935fd00e18.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240', 'Ottawa', 'test@gmail.com', 'love my journey', 'Test1234', '21', 4, '2022-03-16 00:57:44', 'cannonfodder_12');
INSERT INTO `user` VALUES (5, 'https://upload-images.jianshu.io/upload_images/5809200-48dd99da471ffa3f.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240', 'Vancuvour', 'test5@gmail.com', 'saness', 'Test1234', '22', 4, '2022-03-04 00:57:49', 'Yasmeen K');
INSERT INTO `user` VALUES (6, 'https://upload-images.jianshu.io/upload_images/5809200-a99419bb94924e6d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240', 'Waterloo', 'test1@gmail.com', 'Go for it', '$2a$10$upBPbJEyLpoT41N4QfHYxOenDe0k.LKJBNvv52JgE2OoBnxHsTy.S', '1', 5, '2022-03-29 15:45:33', 'ziyi');
INSERT INTO `user` VALUES (7, 'https://upload-images.jianshu.io/upload_images/5809200-a99419bb94924e6d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240', 'Waterloo', 'testshy@gmail.com', 'Go for it', '$2a$10$LleXUnKVc4gBIMJx/RhjROhuEFgJDZ8fBSHSrqSAvhLnQ0f0LlfFK', '1', 5, '2022-09-26 11:26:48', 'shyyhs');
INSERT INTO `user` VALUES (8, 'https://upload-images.jianshu.io/upload_images/5809200-a99419bb94924e6d.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240', 'Waterloo', 'testshyshy@gmail.com', 'Go for it', '$2a$10$QSU.M4Su8/gkLeN6GDJMk.qBWVH4NqArsfAW.i.KoT/.0ydeU0sZS', '1', 5, '2022-09-26 15:27:49', 'shyshy');

SET FOREIGN_KEY_CHECKS = 1;
