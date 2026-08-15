from setuptools import find_packages, setup

package_name = 'inspection_robot_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='revunit001',
    maintainer_email='revunit001@gmail.com',
    description='TODO: Package description',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'robot_status_node = inspection_robot_bringup.robot_status_node:main',
            'robot_command_node = inspection_robot_bringup.robot_command_node:main',
        ],
    },
)
