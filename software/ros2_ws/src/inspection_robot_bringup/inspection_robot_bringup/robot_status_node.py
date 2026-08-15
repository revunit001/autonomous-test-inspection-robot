import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RobotStatusNode(Node):
    """Publishes the current operating state of the inspection robot."""

    VALID_STATES = {
        'INITIALIZING',
        'READY',
        'INSPECTING',
        'FAULT',
        'SHUTDOWN',
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

    def set_status(self, new_status):
        """Change the robot state if the requested state is valid."""

        if new_status not in self.VALID_STATES:
            self.get_logger().error(
                f'Invalid robot state requested: {new_status}'
            )
            return

        self.get_logger().info(
            f'State transition: {self.status_} -> {new_status}'
        )

        self.status_ = new_status

    def command_callback(self, message):
        """Handle incoming robot commands."""

        command = message.data

        self.get_logger().info(
            f'Received command: {command}'
        )

        if command == 'START_INSPECTION' and self.status_ == 'READY':
            self.set_status('INSPECTING')

        elif command == 'STOP_INSPECTION' and self.status_ == 'INSPECTING':
            self.set_status('READY')

        else:
            self.get_logger().warning(
                f'Command {command} is not valid while robot is {self.status_}'
            ) 

def main(args=None):
    rclpy.init(args=args)

    node = RobotStatusNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()