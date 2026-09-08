import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotStatusNode(Node):
    """Manage and publish the operating state of the inspection robot."""

    VALID_STATES = {
        'INITIALIZING',
        'READY',
        'INSPECTING',
        'FAULT',
        'SHUTDOWN',
    }

    ALLOWED_TRANSITIONS = {
        'INITIALIZING': {'READY', 'FAULT'},
        'READY': {'INSPECTING', 'FAULT', 'SHUTDOWN'},
        'INSPECTING': {'READY', 'FAULT'},
        'FAULT': {'READY', 'SHUTDOWN'},
        'SHUTDOWN': set(),
    }

    COMMAND_TRANSITIONS = {
        'START_INSPECTION': 'INSPECTING',
        'STOP_INSPECTION': 'READY',
        'REPORT_FAULT': 'FAULT',
        'RESET_FAULT': 'READY',
        'SHUTDOWN': 'SHUTDOWN',
    }

    def __init__(self):
        super().__init__('robot_status_node')

        self.publisher_ = self.create_publisher(
            String,
            'robot_status',
            10
        )

        self.command_subscription_ = self.create_subscription(
            String,
            'robot_command',
            self.command_callback,
            10
        )

        self.timer_ = self.create_timer(
            1.0,
            self.publish_status
        )

        self.status_ = 'INITIALIZING'
        self.status_publish_count_ = 0

        self.get_logger().info(
            'Inspection Robot Status Node started.'
        )

    def publish_status(self):
        """Publish the robot's current operating state."""
        message = String()
        message.data = self.status_

        self.publisher_.publish(message)
        self.status_publish_count_ += 1

        self.get_logger().info(
            f'Robot status: {message.data}'
        )

        if (
            self.status_ == 'INITIALIZING'
            and self.status_publish_count_ >= 3
        ):
            self.set_status('READY')

    def command_callback(self, message):
        """Process an incoming robot command."""
        command = message.data.strip().upper()

        self.get_logger().info(
            f'Received command: {command}'
        )

        if command not in self.COMMAND_TRANSITIONS:
            self.get_logger().warning(
                f'Unknown robot command: {command}'
            )
            return

        requested_status = self.COMMAND_TRANSITIONS[command]

        self.set_status(requested_status)

    def set_status(self, new_status):
        """Change robot state only when the transition is valid."""
        if new_status not in self.VALID_STATES:
            self.get_logger().error(
                f'Invalid robot state requested: {new_status}'
            )
            return False

        if new_status == self.status_:
            self.get_logger().warning(
                f'Robot is already in state: {new_status}'
            )
            return False

        allowed_states = self.ALLOWED_TRANSITIONS[self.status_]

        if new_status not in allowed_states:
            self.get_logger().warning(
                f'Illegal state transition: '
                f'{self.status_} -> {new_status}'
            )
            return False

        self.get_logger().info(
            f'State transition: {self.status_} -> {new_status}'
        )

        self.status_ = new_status
        return True


def main(args=None):
    rclpy.init(args=args)

    node = RobotStatusNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
