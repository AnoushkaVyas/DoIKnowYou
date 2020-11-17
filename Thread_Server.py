import numpy as np
import cv2
import socket
import pickle
import struct
from Recognize import *
import threading
import ClientHandler
import connUtils

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
print("\r[LISN] Socket is now listening") 	 

name = input('Enter your name :')
print('Welcome to DoIKnowYou. This is server.')
# change_port = input('The default port is 4444. Do you want to change the port? Answer "y" or "n" only:')
# if change_port == 'y':
	# ask_port = input('[CAUTION] Do not Ask for an occupied PORT. Enter PORT number (<8888):')
	# PORT = np.int32(ask_port)
	# print('[CAUTION] Enter the same PORT number on client side also.')

while True:
	sys.stdout.write('%s@[Server] -> ' %name)
	sys.stdout.flush()
	command = sys.stdin.readline().strip()

	if (command == 'quit'):
		print('[WARNING] Quitting Server side. If you sent this command in between an operation you might experience bugs. You have been warned.')
		break

	if (command == 'listen'):
		listen()#TODO
