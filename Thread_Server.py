import numpy as np
import cv2
import socket
import pickle
import struct
from Recognize import *
import threading
import ClientHandler
import connUtils

import sys
import os
import time
import matplotlib.pyplot as plt
from Train import *

def quit(command):
    sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sckt.connect((HOST, PORT))
    connUtils.send_one_message(sckt, command.encode('utf-8'))
    sckt.close()
    return

HOST = "localhost"
# Port for socket
PORT = 5000 # Arbitrary non-privileged port
# Bind to the port
try:
	# Create a socket object
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("\r[CONN] Socket successfully created")
except socket.error as err:
	print("\r[FAIL] Socket creation failed with error : ",err)

try:
	server_socket.bind((HOST, PORT))
except socket.error as err:
	print('[FAIL] Bind failed. Error Message :  ',err)
	sys.exit()

print('Socket bind successfully')
print("\r[BIND] Socket binded to : ",PORT)
# Listen for connections : allow only 5 connection
server_socket.listen(5)
print("\r[RDY] Socket is now deployed") 	 

name = input('Enter your name :')
print('Welcome to DoIKnowYou. This is server.')
# change_port = input('The default port is 4444. Do you want to change the port? Answer "y" or "n" only:')
# if change_port == 'y':
	# ask_port = input('[CAUTION] Do not Ask for an occupied PORT. Enter PORT number (<8888):')
	# PORT = np.int32(ask_port)
	# print('[CAUTION] Enter the same PORT number on client side also.')
def listen():
	while True:
		print('\r[CONN] Waiting for client...')
		# Wait to accept a connection - blocking call
		client_socket, addr = server_socket.accept()
		# print the socket object : ip addr and port nb : client info
		print('\r[CONN] Connected from ip: {} and port : {} '.format(addr[0],addr[1]))
		t = threading.Thread(target=ClientHandler.handle_client, args=(client_socket,))
		#t.daemon = True
		t.start()
		if t.is_alive(): 
		    pass 
		else: 
		    print('[THREAD] Serviced Thread.')
		    break 

def train(video, dataset_name):
	face_cascade = './Haar_Cascades/haarcascade_frontalface_default.xml'
	right_eye_cascade = './Haar_Cascades/haarcascade_righteye_2splits.xml'
	left_eye_cascade = './Haar_Cascades/haarcascade_lefteye_2splits.xml'
	if not (os.path.isfile(face_cascade)):
		raise RuntimeError("%s: not found" % face_cascade)
	if not (os.path.isfile(right_eye_cascade)):
		raise RuntimeError("%s: not found" % right_eye_cascade)
	if not (os.path.isfile(left_eye_cascade)):
		raise RuntimeError("%s: not found" % left_eye_cascade)
	samples = 50
	dataset_name = 'dataset/'
	file_name = 'train.yaml'
	radius = 1
	neighbour = 8
	grid_x = 8
	grid_y = 8
	var = list([radius,neighbour,grid_x,grid_y])
	model = Train_Model(face_cascade,right_eye_cascade,left_eye_cascade,var)
	#create a dataset for further model training
	model.create_dataset(samples,video,dataset_name)
	#Training the model
	model.train(dataset_name,file_name)
	

while True:
	sys.stdout.write('%s@[Server] -> ' %name)
	sys.stdout.flush()
	command = sys.stdin.readline().strip()

	if (command == 'quit'):
		print('[WARNING] Quitting Server side. If you sent this command in between an operation you might experience bugs. You have been warned.')
		break

	elif (command == 'listen'):
		print("\r[LISN] Socket is now listening")
		listen()

	elif (command == 'trainVideo'):
		video_name = input('Enter the location to your video : ')
		dataset_name = input("What would you like to call this person? : ")
		video = cv2.VideoCapture(video_name)
		train(video)

	elif (command == 'trainWebc'):
		print('[WARNING] We hope you have a webcam and it is detected by your machine. Running at 640 x 480.')
		priint('Say Cheese !')
		video = cv2.VideoCapture(0)
		video.set(3, 640)
		video.set(4, 480)
		dataset_name = input("What would you like me to call you as? : ")
		train(video, dataset_name)