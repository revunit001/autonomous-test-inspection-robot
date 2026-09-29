## Build the ROS 2 workspace

From `software/ros2_ws`:

    colcon build --symlink-install

Builds all ROS 2 packages in the workspace.

## Load the workspace

    source install/setup.bash

Makes the newly built packages available to the current terminal.

## List package executables

    ros2 pkg executables inspection_robot_bringup

Shows the executable nodes provided by our bringup package.

## Run the status node

    ros2 run inspection_robot_bringup robot_status_node