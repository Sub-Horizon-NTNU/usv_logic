import numpy as np
import rclpy
from rclpy.node import Node
from waypoint_msgs.msg import Waypoint
from waypoint_msgs.msg import Waypoints


class WaypointGeneratorNode(Node):
    def __init__(self):
        super().__init__("usv_logic")
        self.publisher_ = self.create_publisher(
            Waypoints, "selene/controller/waypoints", 10
        )
        self.single_waypoint_publisher_ = self.create_publisher(
            Waypoint, "selene/controller/waypoint", 10
        )
        #timer_period = 0.0
        #self.timer = self.create_timer(timer_period, self.waypoint_send_cb)
        self.get_logger().info("Waypoint generator started")
        self.waypoint_send_cb()

        #waypoint = Waypoint()
        #waypoint.x = 8.1
        #waypoint.y = 8.25
        #waypoint.radius = 0.1;
        #waypoint.type = Waypoint.HOLD
        #waypoint.keep_on_track = True
        #waypoint.hold = True
        #self.single_waypoint_publisher_.publish(waypoint)
        #print("Waypoint published")

    def waypoint_send_cb(self):
        x,y = self.generate_infinity_symbol(
            x_center=0.0,
            y_center=0.0,
            x_distance=10.0,
            y_distance=10.0
        )

        waypoint_list = Waypoints()
        for i in range(np.size(x)):
            waypoint = Waypoint()
            waypoint.type = Waypoint.PASS
            waypoint.x = x[i]
            waypoint.y = y[i]
            waypoint.keep_on_track = True
            waypoint.radius = 0.1
            waypoint_list.waypoints.append(waypoint)
        
        self.publisher_.publish(waypoint_list)
        print("Waypoints are published")


    def generate_infinity_symbol(self,*,x_center,y_center,x_distance, y_distance):
        # https://math.stackexchange.com/questions/1277790/is-there-a-closed-form-expression-for-the-infinity-symbol

        angles = np.linspace(0.0, 2 * 3.14, num=100, dtype=float)
        x_list = []
        y_list = []

        for angle in angles:
            x_list.append(x_center + x_distance / 2.0 * np.sin(2.0*angle))
            y_list.append(y_center + y_distance / 2.0 * np.sin(angle))
        return np.array(x_list), np.array(y_list)




def main(args=None):
    rclpy.init(args=args)
    waypoint_generator = WaypointGeneratorNode()
    rclpy.spin_once(waypoint_generator)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
