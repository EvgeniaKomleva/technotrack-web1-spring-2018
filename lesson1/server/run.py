# -*- coding: utf-8 -*-
import socket


def get_response(request):
	line = request.split('\n')[0]
	word = line.split()[1]
	line3 = request.split('\n')[2]
	#name = line3.split()[1:7]
	if word == '/':
		return 'Hello mister!'"\n"'You are:'+ line3
	elif word == '/media/':
		return request
	elif word == '/test/':
		return request.split('\n')[1] + word
	else :
    		return 'Page not found'


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #
server_socket.listen(0)  #

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #
        request_string = client_socket.recv(2048)  #
        client_socket.send(get_response(request_string))  #
        client_socket.close()
    except KeyboardInterrupt:  #
        print 'Stopped'
        server_socket.close()  #
        exit()
#~/example/technotrack-web1-spring-2018/lesson1/server
