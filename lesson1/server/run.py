# -*- coding: utf-8 -*-
import socket
from os import listdir 

def get_response(request):
	line = request.split('\n')[0]
	word = line.split()[1]
	line3 = request.split('\n')[2]
	#name = line3.split()[1:7]
	if word == '/':
		return 'Hello mister!'"\n"'You are:'+ line3
	elif word == '/media/':
		fls=['<a href="'+i+'">'+i+'</a><br/>' for i in listdir('../files/')]
		return '\n'.join(fls)
	elif word[:7]=='/media/' and word!='/media/':                             
        	fi=word[7:]                                                   
        	try: 
            		with open('../files/'+fi) as f:                          
                		return f.read()                        
    		except Exception as e:                                              
			return 'File not found'
	elif word == '/test/':
		return request
	else :
    		return 'Page not found'


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  #подсоединяемся к порту 8000
server_socket.listen(0)  #слушаем порт

print 'Started'

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print 'Got new client', client_socket.getsockname()  #получаем данные о новом пользователе
        request_string = client_socket.recv(2048)  #записываем данные в request
        client_socket.send(get_response(request_string))  #получаем ответ
        client_socket.close()
    except KeyboardInterrupt:  
        print 'Stopped'
        server_socket.close()  #останавливаем прослушку порта
        exit()
#~/example/technotrack-web1-spring-2018/lesson1/server
