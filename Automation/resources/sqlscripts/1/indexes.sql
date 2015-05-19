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
-- rule_condition
-- -------------------------
CREATE INDEX IF NOT EXISTS "rule_condition_rcRuleId_index" ON "rule_condition" ("rcRuleId");

-- -------------------------
-- rule_execution
-- -------------------------
CREATE INDEX IF NOT EXISTS "rule_execution_reRuleId_index" ON "rule_execution" ("reRuleId");

-- -------------------------
-- scene_execution
-- -------------------------
CREATE INDEX IF NOT EXISTS "scene_execution_seSceneId_index" ON "scene_execution" ("seSceneId");