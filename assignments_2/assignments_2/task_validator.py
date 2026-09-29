#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Lang Van Huy (23020745)
Module: Task Validator for Plan Safety Check
"""

ALLOWED_SKILLS = ["home", "pick", "place"]
ALLOWED_OBJECTS = ["red_cube", "yellow_cube", "blue_cube"]
ALLOWED_ZONES = ["zone_a", "zone_b", "zone_c"]

class HuyPlanValidator:
    @staticmethod
    def verify_plan(plan_dict):
        if not isinstance(plan_dict, dict) or "plan" not in plan_dict:
            return False, "Loi cau truc JSON: Thieu khoa 'plan'."

        for item in plan_dict["plan"]:
            skill_name = item.get("skill")
            if skill_name not in ALLOWED_SKILLS:
                return False, f"Phat hien skill khong hop le: {skill_name}"

            if skill_name == "pick":
                obj = item.get("object")
                if obj not in ALLOWED_OBJECTS:
                    return False, f"Phat hien object khong hop le trong pick: {obj}"

            elif skill_name == "place":
                obj = item.get("object")
                zone = item.get("zone")
                if obj not in ALLOWED_OBJECTS:
                    return False, f"Phat hien object khong hop le trong place: {obj}"
                if zone not in ALLOWED_ZONES:
                    return False, f"Phat hien zone khong hop le trong place: {zone}"

        return True, "SUCCESS"
