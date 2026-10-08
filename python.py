# import keyword;
# print(keyword.kwlist)

# p=False
# print(type(p))

# p=1
# print(type(p))

# p=3
# x=2*p
# print(x)

# a,b,c=1,2


# type conversion

# a=1
# a=int(a)
# print(a)
# print(type(a))

# a="1"
# a=float(a)
# print(a)
# print(type(a))

# a=21
# a=str(a)
# print(a)
# print(type(a))

# b=1
# print(bool(b))

# b=0
# print(bool(b))

# b=""
# print(bool(b))

# b="hello"
# print(bool(b))


# distance='41'
# distance=float(distance)
# if distance<40:
#     print("Object detected")
# else:
#     print("object not detected")


# age="100"
# result=int(age)+50
# print(result)

# age="12.5"
# age=float(age)
# result=int(age)*2
# print(result)

# distance='45.8'
# distance=float(distance)
# if distance<50:
#     print("Object detected")
# else:
#     print("object not detected")


# a=input("Enter robot speed: ")
# result=float(a)
# print(type(result))
# print("The robot speed is",result,'m/s')

# distance=input("Enter distance: ")
# distance=float(distance)
# if distance<50:
#     print("Obstacle detected")
# else:
#     print("Path is clear....")


# speed=input("Enter speed:")
# battery=input("Robot battery percentage:")
# distance=input("Enter distance:")
# speed=int(speed)
# battery=int(battery)
# distance=int(distance)
# if battery<20:
#     print("Battery Low")
# elif distance<50:
#     print("Obstacle is detected")
# else:
#     print("Robot is ready")
    
    
    
# speed = float(input("Enter speed: "))
# battery = int(input("Robot battery percentage: "))
# distance = float(input("Enter distance: "))

# if battery < 20:
#     print("Battery Low")

# if distance < 50:
#     print("Obstacle detected")
    
# if speed<=0:
#     print("The robot is stop")

# if battery >= 20 and distance >= 50:
#     print("Robot is ready")


# distance=float(input("Enter the distance:"))
# battery=int(input("Enter the distance:"))

# if distance>=50 and battery>=30:
#     print("Robot can move")

# distance=float(input("Enter the distance:"))
# battery=int(input("Enter the battery:"))
# if distance>30 or battery>20:
#     print("Warning!")

# obstacle_detected = False
# if not obstacle_detected:
#     print("The path is clear")
    
    
# battery = 75
# distance = 100
# obstacle_detected = False
# if battery<30:
#     print("Battery low")
# if distance<50:
#     print("Distance to close")
# if obstacle_detected:
#     print("path is clear")

# if battery >=30 and distance>=50 and not obstacle_detected:
#     print("Robot is moving")

# battery=int(input("Enter Battery:"))
# distance=float(input("Enter distance:"))
# obstacle=(input("Enter (yes/no)"))

# if battery <20:
#     print("CRITICAL BATTERY")
# if distance< 30:
#     print("OBSTACLE TOO CLOSE")
# if obstacle=="yes":
#     print("Obstacle was detected")
# if battery>=20 and distance>=30 and obstacle=="no":
#     print("Robot can move")
# if battery<20 or obstacle=="yes":
#     print("Robot must stop")
    
    
# for i in range(1,6):
#     print("Sensor reading ",i)
    
# speed = 2.5

# for i in range(5):
#     speed+=0.5
#     print("Robot speed:", speed, "m/s")
    
# distances = [100, 80, 45, 20, 70]
# for i in range(5):
#     print("Distance ",distances[i])
    
# distances = [100, 80, 45, 20, 70]
# for distance in distances:
#     print("Distance ",distance,"cm")


# distances = [100, 80, 45, 20, 70]
# for distance in distances:
#     if distance<50:
#         print("Distance:",distance,"Obstacle detected")
#     else:
#         print("Distance:",distance,"Pathe clear")
        

# battery=100
# while battery>0:
#     print("Robot is running")
#     battery-=10


