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
		print('Say Cheese !')
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

	while True:
		# Capture, decode and return the next frame of the video
		ret, image = video.read()
		if not ret:
			break
		result, frame = cv2.imencode('.jpeg', image, encode_param)
		# Returns the bytes object of the serialized object.
		data = pickle.dumps(frame, 0)
		size = len(data)
		Client_Socket.sendall(struct.pack("l",size) + data)
		print("\r[SCKT] Image is sent successfully ")
		data = b""
		# struct_size is 8 bytes
		struct_size = struct.calcsize("l")
		
		img_size= Client_Socket.recv(struct_size)
		img_size = struct.unpack("l", img_size)[0]
		print(img_size)
		while len(data) < img_size:
			data += Client_Socket.recv(CHUNK_SIZE)
		frame_data = data[:img_size]
		data = data[img_size:]
		frame=pickle.loads(frame_data)
		frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
		cv2.imshow('Video', frame)	
		if cv2.waitKey (1) & 0xff == 27:
			break