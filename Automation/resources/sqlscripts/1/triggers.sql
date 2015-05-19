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

-- -------------------------
-- kbx_group
-- -------------------------
CREATE TRIGGER IF NOT EXISTS "kbx_group_after_update_on_kbxGroupIcon" AFTER UPDATE OF "kbxGroupIcon" ON "kbx_group"
BEGIN
	SELECT kbx_group_after_update_on_kbxGroupIcon(NEW.kbxGroupId);
END;

-- -------------------------
-- kbx_method
-- -------------------------
CREATE TRIGGER IF NOT EXISTS "kbx_method_after_delete" AFTER DELETE ON "kbx_method"
BEGIN
	SELECT kbx_method_after_delete(OLD.kbxMethodId, OLD.kbxGroupId);
END;

CREATE TRIGGER IF NOT EXISTS "kbx_method_after_update_on_kbxGroupId" AFTER UPDATE OF "kbxGroupId" ON "kbx_method"
BEGIN
	SELECT kbx_method_after_update_on_kbxGroupId(NEW.kbxMethodId, OLD.kbxGroupId, NEW.kbxGroupId);
END;

CREATE TRIGGER "kbx_method_after_update_on_kbxMethodStatus" AFTER UPDATE OF "kbxMethodStatus" ON "kbx_method"
BEGIN
	SELECT kbx_method_after_update_on_kbxMethodStatus(NEW.kbxMethodId, OLD.kbxMethodStatus, NEW.kbxMethodStatus);
END;

-- -------------------------
-- rule
-- -------------------------
CREATE TRIGGER IF NOT EXISTS "rule_after_delete" AFTER DELETE ON "rule"
BEGIN
	SELECT rule_after_delete(OLD.ruleId);
END;

CREATE TRIGGER IF NOT EXISTS "rule_after_update_on_statusProcessed_and_enabled" AFTER UPDATE OF "statusProcessed", "enabled" ON "rule"
BEGIN
	SELECT rule_after_update_on_statusProcessed_and_enabled(NEW.ruleId, OLD.enabled, NEW.enabled, OLD.statusProcessed, NEW.statusProcessed);
END;

-- -------------------------
-- scene
-- -------------------------
CREATE TRIGGER IF NOT EXISTS "scene_after_delete" AFTER DELETE ON "scene"
BEGIN
	SELECT scene_after_delete(OLD.sceneId);
END;

-- -------------------------
-- rule_condition
-- -------------------------
CREATE TRIGGER IF NOT EXISTS "rule_condition_after_delete" AFTER DELETE ON "rule_condition"
BEGIN
	SELECT rule_condition_after_delete(OLD.kbxMethodId);
END;

-- -------------------------
-- rule_execution
-- -------------------------
CREATE TRIGGER IF NOT EXISTS "rule_execution_after_delete" AFTER DELETE ON "rule_execution"
BEGIN
	SELECT rule_execution_after_delete(OLD.kbxMethodId);
END;

-- -------------------------
-- scene_execution
-- -------------------------
CREATE TRIGGER IF NOT EXISTS "scene_execution_after_delete" AFTER DELETE ON "scene_execution"
BEGIN
	SELECT scene_execution_after_delete(OLD.kbxMethodId);
END;
