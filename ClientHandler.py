import numpy as np
import cv2
# Import the socket library
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
		
		

	client_socket.close()
	print('\r[SCKT] Socket closed...')
