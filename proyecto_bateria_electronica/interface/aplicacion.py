import serial,threading,winsound,vlc
from multiprocessing import Process
from time import time

class programa():
	ser = None
	msg = ''
	msg_an = ''
	live_th1 = True
	live_th2 = True
	th3 = ''
	st_time = ''
	dact_time = ''
	dprt_time = ''
	drev_time = ''
	act_time = ''
	prt_time = ''
	rev_time = ''
	instance_vlc = vlc.Instance()
	th3 = ''
	player = instance_vlc.media_player_new()
	media = instance_vlc.media_new('D:\\proyectobateria\\51.mp3')
	player.set_media(media)
	def act(self):
		print("Act ")
		#winsound.PlaySound('51.wav', winsound.SND_FILENAME)
		self.player.play()
	def b_prt(self):
		while self.live_th2:
			if self.msg != self.msg_an:
				self.prt_time=time()
				print(str(self.msg))
				self.dprt_time = time() - self.prt_time
				print("Revision Time "+str(self.drev_time))
				print("Print Time "+str(self.dprt_time))
				self.act_time=time()
				th3 = threading.Thread(target=self.act)
				th3.start()
				#th3.join()
				#th3 = Process(target=self.act)
				self.dact_time = time() - self.act_time
				print("Action Time "+str(self.dact_time))
				self.msg_an = self.msg
	def b_rev(self):
		while self.live_th1:
			self.rev_time=time()
			self.msg = self.ser.readline()
			self.drev_time = time() - self.rev_time
			#print("Revision Time "+str(self.drev_time))
	def __init__(self):
		self.st_time=time()
		self.ser = serial.Serial(port='COM3', baudrate=9600,timeout=0)
		#th1 = Process(target=self.b_rev,args=('world',))
		#th2 = Process(target=self.b_prt,args=('world',))
		th1 = threading.Thread(target=self.b_rev)
		th2 = threading.Thread(target=self.b_prt)
		th1.start()
		th2.start()
if __name__ == '__main__':
	programa()
