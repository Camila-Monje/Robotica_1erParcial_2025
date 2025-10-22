"""
    Author: carlos
    Launch file to visualize the combined Tengoo 2-finger hand model (Pulgar and Indice).
"""
from ament_index_python.packages import get_package_share_path

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration


def generate_launch_description():
    """
    launch method
    """
    pkg_share = get_package_share_path('robot_description')
    
    # APUNTA al modelo Xacro compuesto
    default_model_path = pkg_share / 'urdf/tengoo_hand.urdf.xacro'  
    
    default_rviz_config_path = pkg_share / 'rviz/urdf.rviz'

    # 1. Argumentos de Lanzamiento
    gui_arg = DeclareLaunchArgument(
        name='gui',
        default_value='false',  
        choices=['true', 'false'],
        description='Enable joint_state_publisher_gui (sliders)'
    )

    model_arg = DeclareLaunchArgument(
        name='model',
        default_value=str(default_model_path),
        description='Absolute path to robot URDF/XACRO file'
    )

    rviz_arg = DeclareLaunchArgument(
        name='rvizconfig',
        default_value=str(default_rviz_config_path),
        description='Absolute path to RViz config file'
    )

    # 2. Comando Xacro para procesar el modelo
    robot_description = ParameterValue(
        Command(['xacro ', LaunchConfiguration('model')]),
        value_type=str
    )

    # 3. Nodos Principales
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': robot_description}]
    )

    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        condition=UnlessCondition(LaunchConfiguration('gui')),
        parameters=[{
            'publish_default_positions': True 
        }]
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        condition=IfCondition(LaunchConfiguration('gui'))
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', LaunchConfiguration('rvizconfig')],
    )

    # 4. Retorna la descripción del lanzamiento
    return LaunchDescription([
        gui_arg,
        model_arg,
        rviz_arg,
        joint_state_publisher_node,
        joint_state_publisher_gui_node,
        robot_state_publisher_node,
        rviz_node
    ])