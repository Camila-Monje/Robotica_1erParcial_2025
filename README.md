# Robotica_1erParcial_2025

## Manual de ejecución de ejercicios
Ejercicio 1:

Para ejecutar los archivos del proyecto, dentro de la carpeta principal se encuentra el directorio robot_description, que contiene los archivos URDF del índice, del pulgar y de ambos dedos juntos, además de los archivos launch necesarios para visualizar los modelos en RViz. En la subcarpeta urdf se tienen los archivos:
	indice.urdf (modelo del dedo índice)
	indice.urdf.xacro (índice para la construcción de ambos dedos)
	pulgar.urdf (modelo del pulgar)
	pulgar.urdf.xacro (pulgar para la construcción conjunta) 
	tengoo_hand.urdf.xacro (modelo completo con ambos dedos)
En la subcarpeta launch se incluyen los archivos:
	view_robot_i.launch.py
	view_robot_p.launch.py 
	view_robot_t.launch.py
Que permiten lanzar el modelo del índice, el pulgar o ambos dedos respectivamente. Para compilar y ejecutar los modelos se utilizan los comandos:
	colcon build
	source install/setup.bash 
	ros2 launch robot_description view_robot_i.launch.py
Cambiando el nombre del archivo según el dedo que se desee visualizar.

Por otra parte, en la carpeta visual_pubsub se encuentran los scripts de cinemática inversa: 	inverse_kinematics.py (índice)
	inverse_kinematics_pulgar.py (pulgar)
	inverse_kinematics_t.py (ambos dedos)
En esta misma carpeta se debe modificar el archivo setup.py, añadiendo las líneas 
	'inverse_k = visual_pubsub.inverse_kinematics:main', 
	'inverse_k_p = visual_pubsub.inverse_kinematics_pulgar:main'.
	'inverse_k_t = visual_pubsub.inverse_kinematics_t:main' 
Para registrar los publicadores. Finalmente, los scripts se ejecutan con los comandos 
	colcon build
	source install/setup.bash 
	ros2 run visual_pubsub inverse_k
Cambiando el nombre inverse_k según el publicador correspondiente al dedo que se desee ejecutar.

Ejercicio 2:

Para esta parte, debes compilar dentro del espacio de trabajo pubsub_ws.
Dentro del paquete pubsub, encontrarás los archivos de los nodos.

Nodos

Los nodos node_a, node_b y node_c simulan tres sensores independientes.
En el espacio de trabajo también hay una imagen que explica la estructura de los nodos utilizando rqt_graph.

El paquete tutorial_interfaces contiene los archivos CMake y los archivos de interfaz (.msg) usados para definir el tipo de mensaje personalizado.
Las imágenes en tiempo real incluidas en el repositorio muestran el formato del mensaje tal como se imprime durante la ejecución.

Explicación del gráfico

Cuando el sistema se está ejecutando, rqt_graph muestra solo cuatro nodos.
Esto ocurre porque los tres nodos de sensores (node_a, node_b, node_c) publican en el mismo tópico, y el nodo suscriptor principal agrega sus datos. Por lo tanto, ROS 2 simplifica la visualización mostrando un único nodo suscriptor conectado a un solo tópico compartido por los tres publicadores.
