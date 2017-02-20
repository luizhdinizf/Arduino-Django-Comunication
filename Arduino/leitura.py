import time
from pyfirmata import Arduino, util

board = Arduino('/dev/ttyACM0')
it = util.Iterator(board)
it.start()
board.analog[0].enable_reporting()
board.analog[1].enable_reporting()
board.analog[2].enable_reporting()
board.analog[3].enable_reporting()
board.analog[4].enable_reporting()
board.analog[5].enable_reporting()
time.sleep( 1 )


while 1:
	pins = open("/home/pi/pins.txt", "r")
	config = open("/home/pi/config.txt", 'w')
	A0 = board.analog[0].read()
	A1 = board.analog[1].read()
	A2 = board.analog[2].read()
	A3 = board.analog[3].read()
	A4 = board.analog[4].read()
	A5 = board.analog[5].read()
	config.write("%f \n" % A0)
	config.write("%f \n" % A1)
	config.write("%f \n" % A2)
	config.write("%f \n" % A3)
	config.write("%f \n" % A4)
	config.write("%f \n" % A5)
	config.close()
	print "done"
	c = 2;
	for line in pins:
		print line
		if c < 14:
			board.digital[c].write(int(line))		
		c += 1
	time.sleep(0.1)
	
