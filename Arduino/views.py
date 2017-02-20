from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from pyfirmata import Arduino, util
from pins import escrita
import time
def post_list(request):


    analogicas = [line.rstrip('\n') for line in open('/home/pi/config.txt' ,'r')]
    try:
    	x = [int(float(i) * 1000) for i in analogicas]
        
        indice = analogicas
       	for i in range(len(analogicas)):
           indice[i] = i    	
    	
    except:
        x = 500;
    clist = zip(indice,x)
    return render(request, 'Arduino/post_list.html', {'teste' : clist})

def atualiza(request):
 valor = None
 analogicas = [line.rstrip('\n') for line in open('/home/pi/config.txt' ,'r')]
 try:
        x = [int(float(i) * 1000) for i in analogicas]
 except:
        x[0] = 0;
	x[1] = 0;
	x[2] = 0;
	x[3] = 0;
	x[4] = 0;
	x[5] = 0;

 if request.method == 'GET':
        if request.GET.get('q'):
   		message = 'You submitted: %r' % str(request.GET['q'])
	else:
    		message = 'You submitted nothing!'    
 print message
 resposta = """<?xml version="1.0" encoding="UTF-8"?>
<Analogicas>"""
 c = 0
 for i in x:	
	resposta +="<GAUGE"
        resposta += str(c)
	resposta += ">"
 	resposta += "<A>"
        resposta += str(i)
        resposta += "</A>"
	resposta += "</GAUGE"
	resposta += str(c)
        resposta += ">"
  	c += 1
 resposta += "</Analogicas>"
 #print resposta[0]
 return HttpResponse(resposta,content_type='text/xml')
# Create your views here.

def escreve(request):
	if request.method == 'GET':
		pin = str(request.GET.get('pin'))
		value = str(request.GET.get('value'))
		escrita(pin,value)
		print request.GET
	return HttpResponse()

