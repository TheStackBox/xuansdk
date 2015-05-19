-- ---------------------------------------------------------------------------------------------
-- Copyright 2014-2015 Cloud Media Sdn. Bhd.
--
-- This file is part of Xuan Automation Application.
--
-- Xuan Automation Application is free software: you can redistribute it and/or modify
-- it under the terms of the GNU General Public License as published by
-- the Free Software Foundation, either version 3 of the License, or
-- (at your option) any later version.
--
-- Xuan Automation Application is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU General Public License for more details.
--
-- You should have received a copy of the GNU General Public License
-- along with Xuan Automation Application.  If not, see <http://www.gnu.org/licenses/>.
-- ---------------------------------------------------------------------------------------------

-- ----------------------------
-- Table structure for kbx_group
-- ----------------------------
CREATE TABLE IF NOT EXISTS "kbx_group" (
"kbxGroupId"  INTEGER PRIMARY KEY,
"kbxGroupParentId"  INTEGER,
"kbxGroupName"  TEXT,
"kbxGroupLabel"  TEXT,
"kbxGroupIcon"  TEXT,
"kbxGroupStatus"  INTEGER
);

-- ----------------------------
-- Table structure for kbx_method
-- ----------------------------
CREATE TABLE IF NOT EXISTS "kbx_method" (
"kbxMethodId"  INTEGER PRIMARY KEY,
"kbxMethodName"  TEXT,
"kbxModuleName"	TEXT,
"kbxMethodAppId"	INTEGER,
"kbxMethodLabel"  TEXT,
"kbxMethodStatus"  INTEGER,
"kbxGroupId"  INTEGER NOT NULL,
CONSTRAINT "fkey0" FOREIGN KEY ("kbxGroupId") REFERENCES "kbx_group" ("kbxGroupId")
);

-- ----------------------------
-- Table structure for rule
-- ----------------------------
CREATE TABLE IF NOT EXISTS "rule" (
"ruleId"  INTEGER PRIMARY KEY AUTOINCREMENT,
"ruleName"  TEXT,
"ruleProtected"  BOOLVAL,
"trigger"  DICTIONARY,
"enabled"  BOOLVAL,
"statusProcessed"	TEXT NOT NULL,
"createdTime"  INTEGER NOT NULL,
"updatedTime"  INTEGER NOT NULL,
"sort"  INTEGER NOT NULL
);

-- ----------------------------
-- Table structure for rule_condition
-- ----------------------------
CREATE TABLE IF NOT EXISTS "rule_condition" (
"rcId"	INTEGER PRIMARY KEY AUTOINCREMENT,
"rcRuleId"  INTEGER NOT NULL,
"kbxMethodId"  INTEGER,
"kbxMethodParams"  LIST,
"createdTime"  INTEGER NOT NULL,
"sort"  INTEGER NOT NULL,
CONSTRAINT "fkey0" FOREIGN KEY ("rcRuleId") REFERENCES "rule" ("ruleId"),
CONSTRAINT "fkey1" FOREIGN KEY ("kbxMethodId") REFERENCES "kbx_method" ("kbxMethodId")
);

-- ----------------------------
-- Table structure for rule_execution
-- ----------------------------
CREATE TABLE IF NOT EXISTS "rule_execution" (
"reId"	INTEGER PRIMARY KEY AUTOINCREMENT,
"reRuleId"  INTEGER NOT NULL,
"kbxMethodId"  INTEGER,
"kbxMethodParams"  LIST,
"createdTime"  INTEGER NOT NULL,
"sort"  INTEGER NOT NULL,
CONSTRAINT "fkey0" FOREIGN KEY ("reRuleId") REFERENCES "rule" ("ruleId"),
CONSTRAINT "fkey1" FOREIGN KEY ("kbxMethodId") REFERENCES "kbx_method" ("kbxMethodId")
);

-- ----------------------------
-- Table structure for scene
-- ----------------------------
CREATE TABLE IF NOT EXISTS "scene" (
"sceneId" INTEGER PRIMARY KEY AUTOINCREMENT,
"sceneName" TEXT,
"sceneProtected" BOOLVAL,
"sceneIcon" TEXT,
"statusProcessed" TEXT,
"createdTime" INTEGER NOT NULL,
"updatedTime" INTEGER NOT NULL,
"sort" INTEGER NOT NULL
);

-- ----------------------------
-- Table structure for scene_execution
-- ----------------------------
CREATE TABLE IF NOT EXISTS "scene_execution" (
"seId" INTEGER PRIMARY KEY AUTOINCREMENT,
"seSceneId" INTEGER NOT NULL,
"kbxMethodId" INTEGER,
"kbxMethodParams" LIST,
"createdTime" INTEGER,
"sort" INTEGER NOT NULL,
CONSTRAINT "fkey0" FOREIGN KEY ("kbxMethodId") REFERENCES "kbx_method" ("kbxMethodId"),
CONSTRAINT "fkey1" FOREIGN KEY ("seSceneId") REFERENCES "scene" ("sceneId")
);