# battery = 100
# distance = 100
# while battery>=20:
#     # print("Robot is running b",battery)
#     battery-=10
#     if battery<20:
#         print("Battery Low- robot is stop")
# while distance>= 30:
#     # print("Robot is running d",distance)
#     distance-=5
#     if distance<30:
#         print('Obstacle is detected- robot is stop')
    
# if battery<20 and distance<30:
#     print("Robot is stop")
    

# battery = 100
# distance = 100

# while battery>20 and distance>30:
#     print("Robot is running")
#     print("Battery:", battery)
#     print("Distance:", distance)
#     battery -=10
#     distance-=10
# print('Robot is stoped')
# if battery<=20:
#     print('Battery is low')
# if distance<=30:
#     print('obstacle is detected')
    
# distances = [100, 90, 75, 60, 45, 35, 25, 20]
# for distance in distances:
#     print('Distance',distance)
#     if distance<=30:
#         print('Robot is stoped- obstacle is detected')
#         break
#     print('Robot is moving')

# for i in range(1, 6):

#     if i == 3:
#         continue

#     print(i)
    
# distances = [100, 0, 80, 0, 45, 30, 0, 70]

# for distance in distances:

#     if distance == 0:
#         continue

#     if distance < 50:
#         print("Obstacle:", distance)

#     else:
#         print("Path clear:", distance)


# distances = [100, 0, 80, 45, 0, 35, 25, 90]

# for distance in distances:
#     if distance==0:
#         continue
    
#     # 0 = invalid sensor reading → skip
#     if distance<=30:
#         print('dangerus- stop the robot')
#         break
#     # distance <= 30 = dangerous → stop the robot

#     print("Robot moving:", distance)

# def robot_status():
#     print("Robot is running")
# robot_status()

# def check_distance(distance):
#     if distance<50:
#         print('Obstacle detected')
#     else:
#         print('Path is clear')
# check_distance(100)
# check_distance(30)

# def check_distance(distance):
#     if distance<50:
#         return "Obstacle"
#     else:
#         return "Clear path"
# status=check_distance(49)
# print(status)

# def fun(battery):
#     if battery<20:
#         return "Low Battery"
#     else:
#         return "Good"
# status=fun(10)
# print("Battery status",status)


# def fun(battery,distance):
#     if battery<20:
#         return "Low battery"
#     if distance<30:
#         return "Obstacle detected"
#     return "Robot can move"
# status=fun(90,80)
# print(status)

# def fun(battery,distance):
#     if battery<20:
#         return "Battery Low"
#     if distance<30:
#         return "Obstacle to close"
#     else:
#         return "Path clear"
# battery = 80
# distances = [100, 80, 45, 20, 70]
# for distance in distances:
#     status=fun(battery,distance)
#     print(battery,"|",distance,"|",status)
    


# def fun(battery,distance):
#     if battery<20:
#         return "Battery Low"
#     if distance<30:
#         return "Obstacle to close"
    
#     return "Robot is moving"
# battery_levels = [100, 80, 50, 15, 10]
# distances = [100, 80, 45, 20, 70]
# for battery,distance in zip( battery_levels , distances):
#     status=fun(battery,distance)
#     print(battery,"|",distance,"|",status)
    
    
# distances = [100, 80, 45, 20, 70]
# print(distances[1:3])    

# distances = [100, 80, 45, 20, 70,89]
# if len(distances) >=5:
#     print('Enough sensor readings')
# print(len(distances))


# distances = [100, 80, 45, 20, 70]
# print(distances[0])
# print(distances[-1])
# print(len(distances))


# distances = [100, 80, 45]
# distances.append(20)
# distances.append(70)

# print(distances)


# distances = [100, 80, 45, 20, 70]
# distances.remove(45)
# distances.pop(1)
# print(distances)

# distances = [100, 80, 45, 20, 70]
# results=distances[-3:]
# print(results)
# for result in results:
#     print("Recent distance",result)
    
    
    
# robot_sensors = [
#     [100, 80, 70],
#     [45, 30, 20],
#     [90, 75, 60]
# ]

