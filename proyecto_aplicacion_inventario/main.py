import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import SwapTransition 
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, ListProperty
import sqlite3, os
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.lang import Builder


class vpinicio(ScreenManager):
	def __init__(self,**argopc):
		super(vpinicio,self).__init__()
	pantallau = StringProperty("Ingreso")
	pantallad = StringProperty("Inventario")
	pantallat = StringProperty("Pendientes")
	pantallaayuda = StringProperty("Ayuda")	
	ventanau = StringProperty("vingreso")
	ventanad = StringProperty("vinventario")
	ventanat = StringProperty("vpendientes")
	ventanaayuda = StringProperty("vayuda")
	coloruno = ListProperty([0,.42,.5])
	colordos = ListProperty([0,.22,.3])
	colortres = ListProperty([0,.82,.9])
	colorcuatro = ListProperty([0,.62,.7])
	colorcinco = ListProperty([0,.32,.4])
	tamanos = ListProperty([(1,.10),(1,.85),(1,.05),(1,1),(1,.1),(1,.9),(1,.2),(1,.5),(1,.33)])
	tipos = ListProperty(["Equipos de Conmutacion Publica","Equipos de Transmicion","Equipos de cliente"])
	conmutacion = ListProperty(["Conmutador Analogico","Conmutador Digital"])
	transmicion = ListProperty(["Lineas Cobre","Lineas Fibra Optica","Estaciones Base Transceptoras","Multiplexores","Bucles Locales","Satelites"])
	cliente = ListProperty(["Conmutador Privado","Redes de Area Local","Modems","Telefono movil","Telefono Fijo","Contestador Automatico","Teletipo","Fax","Buscapersonas","Router"])
	tip = 0
	con = 0
	tran = 0
	cli = 0
	pend = 0
	cant = NumericProperty(0)
	men = ""
	men2 = ""
	ventanaconexion = StringProperty("vinicio")
	transition = SwapTransition()
	ubic = NumericProperty(0)
	textou = StringProperty("sss")
	cons = ListProperty([])
	cantele = StringProperty("0")
	cantpend = 0
	#rutas
	ruta_app = os.getcwd()
	ruta_bd = ruta_app + "/inventario.db"
	
	def mas(self):
		if self.tip < 2:
			self.tip = self.tip + 1
		else:
			self.tip = 0
		self.ids['botontipo'].text = self.tipos[self.tip]
	
	def abrirvencon(self):
		self.ventanaconexion="vinicio"
		self.current = self.ventanaconexion

#conexion a db y envio de datos
	def enviar(self):
		con = sqlite3.connect('inventario.db')
		cur = con.cursor()
		inv = (self.ids['botontipo'].text, self.ids['botonactivo'].text, self.ids['desc'].text, 'pppp', False)
		cur.execute('insert into items(tipo,activo,descripcion,foto,pendiente) values(?,?,?,?,?)',inv)
		con.commit()
#combobox
	def activo(self):
		if self.tip == 0:
			if self.con < 1:
				self.con = self.con + 1
			else:
				self.con = 0
			self.ids['botonactivo'].text = self.conmutacion[self.con]
		if self.tip == 1:
			if self.tran < 5:
				self.tran = self.tran + 1
			else:
				self.tran = 0
			self.ids['botonactivo'].text = self.transmicion[self.tran]
		if self.tip == 2:
			if self.cli < 9:
				self.cli = self.cli + 1
			else:
				self.cli = 0
			self.ids['botonactivo'].text = self.cliente[self.cli]

	def consulta(self):
		self.cant = 0
		con2 = sqlite3.connect('inventario.db')
		cur2 = con2.cursor()
		for p in cur2.execute('select * from items where pendiente = 0'):
			self.cons.append(p)
			self.cant = self.cant + 1
		self.ids['consss'].text = str(self.cant)


	def enviarpend(self):
		if self.cantpend < self.cant - 1:
			self.cantpend = self.cantpend + 1
			
		else:
			self.cantpend = 0
		self.ids['botonpendientes'].text = str(self.cons[self.cantpend])




class MainApp(App):
	title = "Inventario Telefonica"
	def build(self):
		return vpinicio()

if __name__ == "__main__":
	MainApp().run()
