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


class RobotTelemetryNode(Node):
    """Publish simulated robot hardware telemetry."""

    def __init__(self):
        """Initialize the telemetry publisher."""
        super().__init__('robot_telemetry_node')

        self.publisher_ = self.create_publisher(
            String,
            'robot_telemetry',
            10
        )

        self.timer_ = self.create_timer(
            1.0,
            self.publish_telemetry
        )

        self.battery_level = 95
        self.motor_available = True
        self.sensor_healthy = True

        self.get_logger().info(
            'Robot telemetry node started.'
        )

    def publish_telemetry(self):
        """Publish simulated hardware telemetry."""
        motor_status = 'OK' if self.motor_available else 'FAULT'
        sensor_status = 'OK' if self.sensor_healthy else 'FAULT'

        telemetry = (
            f'BATTERY={self.battery_level};'
            f'MOTOR={motor_status};'
            f'SENSOR={sensor_status}'
        )

        message = String()
        message.data = telemetry

        self.publisher_.publish(message)

        self.get_logger().info(
            f'Published telemetry: {telemetry}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = RobotTelemetryNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