# print('1 Robot sensor',robot_sensors[0][0])
# print('2 Robot sensor',robot_sensors[1][2])
# print('3 Robot sensor',robot_sensors[2][1])

# robot_sensors = [
#     [100, 80, 70],
#     [45, 30, 20],
#     [90, 75, 60]
# ]
# for sensors in robot_sensors:
#     for distance in sensors:
#         if distance<50:
#             print("Distance:", distance,"|","Obstacle detected")
#         else:
#             print("Distance:", distance,"|","Path clear")
            
# robot = {
#     "name": "Robot-1",
#     "battery": 75,
#     "speed": 3.5,
#     "distance": 80
# }

# print("Robot name:",robot["name"])
# print("Robot name:",robot["battery"])
# print("Robot name:",robot["speed"])
# print("Robot name:",robot["distance"])
        
# robot = {
#     "name": "Robot-1",
#     "battery": 75,
#     "speed": 3.5,
#     "distance": 80
# }

# robot["battery"]=50
# robot["speed"]=2.5
# robot["status"]="moving"


# print(robot)


# robot = {
#     "name": "Robot-1",
#     "battery": 50,
#     "speed": 2.5,
#     "distance": 80,
#     "status": "moving"
# }

# # status ko del se remove karo
# del robot["status"]

# # speed ko pop() se remove karo
# robot.pop("speed")
# print(robot)


# robot = {
#     "name": "Robot-1",
#     "battery": 75,
#     "speed": 2.5,
#     "distance": 100
# }

# for key,value in robot.items():
#     print(key ,":", value)
    

# robot = {
#     "name": "Robot-1",
#     "battery": 15,
#     "speed": 2.5,
#     "distance": 100
# }
# for key,value in robot.items():
#     print(key,":",value)
# if robot["battery"] <20:
#     print("battery is Low")
# else:
#     print("battery is okay")

# robot = {
#     "name": "Robot-1",
#     "battery": 25,
#     "speed": 2.5,
#     "distance": 100
# }
# for key,value in robot.items():
#     if key=="battery":
#         if value<20:
#             print('Battery is low')
#         else:
#             print('Battery is okay')
        
        

# robots = [
#     {
#         "name": "Robot-1",
#         "battery": 80,
#         "speed": 2.5,
#         "distance": 100
#     },
#     {
#         "name": "Robot-2",
#         "battery": 15,
#         "speed": 1.5,
#         "distance": 25
#     },
#     {
#         "name": "Robot-3",
#         "battery": 60,
#         "speed": 3.0,
#         "distance": 70
#     }
# ]

# print(robots[0]['name'])
# print(robots[0])


# robots = [
#     {
#         "name": "Robot-1",
#         "battery": 80,
#         "distance": 100
#     },
#     {
#         "name": "Robot-2",
#         "battery": 15,
#         "distance": 25
#     },
#     {
#         "name": "Robot-3",
#         "battery": 60,
#         "distance": 70
#     }
# ]
# for robot in robots:
#     if robot["battery"]<20:
#         print(robot["name"],"Battery Low")
#     if robot["distance"]<30:
#         print(robot["name"],"Obstacle is detected")
#     else:
#         print('Robot can move')
        

# robot_position = (25, 40)
# x,y=robot_position
# print("Robot X",x)
# print("Robot Y",y)

# sensor_data = (120, 85, 2.5)
# distance,battery,speed=sensor_data
# print("Obstacle distance:",distance)
# print("Robot battery",battery)
# print("Robot speed",speed)

# command = input("Enter command: ")

# if command.lower() == "stop":
#     print("Robot stopped")
    
# ************************************split use for convert string into list************************************
# data = "100 80 45 20"

# distances = data.split()

# print(distances)


# data = "100 80 45 20"
# distances=[float(x) for x in data.split()]
# print("String convert into List: ",distances)


# command = input("Enter robot command: ")

# command = command.strip().lower()

# if command == "forward":
#     print("Robot moving forward")

# elif command == "backward":
#     print("Robot moving backward")

# elif command == "stop":
#     print("Robot stopped")

# else:
#     print("Unknown command")
    
    
    
