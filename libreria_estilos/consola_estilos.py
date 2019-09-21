from termcolor import colored, cprint
import os
from colored import fg, bg
import sys


def styles(t,op):

	def mensage(t,c1,c2,at,sep):
		len_console = int(os.get_terminal_size().columns)
		
		if sep == None:
			len_t = len(t)
			imp = (t.ljust(int(len_t)))
			text = colored(imp,c1,c2,attrs=at)
			print(text,end=" ")	
		else:
			imp = t.center(len_console, sep)
		#mensage(t.center(len_console, '_'),c1,c2,at)
			text = colored(imp,c1,c2,attrs=at)
			print(text)	
		#text = "t.center(len_console, '_'",(fg(1), attr(0))

		
	dict_styles = {
	"grg":['grey','on_green',['bold'],'\t'],
	"grc":['grey','on_cyan',['dark'],' '],
	"cgr":['cyan','on_grey',['underline'],'_'],
	"bw":['blue','on_white',['bold'],'-'],
	"gw":['green','on_white',['blink'],' '],
	"cw":['cyan','on_white',['blink'],' '],
	"mw":['magenta','on_white',['blink'],None],
	"a":['grey','on_yellow',['dark'],'¡'],
	"e":['yellow','on_red',['blink'],'*'],
	"ok":['cyan','on_green',['reverse'],'°'],
	"w":['red','on_grey',['blink'],' '],
	"m":['grey','on_magenta',['blink'],None]
	}
	c1 = dict_styles[op][0]
	c2 = dict_styles[op][1]
	at = dict_styles[op][2]
	sep = dict_styles[op][3]
	mensage(t,c1,c2,at,sep)
	
#print("Control de Errores",fg('white'), bg('yellow'), attr('bold'))


styles("222","grg")
styles("222","grc")
styles("222","cgr")
styles("222","bw")
styles("222","gw")
styles("222","cw")
styles("222","mw")

styles("Alerta","a")
styles("Error","e")
styles("Listo","ok")
styles("Esperandoñññ4444","w")
styles("Esperandoñññ4444","m")





#text_p = colored(text.center(len_console, "="), c1, c2, attrs=at)
#mensage(text.center(len_console, '_'),'red','on_white',['bold'])
#print(text_p)
#cprint("Control de Errores",fg=('white'), bg=('yellow'), attr=('bold'))
	#for men in l_mensages:
	#	men = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
#dict_sesion = {'t':"gggggh",'c1':'blue'}


#text = colored('Hello, World555!', 'red', attrs=['reverse', 'blink'])
#print(text)
