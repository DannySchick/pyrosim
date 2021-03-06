from pyrosim import PYROSIM
import matplotlib.pyplot as plt


class ROBOT:
	def __init__(self, sim, wt):
		sim.Send_Cylinder(objectID = 0, x=0 , y=0 , z=0.6 , length = 1.0, radius = 0.1)
		sim.Send_Cylinder(objectID = 1, x=0, y=.5, z=1.1, r=1, g=0, b=0, r1=0 , r2=1, r3=0)

		sim.Send_Joint(jointID = 0, firstObjectID = 0, secondObjectID = 1, 
			x=0, y=0, z=1.1, n1=-1, n2=0, n3=0, lo=-3.14159/2 , hi=3.14159/2)

		sim.Send_Touch_Sensor(sensorID=0, objectID=0)
		sim.Send_Touch_Sensor(sensorID=1, objectID=1)

		# sensor that returns current angle of joint in rads
		sim.Send_Proprioceptive_Sensor(sensorID=2, jointID=0)

		# sensor that sends ray outwards and returns length of that ray
		# xyz is where it resides (at the tip in this case)
		# r's define where to point
		#sim.Send_Ray_Sensor(sensorID=3, objectID=1, x=0, y=1.1, z=1.1, r1=0, r2=1, r3=0)
		sim.Send_Ray_Sensor(sensorID=3, objectID=1, x=0, y=.55, z=1.1, r1=0, r2=0, r3=-1)

		sim.Send_Position_Sensor(sensorID=4, objectID=1)

		sim.Send_Sensor_Neuron(neuronID=0, sensorID=0)
		sim.Send_Sensor_Neuron(neuronID=1, sensorID=1)
		sim.Send_Motor_Neuron(neuronID=2, jointID=0)


		sim.Send_Synapse(sourceNeuronID = 1 , targetNeuronID = 2 , weight = wt )
		# sim.Send_Synapse(sourceNeuronID=0, targetNeuronID=2, weight=-1.0)

