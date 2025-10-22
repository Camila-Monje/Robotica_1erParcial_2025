import rclpy
from rclpy.node import Node
from tutorial_interfaces.msg import FilteredSensor  # ← cambia aquí

class NodeResultado(Node):
    def __init__(self):
        super().__init__('node_resultado')
        self.sub = self.create_subscription(
            FilteredSensor,           # ← cambia el tipo de mensaje
            '/filtered_sensor',       # ← usa el mismo nombre de tópico
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(
            f'Resultado recibido → Promedio: {msg.promedio:.2f}, '
            f'A={msg.valor_a:.2f}, B={msg.valor_b:.2f}, C={msg.valor_c:.2f}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = NodeResultado()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()