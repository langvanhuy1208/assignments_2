#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Lang Van Huy (23020745)
Module: Robot Skills for UR3 Manipulator
"""

import time

class HuyUR3SkillLibrary:
    def __init__(self):
        print("[SKILLS INIT] Thu vien ky nang robot cua Lang Van Huy da san sang.")

    def move_to_home_pose(self):
        print("[SKILL EXEC] Dang dieu khien UR3 ve vi tri an toan (Home)...")
        time.sleep(0.5)
        return "SUCCESS"

    def execute_pick_action(self, target_object):
        print(f"[SKILL EXEC] Tien hanh thao tac GAP vat the: [{target_object}]")
        time.sleep(0.8)
        return "SUCCESS"

    def execute_place_action(self, target_object, destination_zone):
        print(f"[SKILL EXEC] Tien hanh THA vat [{target_object}] vao khu vuc [{destination_zone}]")
        time.sleep(0.8)
        return "SUCCESS"
