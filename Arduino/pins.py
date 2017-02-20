def to_bin(number):
  x = "{0:b}".format(number)  
  x = x.zfill(11)   
  x = x[::-1]
  return x

def escrita(pino,valor): 
  pino = int(pino)
  a = str(valor)  
  a += "\n" 
  pins = open("/home/pi/pins.txt", "r")
  lines = pins.readlines()
  pins.close()
  print "aaaa"
  if (pino<13 and pino>1):
   print "bbbb"
   lines[pino - 2] = a
   pins = open("/home/pi/pins.txt", 'w')
   pins.writelines(lines) 
   pins.close()
   
