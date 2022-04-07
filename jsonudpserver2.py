import socket
import json 
import pickle
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
address = "127.0.0.1"
dict_info = {'data_actuator1':'value'} # dictionary data 
jsondata = json.dumps(dict_info)
message = pickle.dumps(jsondata)
sock.sendto(message,(address,5091)) # Sending the json data into the udp  
