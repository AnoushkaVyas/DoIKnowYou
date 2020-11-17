import socket
import numpy as np
import cv2
import pickle
import struct
import time
import sys
import connUtils

PORT = 5000
name = input('Enter your name :')
print('Welcome to DoIKnowYou. This is client.')
# change_port = input('The default port is 4444. Do you want to change the port? Answer "y" or "n" only:')
# if change_port == 'y':
	# ask_port = input('[CAUTION] Enter same PORT number as Server(<8888):')
	# PORT = np.int32(ask_port)
	# print('Your input PORT is ',PORT)



while True:
	sys.stdout.write('%s@[Client] -> ' %name)
	sys.stdout.flush()
	command = sys.stdin.readline().strip()
	if (command == 'quit'):
		print('[WARNING] Quitting Server side. If you sent this command in between an operation you might experience bugs. You have been warned.')
		break
	elif (command == 'video'):
		video_name = input('Enter the location to your video : ')
		video = cv2.VideoCapture(video_name)
	elif (command == 'webcam'):
		print('[WARNING] We hope you have a webcam and it is detected by your machine. Running at 640 x 480.')
		priint('Say Cheese !')
		video = cv2.VideoCapture(0)
		video.set(3, 640)
		video.set(4, 480)

	HOST = 'localhost' 
	TCP_IP = socket.gethostbyname(HOST)  # Domain name resolution
	TCP_PORT = PORT  	 
	CHUNK_SIZE = 4 * 1024	 
	encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

	# socket for sending and receiving images
	Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("\r[CONN] Connecting to server @ ip = {} and port = {}".format(TCP_IP,TCP_PORT))
	Client_Socket.connect((TCP_IP, TCP_PORT))
	print("\r[CONN] Client connected successfully!")