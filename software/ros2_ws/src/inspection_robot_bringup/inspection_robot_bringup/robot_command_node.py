# Copyright 2026 Michael W. Smith
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotCommandNode(Node):
    """Publishes commands for the inspection robot."""

    def __init__(self):
        super().__init__('robot_command_node')

        self.publisher_ = self.create_publisher(
            String,
            'robot_command',
            10
        )

        self.get_logger().info(
            'Inspection Robot Command Node started.'
        )

    def send_command(self, command):
        """Publish a robot command."""
        message = String()
        message.data = command

        self.publisher_.publish(message)

        self.get_logger().info(
            f'Command sent: {command}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = RobotCommandNode()

    node.get_logger().info(
        'Waiting for robot command subscriber...'
    )

    timeout_seconds = 5.0
    elapsed_seconds = 0.0
    poll_interval = 0.1

    while (
        node.publisher_.get_subscription_count() == 0
        and elapsed_seconds < timeout_seconds
    ):
        rclpy.spin_once(node, timeout_sec=poll_interval)
        elapsed_seconds += poll_interval

    if node.publisher_.get_subscription_count() == 0:
        node.get_logger().error(
            'No robot command subscriber detected. Command not sent.'
        )
    else:
        node.get_logger().info(
            'Robot command subscriber detected.'
        )

        node.send_command('START_INSPECTION')

        rclpy.spin_once(node, timeout_sec=0.5)

    node.destroy_node()
    rclpy.shutdown()
