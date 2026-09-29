#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Lang Van Huy (23020745)
Main ROS 2 Node to execute LLM plans via Skills and MoveIt
"""

import json
import rclpy
from rclpy.node import Node

from assignments_2.llm_planner import HuyLLMPlanner
from assignments_2.task_validator import HuyPlanValidator
from assignments_2.robot_skills import HuyUR3SkillLibrary

class MainExecutionNode(Node):
    def __init__(self):
        super().__init__('assignments_2_executor_node')
        self.get_logger().info("Khoi tao Main Execution Node cua Lăng Văn Huy (23020745)...")
        
        self.planner = HuyLLMPlanner()
        self.skills = HuyUR3SkillLibrary()

    def run_demo_task(self, prompt_text):
        # 1. LLM sinh ke hoach
        plan_json = self.planner.process_command(prompt_text)
        
        print("\nLLM PLAN:")
        print(json.dumps(plan_json, indent=2))

        # 2. Validator kiem tra
        is_safe, err_msg = HuyPlanValidator.verify_plan(plan_json)
        if not is_safe:
            print(f"\n[CANH BAO] TASK REJECTED: {err_msg}")
            return False

        print("\nEXECUTION:")
        # 3. Thuc thi skill
        for step in plan_json["plan"]:
            s_name = step["skill"]
            status = "SUCCESS"

            if s_name == "home":
                status = self.skills.move_to_home_pose()
                print(f"home() ................. {status}")
            elif s_name == "pick":
                obj = step["object"]
                status = self.skills.execute_pick_action(obj)
                print(f"pick({obj}) ........ {status}")
            elif s_name == "place":
                obj = step["object"]
                zone = step["zone"]
                status = self.skills.execute_place_action(obj, zone)
                print(f"place({obj}, {zone}) SUCCESS")

            if status != "SUCCESS":
                print(f"\nTASK FAILED tai buoc: {s_name}")
                return False

        print("\nTASK SUCCESS")
        return True

def main(args=None):
    rclpy.init(args=args)
    node = MainExecutionNode()
    
    # Kich ban thu nghiem 1 (Co ban)
    sample_command = "Please put the red cube in zone B."
    node.run_demo_task(sample_command)
    
    # Ky vong kich ban nang cao (Bo sung neu can):
    # adv_command = "Arrange all objects according to my student ID."
    # node.run_demo_task(adv_command)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
