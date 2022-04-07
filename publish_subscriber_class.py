from audioop import add
import requests # Getting the 
import socket
import json 
import pickle

mem_sub_variable = [] # mem subscriber return variable 

class Internal_Publish_subscriber(object): 
        
        def Publisher_dict(self,ip,input_message,port):
            try: 
              exec("sock_"+str(port)+" =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)")
              jsondata = json.dumps(input_message)
              message = pickle.dumps(jsondata)
              exec("sock_"+str(port)+".sendto(message,(ip,port))") # Sending the json data into the udp  
            except ValueError: 
                  print("Connection error via ip: ",str(ip))
                  return 
        def Publisher_string(self,ip,input_message,port):
            try: 
              sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
              
              message = input_message.encode() # Encode string to byte
              sock.sendto(message,(ip,port)) # Sending the json data into the udp  
            except: 
                  print("Connection error via ip: ",str(ip))  
        def Subscriber_dict(self,ip,buffer_size,port): 
            try: 
               exec("sock_"+str(port)+" =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)")
               address = (ip,port) 
               exec("sock_"+str(port)+".bind(address)") 
               exec("global data; data,addr"+ "= sock_"+str(port)+".recvfrom("+str(buffer_size)+")") # Btting the bit operating 
               received = pickle.loads(data)
               message = json.loads(received)
               exec("print(message,type(message),addr)")
               return message
            except:
                print("Subscriber connection value error at ip: ",ip,port) # Getting the report on the ip and port value 
        def Subscriber_string(self,ip,buffer_size,port): 
            try: 
               exec("sock_"+str(ip)+" = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)") 
               address = (str(ip),port) 
               exec("sock_"+str(port)+".bind(address)")  
               exec("global data; data,addr"+ "= sock_"+str(port)+".recvfrom("+str(buffer_size)+")") # Btting the bit operating 
               message = data.decode()
               exec("print(message,type(message),addr)") 
               return message   
            except: 
                print("connection error via ip: ",str(ip))

#Sensors and actuator algorithm type of category 
class Action_control(object): 
           #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
           # Local GPIO
           def DC_motor_driver(self,gipoL,gpioR,pwm):  # DC motor driver 
                  pass
           def Stepper_motor_driver(self,GPIOA,GPIOB,GPIOC,GPIOD,g_code):  # Unipolar stepper motor control with stepper_motor        
                  pass 
           def BLDC_motor_Driver(self,GPIO,pwm):# BLDC motor driver 
                  pass
           #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
           #Serial GPIO 
           def Serial_DC_motordriver(self,serialdev,gpiol,gpior):
                  pass 
           def Serial_stepper_driver(self,serialdev,gpioA,GPIOB,GPIOC,GPIOD,g_code): 
                  pass 
           def Serial_BLDC_motor_Driver(self,GPIO,pwm): 
                  pass
           def Serial_Servo_motor(self,angle):
                   pass 
           #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
           #I2C GPIO 
           def I2C_DC_motordriver(self,serialdev,gpiol,gpior):
                  pass 
           def I2C_stepper_driver(self,serialdev,gpioA,GPIOB,GPIOC,GPIOD,g_code): 
                  pass 
           def I2C_BLDC_motor_Driver(self,GPIO,pwm): 
                  pass  
           #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   
           #Camera data in the raw input      
           def Camera_raw(): # Getting the raw image of the camera  
                  pass 
           def Camera_QR():  # Getting the raw camera image 
                  pass 
           def Camera_yolo(): # Getting the raw yolo image 
                  pass 
           def Camera_Face_recognition(): 
                  pass 
           def Camera_Visual_to_text(): 
                  pass
           #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#a = Internal_Publish_subscriber() 
#a.Publisher_dict("127.0.0.1",{"input":9048},5080) # Sending the data type dicationary now thinking about getting the value input from json file and convert data into the specific data type 

#Getting the input from the hiroku json data component selector to classify the type of the data in the list and getting the new code to generate 
data_ex = {"actuator_1":3,"microcontroller_1":[5,7],"gpio_1":8} # list json to classify and get the message from each devices connected with it
#Check the sensor and the devices hardware connection
#Getting the data input to the pub with the key and value of dict representing the data in the topic and message data type 

def Create_node_pub(topic,message,addresses,initial_port): # Create the node public from the json file input from component selection and define function of the code in the node to control 
       #Create the module of the node component input into the function                
       #Before running the loop of publisher check that the module node is created
       port = initial_port
       address = addresses
       exec("pub_"+str(port)+ "= Internal_Publish_subscriber()")  
       exec("pub_"+str(port)+".Publisher_dict('"+str(address)+"',{"+"'"+str(topic)+"'"+":"+str(message)+"},"+str(port)+")") # Sending the data type dicationary now thinking about getting the value input from json file and convert data into the specific data type 

#Create the sensor receiver as the subscriber for each sensor parameter input from the json component input but this function going to define by json type code generator 
def Create_node_sub(t,addresses,buffer,initial_port):
      
           port = initial_port 
           address = addresses        
           exec("sub_"+str(t)+" = Internal_Publish_subscriber()")  
           exec("global data_return;data_return"+" = sub_"+str(t)+".Subscriber_dict('"+str(address)+"',"+str(buffer)+","+str(port)+")")
           return  data_return 

# Configure port at the node generator 
# Before requesting this publisher and the subscriber 

Create_node_pub("actuators_2",[5,7],"127.0.0.1",5080) # Getting the node created from the json component selection 
Create_node_pub("Servo_1",{"speed":5,"Angle":90},"127.0.0.1",5081)

data_out = Create_node_sub(1,"127.0.0.1",4096,5090) # Getting the local message 
print(data_out)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Create the code from json input firmware writer 
data_ref = {"if_1":{"parameter_1":{"in":["input_parameter","list(data_ex)"]},"for_1":['i',"in range(0,10)"],"print_1":['i']}}  
for r in range(0,len(data_ref)): 
       print(list(data_ref)[r],list(data_ref)[r][0])
       for inner_list in range(0,len(list(data_ref.get(list(data_ref)[r])))):
         print(list(data_ref.get(list(data_ref)[r]))[inner_list])
      


#b = Internal_Publish_subscriber() 
#data_return = b.Subscriber_dict("127.0.0.1",4096,5090) 
#print(data_return)

#c = Internal_Publish_subscriber() 
#c.Publisher_dict("127.0.0.1",{"input_1":5048},5040)




