#!/usr/bin/env python3

import rclpy  # Import ROS2 Python library
from rclpy.node import Node  # Import Node module
from std_msgs.msg import String  # Import String message type

# Combined class definition for both publisher and subscriber
class PublisherSubscriberNode(Node):
    def __init__(self):
        super().__init__('publisher_subscriber')  # Initialize the Node with the name 'publisher_subscriber'
        
        # Publisher setup
        self.publisher_ = self.create_publisher(String, 'mobile', 10)  # Create a publisher for 'mobile' topic
        self.timer = self.create_timer(0.5, self.timer_callback)  # Timer to publish a message every 0.5 seconds
        
        # Subscriber setup
        self.subscription = self.create_subscription(
            String,        # The message type
            'Telephone',      # The topic to subscribe to
            self.listener_callback,  # Callback function when a message is received
            10             # Queue size
        )

    def timer_callback(self):
        msg = String()  # Create a new String message
        msg.data = 'Hello, ROS2'  # Assign data to the message
        self.publisher_.publish(msg)  # Publish the message
        self.get_logger().info(f'Publishing: "{msg.data}"')  # Log the message being published

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')  # Log the received message

def main(args=None):
    rclpy.init(args=args)  # Initialize ROS2 communication
    publisher_subscriber_node = PublisherSubscriberNode()  # Create an instance of the combined node
    rclpy.spin(publisher_subscriber_node)  # Keep the node alive and process callbacks

    publisher_subscriber_node.destroy_node()  # Clean up the node
    rclpy.shutdown()  # Shut down ROS2 communication

if __name__ == '__main__':
    main()
