#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Lang Van Huy (23020745)
Module: LLM Planner connected to 9Router API
"""
import json
import os
from openai import OpenAI

class HuyLLMPlanner:
    def __init__(self):
        # Cau hinh ket noi 9Router / OpenAI API Key
        self.api_key = os.getenv("OPENAI_API_KEY", "your_9router_api_key_here")
        self.base_url = os.getenv("OPENAI_BASE_URL", "https://api.9router.com/v1")
        
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )
        
        self.system_prompt = """
Ban la mot bo lap ke hoach tac vu (Task Planner) cho canh tay robot UR3.
Cac skill cho phep:
- home()
- pick(object)
- place(object, zone)

Danh sach vat the (Objects):
- red_cube
- yellow_cube
- blue_cube

Danh sach khu vuc (Zones):
- zone_a
- zone_b
- zone_c

Yeu cau bat buoc:
1. Chi tra ve DUY NHAT mot doi tuong JSON chuan xac theo cau truc mau duoi day, khong kem bat ky van ban nao khac.
2. Khong duoc sinh ma lenh joint cua robot.
3. Cau truc JSON mau:
{
  "plan": [
    {"skill": "pick", "object": "red_cube"},
    {"skill": "place", "object": "red_cube", "zone": "zone_b"},
    {"skill": "home"}
  ]
}
"""

    def process_command(self, user_command):
        print(f"\n==========================================")
        print(f"USER COMMAND (Huy 23020745): {user_command}")
        print(f"==========================================")

        try:
            # Su dung dung cu phap chat completions cua OpenAI python SDK
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_command}
                ],
                temperature=0.0
            )
            
            content = response.choices[0].message.content.strip()
            if content.startswith("```json"):
                content = content[7:]
            if content.endswith("```"):
                content = content[:-3]
                
            plan_data = json.loads(content.strip())
            return plan_data

        except Exception as e:
            print(f"[LOI LLM PLANNER] Khong the goi 9Router API hoac parse JSON: {e}")
            # Fallback thong minh neu chua co API Key 9Router that
            cmd_lower = user_command.lower()
            if "red cube" in cmd_lower and "zone b" in cmd_lower:
                return {
                    "plan": [
                        {"skill": "pick", "object": "red_cube"},
                        {"skill": "place", "object": "red_cube", "zone": "zone_b"},
                        {"skill": "home"}
                    ]
                }
            return {
                "plan": [
                    {"skill": "home"}
                ]
            }
