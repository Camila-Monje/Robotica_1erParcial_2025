import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Point
import numpy as np
import time

class InverseKinematicsDobleDedo(Node):

    def __init__(self):
        super().__init__('inverse_kinematics_doble_dedo')
        self.joint_pub = self.create_publisher(JointState, 'joint_states', 10)
        self.target_sub = self.create_subscription(Point, 'target_position',
                                                     self.target_callback, 10)
        
        self.pulgar_names = ['pulgar_q0', 'pulgar_q1', 'pulgar_q2', 'pulgar_q3']
        self.indice_names = ['indice_q1', 'indice_q2', 'indice_q3']
        self.all_joint_names = self.pulgar_names + self.indice_names
        
        self.l1_p = 0.5; self.l2_p = 0.4; self.l3_p = 0.3 
        self.q_pulgar = np.array([0.0, -0.5, -0.5, -0.5]) 
        self.q_min_p = np.array([-0.52, -1.57, -1.57, -1.57]) 
        self.q_max_p = np.array([ 0.52,  0.0,   0.0,   0.0])

        self.l1_i = 0.6; self.l2_i = 0.5; self.l3_i = 0.4
        self.q_indice = np.array([0.0, 0.0, 0.0]) 
        self.q_min_i = np.array([-1.57, -1.57, -1.57])
        self.q_max_i = np.array([ 1.57,  1.57,  1.57])
        
        self.target_pos = np.array([0.1, -0.2, 0.4]) 
        self.damping_factor = 0.05
        self.global_gain_factor = 2.5
        self.max_step_magnitude = 0.5
        self.tolerance = 0.015        
        self.timer_period = 0.02
        self.timer = self.create_timer(self.timer_period, self.update_joints) 

        self.get_logger().info(f"Objetivo inicial: {self.target_pos}")
    
    def fk_pulgar(self, q):
        q0, q1, q2, q3 = q
        L1, L2, L3 = self.l1_p, self.l2_p, self.l3_p
        
        T_base = np.array([
            [np.cos(2.356), -np.sin(2.356), 0, -0.02],
            [np.sin(2.356), np.cos(2.356), 0, -0.02],
            [0, 0, 1, 0.05],
            [0, 0, 0, 1]
        ])

        R_proj = L1 * np.cos(q1) + L2 * np.cos(q1 + q2) + L3 * np.cos(q1 + q2 + q3)
        x_p = R_proj * np.cos(q0)
        y_p = R_proj * np.sin(q0)
        z_p = L1 * np.sin(q1) + L2 * np.sin(q1 + q2) + L3 * np.sin(q1 + q2 + q3)
        
        pos_pulgar_local = np.array([x_p, y_p, z_p, 1])
        
        pos_pulgar_global = T_base @ pos_pulgar_local
        return pos_pulgar_global[:3]

    def jacobian_pulgar(self, q):
        q0, q1, q2, q3 = q
        L1, L2, L3 = self.l1_p, self.l2_p, self.l3_p
        R = L1 * np.cos(q1) + L2 * np.cos(q1 + q2) + L3 * np.cos(q1 + q2 + q3)
        S1 = L1 * np.sin(q1) + L2 * np.sin(q1 + q2) + L3 * np.sin(q1 + q2 + q3) 
        S2 = L2 * np.sin(q1 + q2) + L3 * np.sin(q1 + q2 + q3)                  
        S3 = L3 * np.sin(q1 + q2 + q3)                                         
        C1 = L1 * np.cos(q1) + L2 * np.cos(q1 + q2) + L3 * np.cos(q1 + q2 + q3) 
        C2 = L2 * np.cos(q1 + q2) + L3 * np.cos(q1 + q2 + q3)                   
        C3 = L3 * np.cos(q1 + q2 + q3)                                          
        
        J_local = np.array([
            [-R * np.sin(q0), -S1 * np.cos(q0), -S2 * np.cos(q0), -S3 * np.cos(q0)],
            [ R * np.cos(q0), -S1 * np.sin(q0), -S2 * np.sin(q0), -S3 * np.sin(q0)],
            [0.0, C1, C2, C3]
        ]).T 

        return J_local.T

    def fk_indice(self, q):
        q1, q2, q3 = q
        L1, L2, L3 = self.l1_i, self.l2_i, self.l3_i
        
        T_base = np.array([
            [np.cos(-0.785), -np.sin(-0.785), 0, 0.02],
            [np.sin(-0.785), np.cos(-0.785), 0, 0.02],
            [0, 0, 1, 0.05],
            [0, 0, 0, 1]
        ])

        x_i = L1 * np.sin(q1) + L2 * np.sin(q1 + q2) + L3 * np.sin(q1 + q2 + q3)
        y_i = - (L1 * np.cos(q1) + L2 * np.cos(q1 + q2) + L3 * np.cos(q1 + q2 + q3))
        z_i = 0.0 
        
        pos_indice_local = np.array([x_i, y_i, z_i, 1])
        
        pos_indice_global = T_base @ pos_indice_local
        return pos_indice_global[:3]

    def jacobian_indice(self, q):
        q1, q2, q3 = q
        L1, L2, L3 = self.l1_i, self.l2_i, self.l3_i
        
        C1 = L1 * np.cos(q1) + L2 * np.cos(q1 + q2) + L3 * np.cos(q1 + q2 + q3)
        C2 = L2 * np.cos(q1 + q2) + L3 * np.cos(q1 + q2 + q3)
        C3 = L3 * np.cos(q1 + q2 + q3)
        
        S1 = L1 * np.sin(q1) + L2 * np.sin(q1 + q2) + L3 * np.sin(q1 + q2 + q3)
        S2 = L2 * np.sin(q1 + q2) + L3 * np.sin(q1 + q2 + q3)
        S3 = L3 * np.sin(q1 + q2 + q3)

        J_local = np.array([
            [C1, C2, C3], 
            [-S1, -S2, -S3], 
            [0.0, 0.0, 0.0]
        ])
        
        return J_local

    def apply_joint_limits_pulgar(self, q):
        return np.clip(q, self.q_min_p, self.q_max_p)

    def apply_joint_limits_indice(self, q):
        return np.clip(q, self.q_min_i, self.q_max_i)

    def target_callback(self, msg):
        self.target_pos = np.array([msg.x, msg.y, msg.z])

    def update_joints(self):
        current_pos_p = self.fk_pulgar(self.q_pulgar)
        error_p = self.target_pos - current_pos_p
        error_norm_p = np.linalg.norm(error_p)
        
        if error_norm_p > self.tolerance:
            J_p = self.jacobian_pulgar(self.q_pulgar)
            JtJ_p = J_p.T @ J_p
            damping_sq_p = (self.damping_factor ** 2) * np.eye(JtJ_p.shape[0])
            J_pseudo_p = J_p.T @ np.linalg.inv(J_p @ J_p.T + (self.damping_factor ** 2) * np.eye(3))
            
            dq_p = J_pseudo_p @ error_p
            
            dq_norm_p = np.linalg.norm(dq_p)
            if dq_norm_p > self.max_step_magnitude:
                dq_p *= self.max_step_magnitude / dq_norm_p
            
            self.q_pulgar += dq_p * self.global_gain_factor * self.timer_period
            self.q_pulgar = self.apply_joint_limits_pulgar(self.q_pulgar)
        
        current_pos_i = self.fk_indice(self.q_indice)
        error_i = self.target_pos - current_pos_i
        error_norm_i = np.linalg.norm(error_i)

        if error_norm_i > self.tolerance:
            J_i = self.jacobian_indice(self.q_indice)
            J_pseudo_i = J_i.T @ np.linalg.inv(J_i @ J_i.T + (self.damping_factor ** 2) * np.eye(3))
            
            dq_i = J_pseudo_i @ error_i
            
            dq_norm_i = np.linalg.norm(dq_i)
            if dq_norm_i > self.max_step_magnitude:
                dq_i *= self.max_step_magnitude / dq_norm_i

            self.q_indice += dq_i * self.global_gain_factor * self.timer_period
            self.q_indice = self.apply_joint_limits_indice(self.q_indice)

        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = self.all_joint_names
        
        msg.position = self.q_pulgar.tolist() + self.q_indice.tolist()
        self.joint_pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = InverseKinematicsDobleDedo()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()