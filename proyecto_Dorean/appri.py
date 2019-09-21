# -*- coding: utf-8 -*-
#!/home/edward/Documentos/dorean/app/entdorean/bin/python3

import sys
from tkinter import *
from tkinter import font  as tkfont
from tkinter import ttk
import libraries.estandar as st
import base64
import time
from bs4 import BeautifulSoup
import requests
from tkinter.scrolledtext import ScrolledText
import re
import webbrowser
from subprocess import PIPE, Popen

class aplication():
#variables Style

	
# Principal Frame

	def __init__(self):
		self.app = Tk()
		self.app.title_font = tkfont.Font(family='Helvetica', size="10", weight="bold", slant="italic")
		self.app.title(st.nombre)
		self.vp = Frame(self.app)
		self.vp.title = "DDDDD"
		self.vp.pack(fill=BOTH, expand=YES)
		self.app.attributes("-zoomed", True)
		



# Principal panels	
		self.panelp1 = PanedWindow(self.vp, orient=HORIZONTAL)
		self.panelp1.config(bg=st.coloruno)
		self.panelp1.pack(fill=BOTH, side=TOP, expand=FALSE, pady=0, padx=0)

		self.etiqueta = Label(self.panelp1, text="Descubre Linux¡¡¡")
		self.etiqueta.config(bg=st.coloruno, fg=st.colorcuatro)
		self.etiqueta.pack(fill=BOTH, expand=FALSE, pady=0, padx=0)


		self.panelp2 = PanedWindow(self.vp, orient=HORIZONTAL)
		self.panelp2.config(bg=st.colorcinco)
		self.panelp2.pack(fill=BOTH, expand=TRUE, pady=0, padx=0)
#Internal Panels

		self.paneli1 = PanedWindow(self.panelp2, orient=HORIZONTAL)
		self.paneli1.config(bg=st.colorcinco)
		self.paneli1.place(relwidth=0.3, relheight=1, relx=0, bordermode="outside")

	

		self.paneli2 = PanedWindow(self.panelp2, orient=HORIZONTAL)
		self.paneli2.config(bg=st.coloruno)
		self.paneli2.place(relwidth=0.7, relheight=1, relx=0.3, bordermode="outside")

		self.etiqueta1 = Label(self.paneli2, text="HALLEY")
		self.etiqueta1.config(bg=st.colortres, fg=st.colorcinco)
		self.etiqueta1.pack(fill=X, expand=FALSE)



#Internal Panels Gliese
		self.paneli10 = PanedWindow(self.paneli1, orient=HORIZONTAL)
		self.paneli10.config(bg=st.colordos)
		self.paneli10.place(relwidth=1, relheight=0.4, rely=0, bordermode="outside")

		self.etiqueta2 = Label(self.paneli10, text="GLIESE")
		self.etiqueta2.config(bg=st.colortres, fg=st.colorcinco)
		self.etiqueta2.pack(fill=BOTH, expand=FALSE)

		self.etiqueta3 = Label(self.paneli10, text="Informacion")
		self.etiqueta3.config(bg=st.colortres, fg=st.colorcinco)
		self.etiqueta3.pack(fill=BOTH, expand=FALSE)

		self.paneli11 = PanedWindow(self.paneli1, orient=HORIZONTAL)
		self.paneli11.config(bg=st.colordos)
		self.paneli11.place(relwidth=1, relheight=0.6, rely=0.4, bordermode="outside")
		pag = requests.get('https://www.muylinux.com/')
		aen = pag.encoding = 'utf-8'

		print("Encodsin"+aen)
		pagto = pag.text
