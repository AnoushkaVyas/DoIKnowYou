import numpy as np
import cv2
import socket
import pickle
import struct
from Recognize import *
import threading
CHUNK_SIZE = 4 * 1024	
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

def handle_client(client_socket):
	skin_detect = Skin_Detect()
	size1 = (30,30)
	size2 = (80,110)
	scale_factor = 3
	Face_Detect = Face_Detector(skin_detect)
	face_cascade = './Haar_Cascades/haarcascade_frontalface_default.xml'
	file_name = 'train.yaml'
	if not (os.path.isfile(file_name)):
		raise RuntimeError("%s: not found" % file_name)
	if not (os.path.isfile(face_cascade)):
		raise RuntimeError("%s: not found" % face_cascade)

	radius = 1
	neighbour = 8
	grid_x = 8
	grid_y = 8
	var = list([radius,neighbour,grid_x,grid_y])

	model = Recognizer(face_cascade,file_name,var)
	
	while True:
		data = b""
		struct_size = struct.calcsize("l")
		img_size= client_socket.recv(struct_size)
		
		if len(img_size) == 0:
			break
		img_size = struct.unpack("l", img_size)[0]
		
		while len(data) < img_size:
			data += client_socket.recv(CHUNK_SIZE)
			if len(data) == 0 :
				break
		
		frame_data = data[:img_size]
		data = data[img_size:]
		frame=pickle.loads(frame_data)
		frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
		predicted = model.predict(frame,Face_Detect,size1,size2)
		result, frame = cv2.imencode('.jpeg', predicted, encode_param)
		
		data = pickle.dumps(frame, 0)
		size = len(data)
		client_socket.sendall(struct.pack("l",size) + data)

	client_socket.close()
	print('\r[SCKT] Socket closed...')
