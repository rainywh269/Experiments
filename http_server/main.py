#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Python 2
import socket
import threading

class socketEcho(threading.Thread):
  def __init__(self,conn):
      super(socketEcho,self).__init__()
      self.conn = conn

  def run(self):
      data = self.conn.recv(1024)
      if not data: 
        print 'Break'
        self.conn.close()
        return
      data = """GET /index.html HTTP/1.1 
      host: www.esqsoft.globalservers.com

      """
      dataList = data.split()
      URI = dataList[1]
      URI = URI[1:]
      hostAddress = dataList[4]    
      try:
        file = open(URI,'r').read()
        result = ''
        #result = "HTTP/1.1 200 OK \r\nContent-Type: text/html\r\n\r\n"
        result = result + file
      except IOError as e: #HTTP 404
        print "Error"
        pass    
      #conn.send(data)
      print "Sending"
      print result
      try:
        self.conn.send(result)
        self.conn.close()
      except:
        print "Send Error"

HOST = ''
PORT = 50421
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(2) #Blocks, accept only one connection
while True:
  newSock, addr = s.accept()
  print 'Connected by', addr
  newConn = socketEcho(newSock)
  newConn.start()



