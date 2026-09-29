from setuptools import setup
import os
from glob import glob

package_name = 'assignments_2'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Lang Van Huy',
    maintainer_email='23020745@vnu.edu.vn',
    description='Assignments 2 - UR3 LLM Skill Planner',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'skill_executor_node = assignments_2.skill_executor_node:main',
        ],
    },
)
