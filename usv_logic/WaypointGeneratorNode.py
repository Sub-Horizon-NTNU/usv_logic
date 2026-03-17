import numpy as np
import rclpy
from rclpy.node import Node

from waypoint_msgs.msg import WaypointPass


class WaypointGeneratorNode(Node):
    def __init__(self):
        super().__init__("usv_logic")
        self.publisher_ = self.create_publisher(
            WaypointPass, "selene/waypoint/pass", 10
        )
        timer_period = 0.
        self.timer = self.create_timer(timer_period, self.waypoint_pass_cb)
        self.get_logger().info("Waypoint generator started")

    def waypoint_pass_cb(self):
        radius = 3.5
        angles = np.linspace(0.0, 2*3.14, num=100, dtype=float)
        for angle in angles:
            wp_pass = WaypointPass()
            wp_pass.waypoint.x = radius * np.cos(angle)
            wp_pass.waypoint.y = radius * np.sin(angle)
            wp_pass.waypoint.radius = 0.2

            self.publisher_.publish(wp_pass)

def main(args=None):
    rclpy.init(args=args)
    waypoint_generator = WaypointGeneratorNode()
    rclpy.spin(waypoint_generator)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