# def robot_speed(speed=23):
#     print("Robot speed:", speed)


# robot_speed()
# robot_speed(5.0)



# def robot_multipleValues():
#     battery=80
#     distance=100
#     speed=2.5
#     return battery,distance,speed
# battery,distance,speed=robot_multipleValues()
# print("Battery",battery)
# print("Distance",distance)
# print("Speed",speed)


# def robot_data(name="Robot-2", battery=50, speed=4.0):
#     # name, battery, speed return karo
#     return name,battery,speed
# name,battery,speed=robot_data()
# print("Robot name",name)
# print("Robot battery",battery)
# print("Robot speed",speed)



# def check_distances(*distances):
#     for distance in distances:
#         if distance<50:
#             print("Obstacle is detected",distance)
#         else:
#             print("Path is clear",distance)

# check_distances(100, 80, 45, 20, 70)


# try:
#     battery = int(input("Enter battery percentage: "))

#     if battery < 20:
#         print("Battery Low")
#     else:
#         print("Battery OK")

# except ValueError:
#     print("Please enter a number!")
    
    
# try:
#         distance=int(input("Enter distance:"))
#         if distance<30:
#             print("Obstacle detected")
#         else:
#             print("Path clear")
# except ValueError:
#     print("Invalid distance")
            

# try:
#     battery = int(input("Enter battery: "))
#     if battery<20:
#         print("battery low")
#     else:
#         print("battery OK")
        
# except ValueError:
#     print("Invalid battery")
# finally:
#     print("Sensor check completed") 



# class Robot:
#     def __init__(self,name,battery,speed):
#         self.name=name
#         self.battery= battery
#         self.speed= speed
#     def status(self):
#         print(self.name,"Battery",self.battery,"speed",self.speed)

# robot1=Robot("Robo 1",80,15)
# robot2=Robot("Robo 2",60,50)
# # print(robot1.name," ",robot1.battery," ",robot1.speed)
# # print(robot2.name," ",robot2.battery," ",robot2.speed)

# robot1.status()
# robot2.status()

# lambda function and map, Filter

# distances = [5, 12, 3, 20, 8, 15]
# distance_filter=list(filter(lambda x:x>=10,distances))
# print(distance_filter)

# speeds = [10, 20, 30, 40]
# speed_double=list(map(lambda x:x*2,speeds))
# print(speed_double)

# def sensor_data():
#     yield 10
#     yield 20
#     yield 30
# d=sensor_data()
# print(next(d))
# print(next(d))
# print(next(d))

# def robot_battery():
#     # 3 battery readings: 90, 70, 45
#     yield 90
#     yield 70
#     yield 45
# for battery in robot_battery():
#     print("Battery:",battery)
    
# def sensor_readings():
#     yield 10
#     yield 25
#     yield 5
#     yield 30
# for b in sensor_readings():
#     if b>10:
#         print('greater:',b)

# json
        
# import json

# robot = {
#     "name": "Robo1",
#     "battery": 85,
#     "speed": 20
# }

# data = json.dumps(robot)

# print(data)



# import numpy as np
# temperature=np.array([85, 70, 90, 60, 75])
# print(np.mean(temperature))
# print(np.max(temperature))
# print(np.min(temperature))


import numpy as np

# temperature = np.array([24, 26, 28, 30, 32, 34])
# first=temperature[2]
# second=temperature[3]
# third=temperature[1:4]
# fourth=temperature[-3:]
# print(first)
# print(second)
# print(third)
# print(fourth)


# sensor = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])
# print(np.sum(sensor, axis=0))
# print(np.sum(sensor, axis=1))


import numpy as np

# temperature = np.array([24, 31, 28, 35, 22, 40])

# hot = temperature > 30

# print(hot)
# print(temperature[hot])


# temperature = np.array([10, 25, 40, 15, 60, 30])
# hot=temperature[(temperature>20)&(temperature<50)]
# print(hot)


sensor = np.array([10, 25, 40, 15, 60, 30])

indices = np.where(sensor > 30)

print(indices)