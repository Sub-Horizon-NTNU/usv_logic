# usv_logic

Small ROS 2 Python **waypoint-generation example** for Selene. It generates a fixed figure-eight route and publishes it to the controller; this repository is not the complete mission or autonomy system.

## Current behaviour

[WaypointGeneratorNode.py](usv_logic/WaypointGeneratorNode.py) creates 100 `PASS` waypoints around (0, 0), with a 10 m extent on each axis and a 0.1 m acceptance radius, and publishes them once on `selene/controller/waypoints`. It also creates a single-waypoint publisher on `selene/controller/waypoint`, but the current example does not use it.

The route is hard-coded. The script does not wait for subscriber discovery or monitor completion, so a one-shot publication is not a reliable mission-delivery mechanism.

## Dependencies and entry point

The package uses ROS 2 `rclpy`, NumPy and [waypoint_msgs](https://github.com/Sub-Horizon-NTNU/waypoint_msgs). Place both packages in a sourced ROS 2 workspace and build from its root:

```sh
colcon build --packages-up-to usv_logic
source install/setup.bash
```

The installed executable is `ros2 run usv_logic waypoint_generator`. Starting it immediately publishes the route to any connected controller; use an isolated test setup when inspecting the example.

For the more extensive mission API and mission examples, see [usv_mission_package](https://github.com/Sub-Horizon-NTNU/usv_mission_package).
