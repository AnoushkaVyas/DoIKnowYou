import socket
import os, sys
import tqdm
import struct
import time
import shutil

def send_one_message(sock, data):
    length = len(data)
    sock.sendall(struct.pack('!I', length))
    sock.sendall(data)

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def recv_one_message(sock):
    lengthbuf = recvall(sock, 4)
    if isinstance(lengthbuf,type(None)):
        return None
    length, = struct.unpack('!I', lengthbuf)
    return recvall(sock, length)