#print(str(pagto))
		soup = BeautifulSoup(pag.text, 'lxml')
		articulos = soup.find_all('article')
		labelnot = Label(self.paneli1, text="Noticias")
		labelnot.config(justify=CENTER, bg=st.colortres, fg=st.colorcinco)
		labelnot.pack(fill=BOTH, expand=FALSE, side=TOP)
		for arti in articulos:
			tit = arti.find_all('a')[1].get_text()
			link = arti.find_all('a')[2]
			linka = link['href']
			linka = str(linka)
			articu = arti.find('p').get_text()
			t = str(articu)
			te = ""
			try:
				te = '\n'.join(line.strip() for line in re.findall(r'.{1,80}(?:\s+|$)', t))
				print(te)
			except Exception as e:
				print(str(e))
			#t.config(wrap=WORD)
			label = Label(self.paneli1, text=str(tit))
			label.config(bg=st.coloruno, fg=st.colortres)
			label.pack(fill=BOTH, expand=FALSE, side=TOP)
			labelt = Label(self.paneli1, text=te)
			labelt.config(bg=st.colordoce, fg=st.coloruno)
			labelt.pack(fill=BOTH, expand=FALSE, side=TOP)
			palink = "r\""+str(linka)+"\""
			labelcon = Label(self.paneli1, text=str(palink))
			labelcon.config(bg=st.colordiez, fg=st.coloruno)
			labelcon.pack(fill=BOTH,  side=TOP, expand=FALSE)
			botonint = Button(labelcon, relief='flat', text=linka, anchor=W, bg=st.colordiez, fg=st.coloruno, borderwidth=0, command= self.linker(linka))
			botonint.pack(fill=X, side=TOP, pady=0, padx=0, expand=FALSE)
		self.etiqueta4 = Label(self.paneli11, text="Noticias")
		self.etiqueta4.config(bg=st.colortres, fg=st.colorcinco)
		self.etiqueta4.pack(fill=BOTH, expand=FALSE)
#Internal Panels Halley
		self.panelh1 = PanedWindow(self.paneli2, orient=HORIZONTAL)
		self.panelh1.config(bg=st.coloruno)
		self.panelh1.pack(fill=BOTH, side=TOP, expand=FALSE, pady=0, padx=0)
		self.container = Frame(self.paneli2)
		self.container.config(bg=st.colorcinco)
		self.container.pack(fill=BOTH, expand=YES)
		self.frames = {}
		for F in (StartPage, PageHard, PageSoft, PageRed, PageLib):
			page_name = F.__name__
			self.container.pack(fill=BOTH, expand=TRUE)
			frame = F(parent=self.container, controller=self)
			self.frames[page_name] = frame
			frame.config(bg=st.colorcinco)
			frame.place(relwidth=1, relheight=1, rely=0, relx=0, bordermode="outside")
		self.show_frame("StartPage")
		self.app.mainloop()
	def linker(self, linka):
		pass
	def show_frame(self, page_name):
		frame = self.frames[page_name]
		#frame.pack(fill=BOTH, expand=TRUE)
		titu = page_name
		
		if page_name == "StartPage":
			sec = "Home"
			ahora =  time.strftime("%X")
			ahorat = str(ahora)
			tit = "Dorean %s" % sec+" |"+ahorat+"|"
			self.app.title(tit)
			print("Llegaste a la seccion Principal")
		elif page_name == "PageHard":
			sec = "Hardware"
			ahora =  time.strftime("%X")
			ahorat = str(ahora)
			tit = "Dorean %s" % sec+" |"+ahorat+"|"
			self.app.title(tit)
			print("Llegaste a la pagina de Hardware")
		elif page_name == "PageSoft":
			sec = "Software"
			ahora =  time.strftime("%X")
			ahorat = str(ahora)
			tit = "Dorean %s" % sec+" |"+ahorat+"|"
			self.app.title(tit)
			print("Llegaste a la pagina de Software")
		elif page_name == "PageRed":
			sec = "Redes"
			ahora =  time.strftime("%X")
			ahorat = str(ahora)
			tit = "Dorean %s" % sec+" |"+ahorat+"|"
			self.app.title(tit)
			print("Llegaste a la pagina de Redes")
		elif page_name == "PageLib":
			sec = "Libertad"
			ahora =  time.strftime("%X")
			ahorat = str(ahora)
			tit = "Dorean %s" % sec+" |"+ahorat+"|"
			self.app.title(tit)
			print("Llegaste a la seccion Libre¡¡¡")
		frame.tkraise()
	def labdorean(self, label, txt, colfondo, coletra, exp):
		textt = str(txt)
		label = Label(label, text=textt)
		label.config(bg=colfondo, fg=coletra)
		label.pack(fill=BOTH, expand=exp)
		return label
	def labdorean2(self, label, colfondo, coletra, relx, rely, xx, yy):
		label = Label(label)
		label.config(bg=colfondo, fg=coletra)
		label.place(relwidth=relx, relheight=rely, rely=yy, relx=xx, bordermode="outside")
		return label
	def butdorean(self, lab, controller, textt, colorfondo, coletras, pagina, posicion):
		boton = Button(lab, text=textt, relief='flat', 
			bg=colorfondo, fg=coletras, borderwidth=0, highlightthickness=0, activebackground=coletras, activeforeground=colorfondo, command=lambda: controller.show_frame(pagina))
		boton.pack(fill=BOTH, side=posicion, pady=0, padx=0)
		return boton
	def butdorean2(self, lab, controller, textt, colorfondo, coletras):
		boton = Button(lab, relief='flat', text=textt, anchor=W, bg=colorfondo, fg=coletras, borderwidth=0, highlightthickness=0,
		 activebackground=coletras, activeforeground=colorfondo, command=lambda: controller.valpal(textt))
		boton.pack(fill=X, side=TOP, pady=0, padx=0, expand=FALSE)
		return boton
	def butdorean3(self, lab, controller, textt, colorfondo, coletras):
		boton = Button(lab, relief='flat', text=textt, anchor=W, bg=colorfondo, fg=coletras, borderwidth=0, highlightthickness=0,
		 activebackground=coletras, activeforeground=colorfondo )
		boton.pack(fill=BOTH, side=TOP, pady=0, padx=0, expand=FALSE)
		return boton

	
	
class StartPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        parent.pack(fill=BOTH, side=LEFT, pady=0, padx=0, expand=TRUE)
        label = Frame(self)
        label.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
        label.config(bg=st.coloruno)
        self.botonh1 = controller.butdorean(self, controller, "HARDWARE", st.coloruno, st.colornueve, "PageHard", LEFT)
        self.botonh2 = controller.butdorean(self, controller, "SOFTWARE", st.coloruno, st.colordiez, "PageSoft", LEFT)
        self.botonh3 = controller.butdorean(self, controller, "REDES", st.coloruno, st.coloronce, "PageRed", LEFT)
        self.botonh4 = controller.butdorean(self, controller, "LA LIBERTAD", st.coloruno, st.colorocho, "PageLib", RIGHT)
        st.seccion = "Inicio"
        #self.controller.app.title("ggg")
        labeltit1 = controller.labdorean(label,"Pagina Principal", st.colorseis, st.coloruno, FALSE)
        labelcon1 = controller.labdorean(label, "", st.colorcuatro, st.colorocho, TRUE)
class PageLib(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        parent.pack(fill=BOTH, side=LEFT, pady=0, padx=0, expand=TRUE)
        label = Frame(self)
        label.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
        label.config(bg=st.coloruno)
        self.botonh1 = controller.butdorean(self, controller, "HARDWARE", st.coloruno, st.colornueve, "PageHard", LEFT)
        self.botonh2 = controller.butdorean(self, controller, "SOFTWARE", st.coloruno, st.colordiez, "PageSoft", LEFT)
        self.botonh3 = controller.butdorean(self, controller, "REDES", st.coloruno, st.coloronce, "PageRed", LEFT)
        self.botonh4 = controller.butdorean(self, controller, "HOME", st.gris1, st.colorseis, "StartPage", RIGHT)
        st.seccion = "Libertad"
        #self.controller.app.title("ggg")
        
        labeltit1 = controller.labdorean(label, "La Libertad", st.colorocho, st.coloruno, FALSE)
        labelcon1 = controller.labdorean(label, "", st.colordoce, st.colorocho, TRUE)

class PageHard(Frame):
	def __init__(self, parent, controller):
		parent.pack(fill=BOTH, side=LEFT, pady=0, padx=0, expand=TRUE)
		Frame.__init__(self, parent)
		self.controller = controller
		label = Label(self)
		label.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
		self.botonh1 = controller.butdorean(self, controller, "HOME", st.gris1, st.colorseis, "StartPage", LEFT)
		self.botonh2 = controller.butdorean(self, controller, "SOFTWARE", st.coloruno, st.colordiez, "PageSoft", LEFT)
		self.botonh3 = controller.butdorean(self, controller, "REDES", st.coloruno, st.coloronce, "PageRed", LEFT)
		self.botonh4 = controller.butdorean(self, controller, "LA LIBERTAD", st.coloruno, st.colorocho, "PageLib", RIGHT)
		labeltit1 = controller.labdorean(label,"Hardware", st.colornueve, st.coloruno, FALSE)
		labelcon1 = controller.labdorean(label, "", st.colordoce, st.colornueve, TRUE)
		labelcon3 = controller.labdorean2(labelcon1, st.gris1, st.colorseis, 1, 1, 0, 0)
		procesoh = ["./hard.sh"]
		proch = procesoh
		rprocesh = Popen(proch, stdout=PIPE, stderr=PIPE)
		rprocesh.wait()
		error_econtradoh = rprocesh.stderr.read()
		listadoh = rprocesh.stdout.read()
		#listadot = base64.encodebytes(listado)
		#listado = listado.encoding = 'utf-8'
		print("LIST"+str(listadoh))
		#listado = str(listado)
		st.txuh = str(listadoh).split("\n")
		#print("Lis1"+str(listado)[1])
		textosah = ""
		textosbh = ""
		listextosh = []
		for itemtxuh in st.txuh:
			
			itlh = str(itemtxuh).split("\\n")
			for itemlh in itlh:
				itemlh = str(itemlh).replace("b'", "")
				itemlh = str(itemlh).replace("'", "")
				print("Item"+str(itemlh))
				textosah = str(textosah)+str(itemlh)+"\n"
				textosah = str(textosah)
				listextosah = str(textosah).split("\\n")
				itemlh = str(itemlh)
				if itemlh != "":
					listextosh.append(itemlh)
					for itemtextoh in listextosh:
						itemtextoh =  listextosh
						itemtextoh = str(itemtextoh)
						print("ee"+str(itemtextoh))
			print("Texx"+str(textosah)+"tip"+str(type(textosah)))
			#textosa = textosa.replace("Direc. inet", "Direccion Encontrada")
		print("Texx"+str(textosah))
		labelcon3.config(text=str(textosah))
		labelcon3.place(relwidth=1, relheight=1, rely=0, relx=0, bordermode="outside")

        
		#self.controller.app.title(self.st.nombre)


class PageSoft(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller
		label = Label(self)
		label.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
		self.botonh1 = controller.butdorean(self, controller, "HARDWARE", st.coloruno, st.colornueve, "PageHard", LEFT)
		self.botonh2 = controller.butdorean(self, controller, "HOME", st.gris1, st.colorseis, "StartPage", LEFT)
		self.botonh3 = controller.butdorean(self, controller, "REDES", st.coloruno, st.coloronce, "PageRed", LEFT)
		self.botonh4 = controller.butdorean(self, controller, "LA LIBERTAD", st.coloruno, st.colorocho, "PageLib", RIGHT)
		labeltit1 = controller.labdorean(label,"Software", st.colordiez, st.coloruno, FALSE)
		labelcon1 = controller.labdorean(label, "", st.colordoce, st.colordiez, TRUE)
		labelcon2 = controller.labdorean2(labelcon1, st.colordiez, st.colorseis, 0.15, 1, 0, 0)
		labelcon3 = controller.labdorean2(labelcon1, st.colordoce, st.colorseis, 0.85, 1, 0.15, 0)
		self.botonh1 = controller.butdorean2(labelcon2, controller, "Sistema Operativo", st.blanco, st.colordiez)
		self.botonh2 = controller.butdorean2(labelcon2, controller, "Paquetes", st.blanco, st.colordiez)
		self.botonh1 = controller.butdorean2(labelcon2, controller, "Repositorios", st.blanco, st.colordiez)
		self.botonh2 = controller.butdorean2(labelcon2, controller, "Buscar", st.blanco, st.colordiez)		


class PageRed(Frame):
	
	def butdoreanred(self, lab, textt, colorfondo, coletras, funn, lab2):
		boton = Button(lab, text=textt, relief='flat', bg=colorfondo, fg=coletras, borderwidth=0, highlightthickness=0, activebackground=coletras, activeforeground=colorfondo, command=lambda: self.valpan(funn, lab2))
		boton.pack(fill=X, side=TOP, pady=0, padx=0, expand=FALSE)
		return boton
	def valpan(self,val,lab2):
		print(str(val))
		proceso1 = ["gedit", "doc.doc"]
		proceso2 = ["./ip.sh", "|sort"]
		if val == "txu":
			proceso = proceso2
		rprocess = Popen(proceso, stdout=PIPE, stderr=PIPE)
		rprocess.wait()
		error_econtrado = rprocess.stderr.read()
		listado = rprocess.stdout.read()
		#listadot = base64.encodebytes(listado)
		#listado = listado.encoding = 'utf-8'
		print("LIST"+str(listado))
		#listado = str(listado)
		st.txu = str(listado).split("\n")
		#print("Lis1"+str(listado)[1])
		textosa = ""
		textosb = ""
		listextos = []
		for itemtxu in st.txu:
			
			itl = str(itemtxu).split("\\n")
			for iteml in itl:
				iteml = str(iteml).replace("b'", "")
				iteml = str(iteml).replace("'", "")
				print("Item"+str(iteml))
				textosa = str(textosa)+str(iteml)+"\n"
				textosa = str(textosa)
				listextosa = str(textosa).split("\\n")
				iteml = str(iteml)
				if iteml != "":
					listextos.append(iteml)
					for itemtexto in listextos:
						itemtexto =  listextos
						itemtexto = str(itemtexto)
						print("ee"+str(itemtexto))
						if val == "txu":
							textosa = str(textosa).replace("Direc. inet:", "Direccion IP:")
							textosa = str(textosa).replace("M\\xc3\\xa1sc:", "Mascara de red:")
							textosa = str(textosa).replace("direcci\\xc3\\xb3nHW", "Direccion Fisica:")
			#textosa = str(textosa)+"\n"(())
			print("Texx"+str(textosa)+"tip"+str(type(textosa)))
			#textosa = textosa.replace("Direc. inet", "Direccion Encontrada")
		print("Texx"+str(textosa))
		self.labelcon3.config(bg=st.colorcinco, fg=st.gris1, text=str(textosa))
		self.labelcon3.place(relwidth=0.85, relheight=1, rely=0, relx=0.15, bordermode="outside")
		print("Lis"+str(listado))
			
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller
		label = Label(self)
		label.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
		self.botonh1 = controller.butdorean(self, controller, "HARDWARE", st.coloruno, st.colornueve, "PageHard", LEFT)
		self.botonh2 = controller.butdorean(self, controller, "SOFTWARE", st.coloruno, st.colordiez, "PageSoft", LEFT)
		self.botonh3 = controller.butdorean(self, controller, "HOME", st.gris1, st.colorseis, "StartPage", LEFT)
		self.botonh4 = controller.butdorean(self, controller, "LA LIBERTAD", st.coloruno, st.colorocho, "PageLib", RIGHT)
		#self.txu = StringVar()
		labeltit1 = controller.labdorean(label,"Redes", st.coloronce, st.coloruno, FALSE)
		labelcon1 = controller.labdorean(label, "", st.colordoce, st.coloronce, TRUE)
		labelcon2 = controller.labdorean2(labelcon1, st.coloronce, st.colorseis, 0.15, 1, 0, 0)
		self.labelcon3 = controller.labdorean2(labelcon1, st.colordoce, st.gris1, 0.85, 1, 0.15, 0)
		self.labelcon3.config(textvariable=st.txu)
		self.botontxu = self.butdoreanred(labelcon2, "IP", st.gris1, st.colornueve, "txu", self.labelcon3)
		#txu = Entry(labelcon1)
		#txu.place(relwidth=0.15, relheight=0.1, rely=0, relx=0, bordermode="outside")
		textored1 = []
		


		
		
def main():
    mi_app = aplication()
    return 0

if __name__ == '__main__':
    main()